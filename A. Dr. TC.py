t=int(input())
for i in range(t):
    n=int(input())
    s=(input())
    l=[]
    count_1=0
   
    for j in range(n):
        ss=s[:]
        if(ss[j]=="1"):
            l.append(s[:j]+"0"+s[j+1:])
        else:
            l.append(s[:j]+"1"+s[j+1:])
        
    
    for k in l:
        if "1" in k:
            count_1+=k.count("1")
    print(count_1)


            







       
            
        
    
