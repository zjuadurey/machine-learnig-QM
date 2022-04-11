# 毕设总体路线梳理
## 一 算法总体框架
### 1 定义哈密顿量
首先需要定义我们要处理的自由度（例如，如果我们有自旋，玻色子，费米子等），方法是指定问题的希尔伯特空间完成
```
hi = nk.hilbert.Spin(s = 0.5, N = graph.n_nodes)
```
然后指定哈密顿量。
```
H: LocalOperator(dim=16, #acting_on=64 locations, constant=0, dtype=float64)
```
### 2 精确对角化($4\times4$之前可以验证算法精度)
```
sp_h=H.to_sparse()
sp_h.shape
```
### 3 哈密顿量基态的变分近似/平均场近似
首先可以尝试使用一个非常简单的平均场近似
$\langle \sigma^{z}_1,\dots \sigma^{z}_N| \Psi_{\mathrm{mf}} \rangle = \Pi_{i=1}^{N} \Phi(\sigma^{z}_i)$

定义一个近似于波函数振幅(或密度矩阵值)的对数的变分函数,我们称这个变分函数为模型

$\langle \sigma^{z}_1,\dots \sigma^{z}_N| \Psi_{\mathrm{mf}} \rangle = \exp\left[\mathrm{Model}(\sigma^{z}_1,\dots \sigma^{z}_N ; \theta ) \right]$

$\theta$是是一组参数

模型本身只是一组关于如何初始化参数和如何计算结果的指令

为了实际创建具有其参数的变化状态，最简单的方法是构造一个蒙特卡罗采样的变分状态。为此，我们首先需要定义采样器，这里使用一个简单的默认采样器：一个一个地将配置中的自旋翻转
### 4 变分蒙特卡洛
##### 4a 优化循环 
优化(或训练)循环必须做一件非常简单的事情:在每次迭代中，它必须计算能量和它的梯度，然后将梯度乘以一定的学习率λ=0.05，最后它必须用这个缩放的梯度更新参数
##### 4b netket自带优化循环
```
# First we reset the parameters to run the optimisation again
vstate.init_parameters()

# Then we create an optimiser from the standard library.
# You can also use optax.
optimizer = nk.optimizer.Sgd(learning_rate=0.05)

# build the optimisation driver
gs = nk.driver.VMC(H, optimizer, variational_state=vstate)

# run the driver for 300 iterations. This will display a progress bar
# by default.
gs.run(n_iter=300)

mf_energy=vstate.expect(H)
error=abs((mf_energy.mean-eig_vals[0])/eig_vals[0])
print("Optimized energy and relative error: ",mf_energy,error)
```

#### 5 