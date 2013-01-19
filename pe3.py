def isprime(n):
    '''check if integer n is a prime'''
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


i=1;
while (i <= 600851475143) :
     if (isprime(i) and 600851475143 % i == 0):
        print i
     i += 1;

        
