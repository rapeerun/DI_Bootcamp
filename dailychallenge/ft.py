#  challenge 1
code_name=[1,2,3,4,5,6,7,8,9]
size=len(code_name)
print(code_name)
print(size)


num = int(input("Enter a number") )
if num in code_name:
    print (num)
else:
    print("reject")

# challenge 2
# remove consecutive duplicates from string
def remove_consec_duplicates(a):
    new_a = ""
    prev = ""
    for c in a:
        if len(new_a) == 0:
            new_a += c
            prev = c
        if c == prev:
            continue
        else:
            new_a += c
            prev = c
    return new_a
a=input('Enter a word')
print(a)
# remove consecutive duplicates
a = remove_consec_duplicates(a)
print(a)





    
