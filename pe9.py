for c in range(3,1000):
    for a in range(0,c):
        for b in range(a+1,c):
            if (a**2 + b**2 == c**2):
                if (a+b+c == 1000):
                    print a*b*c

        
