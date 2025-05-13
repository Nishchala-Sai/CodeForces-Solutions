l=list(map(int,input().split()))
k=l[0]
n=l[1]
w=l[2]
total=0
for i in range(1,w+1):
    total+=i*k
if(total>n):
    print(total-n)
else:
    print("0")