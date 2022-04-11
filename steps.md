# 毕设总体路线梳理
## 1 算法总体框架

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
### 3 找到这个哈密顿量基态的变分近似

