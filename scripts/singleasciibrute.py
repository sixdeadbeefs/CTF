import string
from pwn import *
import time

flagv = "see_rEv_aint_so_bad"
#a = string.printable
#letter = ['a','b','c','d','e','f','g','h','0','1','2','3','4','5','6','7','8','9','0']

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
