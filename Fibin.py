def fibin(n):
    if n==0: return 0
    if n==1: return 1
    else:
        return fibin(n-1)+fibin(n-2)

def fin(n):
    if(n==1):
        return 1;
    if(n==0):
        return 0;
    for i in range(n):
        ans=fin(i-1)+fin(i-2)
    return ans

print(fibin(3))
#print(fin(3))