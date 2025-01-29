# Definite Loop

# Variables
numbers_entered = []

# Hard Coded Name
first_name = "Joseph"
last_name = "Simonin"

# Determine length of full name
total_name_length = len(first_name) + len(last_name)

# Hello Message
print(f"Hello {first_name} {last_name}") # f enables the use of variables through {} inside strings
print(f"Please enter {total_name_length} numbers.")

# User input Loop
for i in range(total_name_length):
    numbers = float(input("Please enter a number: ")) # Convert string to float
    numbers_entered.append(numbers)

# Find number of numbers entered, sum of numbers, average of numbers, largest number, and smallest number entered
number_count = len(numbers_entered)
number_sum = sum(numbers_entered)
number_average = number_sum / number_count
largest_number = max(numbers_entered)
smallest_number = min(numbers_entered)

# Display output
print(f"Number of numbers entered: {number_count}")
print(f"Total of the numbers: {number_sum}")
print(f"Average of the numbers: {number_average}")
print(f"Largest number entered was: {largest_number}")
print(f"Smallest number entered was: {smallest_number}")


