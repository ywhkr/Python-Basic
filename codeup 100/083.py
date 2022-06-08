r,g,b = map(int,input().split())

for i in range(r):
    for j in range(g):
        for m in range(b):
            print(i,j,m,end = "\n")
            
print(r*g*b)