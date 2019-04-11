a=[[1,2,3],[4,5,6],[6,7,8]]
b=[[1,2,3],[3,4,5],[6,7,8]]
c=[[0,0,0],[0,0,0],[0,0,0]]
for j in range(0,len(a),1):
    for q in range(0,len(a),1):
        c[j][q]=a[j][q]+b[j][q]
for i in c:
    for z in i:
        print(z,end=' ')
    print()

        
        
    
