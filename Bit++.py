n=int(input())
sum=0
if n>=1 and n<=150:
    for i in range(n):
        inpt=input()
        if inpt== "++X":
            sum+=1
        elif inpt=="X++":
            sum+=1
        elif inpt=="--X":
            sum-=1
        elif inpt=="X--":
            sum-=1
    print(sum)
