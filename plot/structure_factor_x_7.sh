for ((ky = 15; ky <= 100; ky+=5))
do
	echo "sh: kx:10 ky:$ky start"
	python3 test_ffn_structure_factor_x.py 7 0.01 1000 15 $ky
	echo "sh: kx:10 ky:$ky start"
done

for (( kx=20; kx <= 100; kx+=5 ))
do
	for (( ky=0; ky <= 100; ky+=5 ))
	do
		echo "sh: kx:$kx ky:$ky start"
    	python3 test_ffn_structure_factor_x.py 7 0.01 1000 $kx $ky
        echo "sh: kx:$kx ky:$ky done"
	done
done