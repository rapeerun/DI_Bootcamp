text = input("Please enter a string (10 characters long): ")

if len(text) < 10:
    print("String not long enough.")
elif len(text) > 10:
    print("String too long.")
else:
    print("First character:", text[0])
    print("Last character:", text[-1])
    print("Printing the string character by character:")
    for char in text:
        print(char)