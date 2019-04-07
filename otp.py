##OTP generation
import random
print('enter the size of otp 4 or 6')
size=int(input())
list1=[]
if size==4 or size==6:
       for i in range(0,size,1):
        list1.append(random.randint(0,9))
for j in list1:
    print(j,end='')
    
        
