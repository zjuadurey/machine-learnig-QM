for g in 0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40 0.45 0.50 0.55 0.60 0.65 0.70 0.75 0.80 0.85 0.90 0.95 1.00
    do
    {    echo "test_ffn_all.py 6 $g 1000"
        python3 test_ffn_all.py 6 $g 1000
    } & done
wait
#python3 test_ffn_all.py 7 0.00 1000

for g in 0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40 0.45 0.50 0.55 0.60 0.65 0.70 0.75 0.80 0.85 0.90 0.95 1.00
    do
    {    echo "test_ffn_all.py 5 $g 1000"
        python3 test_ffn_all.py 5 $g 1000
    } & done
wait


for g in 0.00 0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40 0.45 0.50 0.55 0.60 0.65 0.70 0.75 0.80 0.85 0.90 0.95 1.00
    do
    {    echo "test_ffn_all.py 4 $g 1000"
        python3 test_ffn_all.py 4 $g 1000
    } & done
wait