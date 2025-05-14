n=int(input())
s=input()
anton_wins=0
danik_wins=0
for i in range(n):
    if s[i]=="A":
        anton_wins+=1
    else:
        danik_wins+=1
if(anton_wins>danik_wins):
    print("Anton")
elif(danik_wins>anton_wins):
    print("Danik")
else:
    print("Friendship")
