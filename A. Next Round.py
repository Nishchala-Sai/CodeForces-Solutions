l1=list(map(int, input().split()))
n,k=l1[0],l1[1]
qualified=0
if n>=k and n>=1 and n<=150 and k>=1 and k<=150:
    l=list(map(int,input().split()))
    for i in l:
        if i>= l[k-1] and i>0:
            qualified+=1
    print(qualified)