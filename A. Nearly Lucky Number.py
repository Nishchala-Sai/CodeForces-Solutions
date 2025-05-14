n=int(input())
a=n
lucky_digit=0
while n!=0:
    if n%10==4 or n%10==7:
        lucky_digit+=1
        n=n//10
    else:
        n//=10
if lucky_digit==4 or lucky_digit==7:
    print("YES")
else:
    print("NO")

