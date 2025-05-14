s=input()
t=input()
if len(s)>1 and s[::-1]==t:
    print("YES")
elif len(s)==1 and s==t:
    print("YES")
else:
    print("NO")