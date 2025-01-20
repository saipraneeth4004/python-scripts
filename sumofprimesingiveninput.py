n=int(input())
sum=0
for i in range(n):
    k=int(input())
    if(k!=1):
        fact=0
        for j in range(2,k):
            if(k%j==0):
                fact=1 
        if(fact==0):
            sum=sum+k
print(sum)


