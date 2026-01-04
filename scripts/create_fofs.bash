input="fof/salmonella_fof.txt"

for i in $(seq 1 17); do
    n=$((2**i))
    head -n "$n" "$input" > "fof/salmonella_fof_${n}.txt"
done
