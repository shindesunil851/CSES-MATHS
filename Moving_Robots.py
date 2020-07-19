
from collections import deque, defaultdict, Counter, OrderedDict
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from heapq import heappush, heappop, heapify, nlargest, nsmallest

import os
import sys
sys.setrecursionlimit(1<<30)
from io import BytesIO, IOBase
import math
import bisect
from math import inf
import random
ins = lambda: [int(x) for x in input()]
inp = lambda: int(input())
inps = lambda: [int(x) for x in input().split()]

inpu=lambda :[x for x in input()]
from fractions import Fraction as F
mx=int(1e3)+1
md=pow(10,9)+7
#print(pr[17],"P")
#print(primes)



#print(fc)

def main():
    n=inp()
    ans=[[1]*8 for _ in range(8)]

    res=[[[0]*8 for _ in range(8)] for _ in range(n+1)]

    
    for i1 in range(8):
        for j1 in range(8):
            res=[[[0]*8 for _ in range(8)] for _ in range(n+1)]
            res[0][i1][j1]=1
            for k in range(n):
            #    res[k][i][j]=1
                
                for i in range(8):
                    for j in range(8):
                        md=0
                        if i>0:
                            md+=1
                        if j>0:
                            md+=1
                        if i<7:
                            md+=1
                        if j<7:
                            md+=1
                        
                        if i:
                            res[k+1][i-1][j]+=res[k][i][j]/md
                        
                        if i<7:
                            res[k+1][i+1][j]+=res[k][i][j]/md
                        
                        if j<7:
                            res[k+1][i][j+1]+=res[k][i][j]/md

                        if j>0:
                            res[k+1][i][j-1]+=res[k][i][j]/md
            for i2 in range(8):
                for j2 in range(8):
                    ans[i2][j2]*=(1-res[n][i2][j2])


    sm=0
    #print(ans)
    for i in range(8):
        for j in range(8):
            sm+=ans[i][j]
    #print(round(sm/pow(6,n),6))
    print("{:.6f}".format(sm))

   




BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
# endregion
 
if __name__ == "__main__":
    main()
# import threading,sys
# sys.setrecursionlimit(1000000)
# threading.stack_size(1024000)
# thread=threading.Thread(target=main)
# thread.start()
