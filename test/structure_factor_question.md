#

$S^{xx}(\vec{k})=\frac{1}{N(N-1)}\sum_{l\neq j}e^{-i\vec{k}.(\vec{r_l}-\vec{r_j})}\langle\sigma_l^x\sigma_j^x\rangle,$

#

k = (kx, ky)  这个kx和ky应该在哪里改变呢

```python
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

import cmath
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
```

2. 什么间隔比较合适呢？