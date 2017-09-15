def search(x,n,start,end):
    if start==end:
        if x[start]==n: return n
        if x[start]!=n: return False
    else:
        mid = int((start+end)/2)
        if(x[mid]>n):
            return search(x,n,start,mid-1)
        if(x[mid]<n):
            return search(x,n,mid+1,end)
        if(x[mid]==n):
            return mid;

def search2(x,n):
    start=0
    end=len(x)-1

    found=False
    while start<=end and not found:
        mid = int((end + start) / 2)
        if(x[mid]>n):
            end = mid-1
        elif(x[mid]<n):
            start = mid+1
        elif(x[mid]==n):
            return n
    return found


x = [1,2,3,4,5]
n=52
start=0
end = len(x)-1
#result=search(x,n,start,end)
result=search2(x,n)
print(result)