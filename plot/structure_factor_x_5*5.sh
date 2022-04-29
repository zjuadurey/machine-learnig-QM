for (( kx=70; kx <= 100; kx+=5 ))
do
	for (( ky=0; ky <= 100; ky+=5 ))
	do
		echo "sh: kx:$kx ky:$ky start"
    	python3 test_ffn_structure_factor_x.py 5 0.01 1000 $kx $ky
		echo "sh: kx:$kx ky:$ky done"
	done
done