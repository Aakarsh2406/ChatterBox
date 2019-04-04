n=int(input('enter the 1 number'))
m=int(input('enter the 2 number'))
c=min(n,m)
a=n
b=m
p=2
f=1
for i in range(2,c+1):
    if n%p==0 and m%p==0:
        n=n//p
        m=m//p
        f*=p
    else:
        p+=1
print(a*b//f)
