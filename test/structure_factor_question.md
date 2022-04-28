#

```python
#1(暂时用的这个)
sfxy.append ( 
                (
                    cmath.exp(-complex(0, absx * kx ))*msxsx 
                    +
                     cmath.exp(-complex(0, absy * ky ))*msysy
                ).tolist() 
            )

#2
sfxy.append(
                (
                cmath.exp(
                    -complex(
                        0,absx*kx + absy*ky)
                        )
                    )
                    *(msxsx+msysy)
                ).tolist()
            )


#3
sfxy.append( 
    (
        cmath.exp(
                    -complex( 0, absx*kx*msxsx + absy*ky*msysy )
                )
        ).tolist() 
    )
```
