n=int(input())
space=0 
star=n*2-1 
for i  in range(1,n+1):
    print(" "*space+"*"*star)
    star=star-2 
    space+=1 
