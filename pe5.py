from math import *

def checknum(n):
    array = range(2,21);
    for i in array:
        if(n%i != 0):
            return False;
    return True

j=9699690;
while (j <= factorial(20)):
    if (checknum(j)):
        print j
        
    j += 9699690;
    
