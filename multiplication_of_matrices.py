a=[[1,2,3],[3,4,5]]
b=[[1,1,1],[1,1,1]]
c=[[0,0,0],[0,0,0]]
for i in range(0,len(a),1):
    for j in range(0,len(b[0]),1):
        for k in range(0,len(b),1):
            c[i][j]+=a[i][k]*b[k][j]
for q in c:
    for l in q:
        print(l,end=' ')
    print()
    
