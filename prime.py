t=int(input('enter the time you want to run the program'))
while t>0:
    n=int(input('enter the number you want to check whether it is prime or  not'))
    def prime(k):
        count=0
        for i in range(1,k+1,1):
            if k%i==0:
                count+=1
        if count==2:
            return 1
        else :
            return 0
    if prime(n)==1:
          print('Number you enter is a prime number')
    else :
          print('Not prime number')
    t-=1

