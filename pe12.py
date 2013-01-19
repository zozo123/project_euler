def divisor(n):
    div = 0;
    for i in xrange(1,int(n/2)+1):
        if(n%i == 0):
            div += 1
    return div
    


MAX_INT = int(1e5)
for i in xrange(1000,int(MAX_INT)):
    sum = (i+1)*i/2;
    if divisor(sum) > 500:
        print sum;
   

"""

b = divisor(500);
primes = [2,3,5,7,11,13,15,17,19]

dic ={};

for p in primes :
   dic[p]=  [p**div for div in b]




"""

