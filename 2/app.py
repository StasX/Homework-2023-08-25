# Init  variables
names = []

# Inform the user to enter 5 names
print("Please enter 5 names")

# Get from user 5 names
for i in range(1, 6):
    name = input(f"name #{i}: ")
    names.append(name)

# Print first na and last names from the list
print(names[0], names[-1])

# Print names with their's length
for name in names:
    print(f"The length of name {name} is {len(name)} characters.")

# Print names with their's length but in reverse
for name in names[::-1]:
    print(f"The length of name {name} is {len(name)} characters.")
