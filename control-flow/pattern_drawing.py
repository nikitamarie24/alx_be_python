# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop to handle rows
while row < size:
    # For loop to handle columns
    for col in range(size):
        print("*", end="")  # print * without moving to a new line
    print()  # move to the next line after finishing a row
    row += 1
