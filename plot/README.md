# README

```sh
#generate all we need(energy, structure factor, conherence, etc)
python3 test_ffn_all.py L J iterations
```



```sh
#generate structure factor only
python3 test_ffn_structure_factor.py L J iterations
```

test_ffn_structure_factor.py

```sh
#generate structure factor x attached to the kx & ky
python3 test_ffn_structure_factor_x.py L J iterations kx ky

( kx, ky ranging(0,100)(int) )
```
