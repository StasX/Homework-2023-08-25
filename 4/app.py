import random


numbers = []

# Generate 100 random numbers between 1 and 100
generate_from = 1
generate_to = 100
for _ in range(100):
    number = random.randint(generate_from, generate_to)
    numbers.append(number)

# Print all numbers separated by |
for number in numbers:
    print(number, end=" | ")
print()

# Print reversed list
print(numbers[::-1])

# Calculate the sum
total = 0
for number in numbers:
    total += number

# Print sum of all numbers
print("Sum of numbers is:", total)

# Calculate the average
average = total/len(numbers)

# Print average of all numbers
print("Average of numbers is:", average)

# Print even numbers
print("Even numbers is", end=": ")
for number in numbers:
    if number % 2 == 0:
        print(number, end=", ")
print()

# Print odd numbers
print("Odd numbers is", end=": ")
for number in numbers:
    if number % 2 != 0:
        print(number, end=", ")
print()

# Calculate count of 7 dividable numbers
seven_dividable = 0
for number in numbers:
    if number % 7 == 0:
        seven_dividable += 1
print(f"count of numbers that dividable by 7 is {seven_dividable}")

# Print max number
max_number = generate_from-1
for number in numbers:
    if max_number < number:
        max_number = number
print("Max number is:", max_number)

# Print min number
min_number = generate_from-1
for number in numbers:
    if min_number > number:
        min_number = number
print("Min number is:", min_number)

# Print numbers larger or equals to average
print("The numbers larger or equals to average is:", end=": ")
for number in numbers:
    if number >= average:
        print(number, end=" ")
