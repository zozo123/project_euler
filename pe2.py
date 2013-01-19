a = [1,2]
sum =0
while (a[1] <= int(4e6)):
    if (a[1] % 2 == 0):
        sum += a[1];
    a[0],a[1] = a[1],(a[0]+a[1])

print sum
