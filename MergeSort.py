def mergesort(x):
    if len(x)==1 or len(x)==0:
        return x;
    else:
        middle = int(len(x)/2)
        a=mergesort(x[:middle])
        b=mergesort(x[middle:])
        return merge(a,b)

def merge(a,b):
    c = []
    while len(a)!=0 and len(b)!=0:
        if(a[0]<b[0]):
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a)==0:
        c+=b;
    else:
        c+=a;
    return c

x = [1,9,2,3,4,5]
merged_array = mergesort(x)
print("init: ",x)
print("merged: ",merged_array)