list1=[]
l=int(input('enter the size of list'))
for i in range(0,l,1):
    list1.append(int(input('enter the element')))
for j in range(0,l,1): # printing elements of list
    print(list1[j],end=',')
no=int(input('Enter the number you want to search in list'))
for t in range(0,l,1):
    if list1[t]==no:
        print('your number found and nuymber is= and at index=',list1[t],t)
        break
else:
        print('Not found')
