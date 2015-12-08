import time

curTime = time.time()

def Primes(N):
    primes = [i for i in range(1, N + 1)]
    primes[0] = 0
 
    for i in range(0, N):
        if primes[i] != 0:
            for j in range(i + primes[i], N, primes[i]):
                primes[j] = 0
 
    return [x for x in primes if x != 0]
K = 30
Primes(K) 
# 10 ^ 7  
newTime = time.time()
print (Primes(K))
print (".............\n")
print ((float)(newTime - curTime)) 