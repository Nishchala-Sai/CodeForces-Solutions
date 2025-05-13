l=list(map(int,input().split()))
a=l[0]
b=l[1]
years=0
while True:
    if a<=b:
        years+=1
        a=a*3
        b=b*2
    else:
        print(years)
        break
