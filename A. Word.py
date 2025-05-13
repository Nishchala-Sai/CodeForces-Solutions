s=input()
count_upper=0
count_lower=0
for ch in s:
    if ch.isalpha():
        if ch.isupper():
            count_upper+=1
        else:
            count_lower+=1
if count_lower>count_upper:
    print(s.lower())
elif count_lower<count_upper:
    print(s.upper())
else:
    print(s.lower())

            
