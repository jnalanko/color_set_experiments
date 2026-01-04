for i in range(1, 17+1):
    n = 2**i
    input = f"fof/salmonella_fof_{n}.txt"
    sbwt = f"SBWTs/salmonella_{n}.sbwt"
    lcs = f"SBWTs/salmonella_{n}.lcs"
    output = f"themisto2/salmonella_{n}.thm2"
    log_output = f"logs/salmonella_{n}_themisto.log"

    print(f"/usr/bin/time -v themisto2 build -i {input} --sbwt {sbwt} --lcs {lcs} -o {output} --temp-dir temp -k 31 -d 30 -t 32 --index-type sparse-dense 2>&1 | tee {log_output}")
