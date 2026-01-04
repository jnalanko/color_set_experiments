for i in range(1, 17+1):
    n = 2**i
    input = f"fof/salmonella_fof_{n}.txt"
    output = f"SBWTs/salmonella_{n}"
    log_output = f"logs/salmonella_{n}_sbwt.log"
    
    print(f"/usr/bin/time -v sbwt build --input-list {input} -t 32 -v -o {output} --temp-dir temp --in-memory -l -k 31 -m 100 -d -r 2>&1 | tee {log_output}")
