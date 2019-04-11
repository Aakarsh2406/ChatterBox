a=open('test.txt','r')
if not a.closed:
    print('file openend',a.name)
    data=a.read()
    print(data)
    a.close()
    if a.closed:
        print('closed')
else:
    print('file not opened')
    

