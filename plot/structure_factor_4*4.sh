for (( kx=0; kx <= 100; kx+=5 ))
do
	for (( ky=0; ky <= 100; ky+=5 ))
	do
	{
    	echo "sh: kx:$kx ky:$ky done"
		python3 test_ffn_structure_factor_x.py 4 1 1000 $kx $ky
		echo "sh: kx:$kx ky:$ky done"
	} & done
	wait
done

for (( kx=0; kx <= 100; kx+=5 ))
do
	for (( ky=0; ky <= 100; ky+=5 ))
	do
	{
    	echo "sh: kx:$kx ky:$ky done"
		python3 test_ffn_structure_factor_x.py 5 1 1000 $kx $ky
		echo "sh: kx:$kx ky:$ky done"
	} & done
	wait
done

for (( kx=0; kx <= 100; kx+=5 ))
do
	for (( ky=0; ky <= 100; ky+=5 ))
	do
	{
    	echo "sh: kx:$kx ky:$ky done"
		python3 test_ffn_structure_factor_x.py 6 1 1000 $kx $ky
		echo "sh: kx:$kx ky:$ky done"
	} & done
	wait
done