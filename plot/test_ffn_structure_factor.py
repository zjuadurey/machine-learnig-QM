import netket as nk
import numpy as np
import jax.numpy as jnp
import cmath
import math
import sys



# Flax is a framework to define models using jax
import flax
# we refer to `flax.linen` as `nn`. It's a repository of 
# layers, initializers and nonlinear functions.
import flax.linen as nn

import jax
import jax.numpy as jnp                # JAX NumPy

from flax import linen as nn           # The Linen API
from flax.training import train_state  # Useful dataclass to keep train state

import numpy as np                     # Ordinary NumPy
import optax  

#晶格相互作用对定义
size = (7,7)
row_num, col_num = size
n_lattice = row_num * col_num
num = [ i for i in range(row_num * col_num)]

begin = [ i * col_num for i in range(row_num)]
end = [(i + 1) * col_num - 1 for i in range(row_num)]

edgesx = []
edgesy = []
edgesz = []

for i in num:
    if i in begin:
        edgesx.append([i, i + col_num - 1])
    else:
        edgesx.append([i, i - 1])

for i in num:
    if i in num [ :col_num]:
        edgesy.append([i, num[- (col_num - i)]])
    else:
        edgesy.append([i, i - col_num])

for i in num:
    if i in num [-col_num:-1]:
        edgesz.append([i, num[- (col_num*3 - i)]+1])
    elif i in end:
        if i==n_lattice-1:
            edgesz.append([0, i])
        else:
            edgesz.append([i, i + 1])     
    else:
        edgesz.append([i, i + col_num + 1])

edges = edgesx + edgesz + edgesy
graph = nk.graph.Graph(edges)
graph.nodes()

#希尔伯特空间
hi = nk.hilbert.Spin(s = 0.5, N = graph.n_nodes)

#pauli matrix
sx = [[0, 1], [1, 0]]
sy = [[0, -1j], [1j, 0]]
sz = [[1, 0], [0, -1]]
#parameter
h=1
J=float(sys.argv[1])
#g = J / h
H = nk.operator.LocalOperator(hi)
for i in edges:
    H += -J*nk.operator.LocalOperator(hi, np.kron(sz, sz), i)
sxx = -h* nk.operator.LocalOperator(hi, [sx] * n_lattice, [[i] for i in range(n_lattice)])
H += sxx #This term is magnetization, which can be regarded as an operator Mx(g)


#神经网络量子态
class FFN(nn.Module):
    
    # You can define attributes at the module-level
    # with a default. This allows you to easily change
    # some hyper-parameter without redefining the whole 
    # flax module.
    alpha : int = 1
            
    @nn.compact
    def __call__(self, x):

        # here we construct the first dense layer using a
        # pre-built implementation in flax.
        # features is the number of output nodes
        # WARNING: Won't work with complex hamiltonians because
        # of a bug in flax. Use nk.nn.Dense otherwise. 
        dense = nn.Dense(features=self.alpha * x.shape[-1])
        
        # we apply the dense layer to the input
        y = dense(x)

        # the non-linearity is a simple ReLu
        y = nn.relu(y)
                
        # sum the output
        return jnp.sum(y, axis=-1)

# Create the local sampler on the hilbert space
sampler = nk.sampler.MetropolisLocal(hi)

model = FFN(alpha=1)

vstate = nk.vqs.MCState(sampler, model, n_samples=1008)

obs={}

def d1tod2(po, row_num, col_num):
    # po -> (px, py)
    if po < 0 or po >= row_num*col_num:
        print("Wrong Index!")
    else:
        return 0.5*((po-(po//col_num)*col_num+(po//col_num)/2)*2), (math.sqrt(3)/2)*(po//col_num)
    
def d1tod2pbc(po, row_num, col_num):
    # po -> (px, py)
    if po < 0 or po >= row_num*col_num:
        print("Wrong Index!")
    else:
        return 0.5*((po-(po//col_num)*col_num+(po//col_num)/2)*2)+col_num, (math.sqrt(3)/2)*(po//col_num)


####### ################ Structure FactorX ###########################################
msxsx = (np.kron(sx, sx)) 
sfx = []
sitesfx = []
for i in range(0, n_lattice):
    xi, yi = d1tod2(i, row_num, col_num)
    for k in range(i, n_lattice):
        if i==k:
            pass
        else:
            xk1, yk1 = d1tod2(k, row_num, col_num)
            xk2, yk2 = d1tod2pbc(k, row_num, col_num)
#             dis = min(math.sqrt(abs(xi-xk1)**2+abs(yi-yk1)**2), math.sqrt(abs(xi-xk2)**2+abs(yi-yk2)**2))
            absx = min(abs(xi-xk1),abs(xi-xk2))
            sfx.append((cmath.exp(-complex(0,2*absx*3.14/3))*msxsx).tolist())
            sitesfx.append([i,k])

structure_factorx = nk.operator.LocalOperator(hi, sfx, sitesfx)
obs.update(StructureFactorX=structure_factorx)

optimizer = nk.optimizer.Sgd(learning_rate=0.01)

# Notice the use, again of Stochastic Reconfiguration, which considerably improves the optimisation
gs = nk.driver.VMC(H, optimizer, variational_state=vstate,preconditioner=nk.optimizer.SR(diag_shift=0.01))


#################### here  J & iter are needed to be changed ####################
log=nk.logging.RuntimeLog()
gs.run(n_iter=1000,out="log_data_7*7/<text%0.2f_iter_1000_7*7>"%(J), obs=obs)

ffn_energy=vstate.expect(H)
#error=abs((ffn_energy.mean-eig_vals[0])/eig_vals[0])
print("Optimized energy and relative error: ",ffn_energy)