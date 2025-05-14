l1=list(map(int,input().split()))
n=l1[0]
h=l1[1]
width=0
l2=list(map(int,input().split()))
for i in range(n):
    if l2[i]>h:
        width+=2
    else:
        width+=1
print(width)
