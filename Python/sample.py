# 1. Store a short paragraph about a Python course using multiline string
description = """
  This Python course is designed for beginners.
  It covers programming basics, data types, and more.
  Python makes learning to code easy and fun!
"""

# 2. Print the length of the paragraph
print("Paragraph length:", len(description))

# 3. Print the first and last characters
print("First character:", description[0])
print("Last character:", description[-1])

# 4. Slice and print the first 50 characters
print("Preview (first 50 characters):", description[:50])

# 5. Replace all occurrences of "Python" with "PYTHON"
updated_description = description.replace("Python", "PYTHON")
print("Updated Description:\n", updated_description)

# 6. Convert to lowercase
lowercase_description = description.lower()
print("Lowercase Description:\n", lowercase_description)

# 7. Remove leading/trailing whitespaces
cleaned_description = description.strip()
print("Cleaned Description:\n", cleaned_description)

# 8. Split the paragraph into words
word_list = description.split()
print("List of words:", word_list)

# 9. Check if "course" is in the paragraph
if "course" in description:
    print("The word 'course' is found in the paragraph.")
else:
    print("The word 'course' is not found in the paragraph.")


word_count = len(word_list)
char_count = len(description.replace(" ", "").replace("\n", ""))
final_msg = "The course description is {} characters long and has {} words.".format(char_count, word_count)
print(final_msg)

