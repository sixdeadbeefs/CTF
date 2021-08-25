from sys import stdin
from Crypto.Util.number import bytes_to_long, getStrongPrime, long_to_bytes, isPrime

import subprocess
import nclib

def nextPrime(n):
    while True:
        n += (n % 2) + 1
        if isPrime(n):
            return n

def main():
    current_p = 499
    LIMIT = 64
    x = 1

    primes = []
    remainders = []
    # nc crypto.be.ax 6000
    proc = subprocess.Popen("nc crypto.be.ax 6000", stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, shell=True)
    g = proc.stdout.readline().decode("ASCII")
    print(g)
    g = int(g.split(":")[1].strip())

    p = proc.stdout.readline().decode("ASCII")
    print(p)
    p = int(p.split(":")[1].strip())

    enc = proc.stdout.readline().decode("ASCII")
    print(enc)
    enc = int(enc.split(":")[1].strip())

    for _ in range(LIMIT):
        proc.stdin.write(bytes(str(current_p) + "\n", "ASCII"))
        proc.stdin.flush()

        g_x_div_current_p = proc.stdout.readline().decode("ASCII")
        print(g_x_div_current_p)
        g_x_div_current_p = int(g_x_div_current_p.split(">")[-1].strip())
        
        g_x_div_current_p_times_p = pow(g_x_div_current_p, current_p, p)

        primes.append(current_p)
        for mds in range(current_p):
            if (pow(g, mds, p) * g_x_div_current_p_times_p) % p == enc:
                remainders.append(mds)
                break

        # if pow(g_x_div_current_p, current_p, p) == enc:
        #    # the current prime is a prime factor of x
        #     print("found_factor:", current_p)
        #     x *= current_p
        #     print("current_x", x)
        #     if pow(g, x, p) == enc:
        #         print("found x:", x)
        #         exit()
        # else:
        #     print("not_a_factor:", current_p)
        
        current_p = nextPrime(current_p)
    proc.kill()
    print(primes)
    print(remainders)

main()