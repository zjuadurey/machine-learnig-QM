for (( ky=0; ky <= 100; ky+=4 ))
do
	for (( kx=0; kx <= 100; kx+=4 ))
	do
    	python3 test_ffn_structure_factor_xx.py 5 0.01 1000 $kx $ky
	done
done