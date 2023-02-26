words = input("Enter comma-separated sequence of words: ")

# Split the input into a list of words
word_list = [word.strip() for word in words.split(",")]

# Sort the list alphabetically
sorted_words = sorted(word_list)

# Print the sorted words
print(",".join(sorted_words))




