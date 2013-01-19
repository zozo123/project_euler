fn_1 = 1
fn_2 = 1
n=2
while True:
    fn = fn_1 + fn_2
    n += 1
    fn_2 = fn_1
    fn_1 = fn
    if len(str(fn)) == 1000:
        print fn
        print n
        break;
