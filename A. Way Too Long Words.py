n=int(input())

if n>=1 and n<=100:
    for i in range(n):
        input_string= input()
        if len(input_string)>10:
            first_letter, last_letter, final_string="","",""
            first_letter+=input_string[:1]
            last_letter+=input_string[-1]
            final_string += first_letter + str(len(input_string)-2)+ last_letter
            print(final_string)
        else:
            print(input_string)

