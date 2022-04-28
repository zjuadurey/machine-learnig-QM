for (( kx=0; kx <= 100; kx+=4 ))
do
	for (( ky=0; ky <= 100; ky+=4 ))
	do
    	python3 test_ffn_structure_factor_xy.py 7 0.01 1000 $kx $ky
        echo "kx:$kx ky:$ky done"
	done
done