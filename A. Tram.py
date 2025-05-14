n=int(input())
capacity_list=[]

count=0
for i in range(n):
    a_b_list=list(map(int, input().split()))
    b=a_b_list[0]
    a=a_b_list[1]
    count=count-b+a
    capacity_list.append(count)
print(max(capacity_list))
