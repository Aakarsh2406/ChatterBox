list2=[]
list1=list(map(int,input().split(' ')))
l=len(list1)
d=0
for i in range(l-1):
	d=list1[i]-list1[i+1]
	list2.append(abs(d))
list2.sort()
a=min(list2)
print(a)



		
