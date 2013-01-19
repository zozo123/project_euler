def isprime(n):
    '''check if integer n is a prime'''
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True
 


n=1;
i=0
while (i < 10001):
    n += 1;
    if isprime(n):
        i += 1
    

print i , n

      
