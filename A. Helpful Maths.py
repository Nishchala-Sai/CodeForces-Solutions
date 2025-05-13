s=input()
numbers=s.split("+")
counter=0
numbers.sort()
for number in numbers :
    counter+=1
     
    if len(numbers)>1:
        if counter<len(numbers):
           print(f"{number}+",end="")
        else:
            print(number)
    else:
        print(number)

