array = [True] * int(2e6)


for i in xrange(2,int(2e6**0.5)+1):
    for j in xrange(2*i , len(array), i):
        array[j] = False


print sum(i for i in range(2,len(array)) if array[i]) 





""""


def isprime(n):
    # from 3 since no even numbers in the main loop
    for x in xrange(3, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True



sum=0;
for i in xrange(1,int(2e6),2):
    if isprime(i):
        sum += i
"""

    
"""
sieve = [True] * 2000000 # Sieve is faster for 2M primes
#print sieve
def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: mark(sieve, x)

print sum(i for i in xrange(2, len(sieve)) if sieve[i])

"""
