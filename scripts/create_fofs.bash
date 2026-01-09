input="fof/random_fof_all.txt"

for i in $(seq 1 14); do
    n=$((2**i))
    head -n "$n" "$input" > "fof/random_fof_${n}.txt"
done
