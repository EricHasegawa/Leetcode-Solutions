class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True] * n
        
        i = 2
        while (i * i) < len(primes):
            if primes[i]:
                j = i
                while (j * i) < len(primes):
                    primes[i * j] = False
                    j += 1
            i += 1
        primeCount = 0
        for i in range(2, n):
            if primes[i]:
                primeCount += 1
        
        return primeCount
