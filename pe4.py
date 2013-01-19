
def check(a ,b):
    return[i for i, j in zip(a, b) if i == j]
    
    

    


maxp =0;
maxi=0
for i in range(10,1000):
    for j in range(10,1000):
        num_str = list(str(i*j));
        rev_str = reversed(num_str);
        if (check(num_str ,rev_str ) == num_str):
            if (maxp<i*j):
                maxp =i*j;maxi=i;



print maxp, maxi, maxp/maxi
