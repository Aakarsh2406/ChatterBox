no=int(input('enter the number'))
ch=''
def Arms(k):
    cpy=k
    sum=0
    while(k>0):
        d=k%10
        k=k//10
        sum+=pow(d,3)
    if cpy==sum:
        return  1
    else :
        return 0
a=Arms(no)
if a==1:
    print('ARMSTRONG NUMBER')
else:
    print('NOT ARMSTRONG NUMBER')
