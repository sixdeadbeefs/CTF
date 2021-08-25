import string
from pwn import *
import time

flagv = "see_rEv_aint_so_bad"

for _ in string.printable:
    for i in range(0,len(flagv)+1):
        flag = "corctf{" + flagv[:i] + _ + flagv[i:] + "}"
        p = process("./babyrev")
        p.sendline(flag)
        #time.sleep(0.1)
        print("Trying: "+flag)
        answer = p.recvline()
        if "correct" in answer.decode("utf-8"):
            print("CONGRATS")
        else:
            p.close()
