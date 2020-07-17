def sumOfDivisors(n):
    ans=0
    i=1
    while(i<=n):
        r=n//(n//i)
        ans+=(n//i)*((r*(r+1))//2-i*(i-1)//2)
        i=r+1
    return ans%(10**9+7)
n=int(input())
print(sumOfDivisors(n))