x=int(input())
steps=0
while x>0:
    while x>=5:
        steps+=1
        x=x-5
    if x==4:
        steps+=1
        x=x-4
    elif x==3:

        steps+=1
        x-=3
    elif x==2:
        steps+=1
        x-=2
    elif x==1:
        steps+=1
        x-=1
print(steps)