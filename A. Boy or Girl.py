s=input()
characters=[]
for ch in s:
    if ch in characters:
        pass
    else:
        characters.append(ch)
if len(characters)%2==0:
    print("CHAT WITH HER!")
else:
    print('IGNORE HIM!')

