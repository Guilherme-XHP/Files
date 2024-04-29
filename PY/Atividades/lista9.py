# Read the first term and the common difference
first_term = int(input("Enter the first term: "))
common_difference = int(input("Enter the common difference: "))

# Print the first 10 terms of the arithmetic progression
for i in range(10):
    term = first_term + i * common_difference
    print(term)