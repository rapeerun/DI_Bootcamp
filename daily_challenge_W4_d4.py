matrix = [
    '7iTshi$#',
    'Ts Mta^r!'
]

# Initialize empty string
secret_message = ""

# Loop through each column
for i in range(len(matrix[0])):
    # Initialize a string for the current column
    current_column = ""

    # Loop through current column
    for j in range(len(matrix)):
        # Add the current character to the current column
        current_column += matrix[j][i]

    # Loop through the characters in the current column
    for c in current_column:
        
        if c.isalpha():
            secret_message += c

        
        else:
            secret_message += " "

# Print the secret message
print(secret_message)
