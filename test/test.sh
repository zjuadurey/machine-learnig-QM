for ((ky = 50; ky <= 100; ky+=5))
do
	echo "sh: kx:45 ky:$ky start"
done

for (( kx=50; kx <= 100; kx+=5 ))
do
	for (( ky=0; ky <= 100; ky+=5 ))
	do
		echo "sh: kx:$kx ky:$ky start"
	done
done