# ==========================================
# PHASE 1 - PYTHON FUNDAMENTALS
# FOCUS AREA: LOOPS
# ==========================================


# ------------------------------------------
# Exercise 1 - Basic for loop
# ------------------------------------------
# Use a for loop to print:
#
# Hello
# Hello
# Hello
# Hello
# Hello
#
# Use range(5).

i = "Hello"

for i in range(5):
    print("Hello")


# ------------------------------------------
# Exercise 2 - Print numbers
# ------------------------------------------
# Use a for loop with range(5).
#
# Print:
# 0
# 1
# 2
# 3
# 4

for i in range(5):
    print(i)

# ------------------------------------------
# Exercise 3 - Start and stop
# ------------------------------------------
# Use range() to print:
#
# 2
# 3
# 4
# 5
#
# Remember: the stop number is NOT included.

for i in range(2,6):
    print(i)


# ------------------------------------------
# Exercise 4 - Step
# ------------------------------------------
# Use range() to print:
#
# 2
# 4
# 6
# 8
#
# Use a step of 2.

for i in range(2, 10, 2):
    print(i)


# ------------------------------------------
# Exercise 5 - Loop variable
# ------------------------------------------
# Use:
#
# for number in range(5):
#
# Print the value of number each time.
#
# What values does number have?

for number in range(5):
    print(number)


# ------------------------------------------
# Exercise 6 - Loop through a list
# ------------------------------------------
# Create:
#
# names = ["Paul", "John", "Mary"]
#
# Use a for loop to print each name.

names = ["paul", "John", "Mary"]

for name in names:
    print(name)


# ------------------------------------------
# Exercise 7 - Loop through scores
# ------------------------------------------
# Create:
#
# scores = [40, 55, 80, 35, 90]
#
# Use a for loop to print every score.

scores = [40, 55, 80, 35, 90]

for score in scores:
    print(score)


# ------------------------------------------
# Exercise 8 - Loop + if
# ------------------------------------------
# Create:
#
# scores = [40, 55, 80, 35, 90]
#
# Use a for loop and an if statement.
#
# Print only scores that are greater than
# or equal to 50.
#
# Expected output:
#
# 55
# 80
# 90

scores = [40, 55, 80, 35, 90]

for score in scores:
    if score >= 50:
        print(score)


# ------------------------------------------
# Exercise 9 - Print even numbers
# ------------------------------------------
# Use a for loop with range().
#
# Print:
#
# 2
# 4
# 6
# 8
# 10
#
# Hint:
# Use range() with a step.

for i in range(2, 11, 2):
    print(i)


# ------------------------------------------
# Exercise 10 - Print odd numbers
# ------------------------------------------
# Use a for loop to print:
#
# 1
# 3
# 5
# 7
# 9

for number in range(1, 10, 2):
    print(number)


# ------------------------------------------
# Exercise 11 - Counter
# ------------------------------------------
# Create:
#
# passed = 0
# scores = [40, 55, 80, 35, 90]
#
# Loop through the scores.
#
# If a score is greater than or equal to 50,
# increase passed by 1.
#
# At the end, print passed.
#
# Expected output:
#
# 3

passed = 0
scores = [40, 55, 80, 35, 90]

for score in scores:
    if score >= 50:
        passed = passed + 1
print(passed)

# ------------------------------------------
# Exercise 12 - Count even numbers
# ------------------------------------------
# Create:
#
# numbers = [2, 5, 8, 11, 14, 17]
#
# Count how many numbers are even.
#
# Expected output:
#
# 3
count = 0

numbers = [2, 5, 8, 11, 14, 17]

for number in numbers:
    if number % 2 == 0:
        count = count + 1
print(count)



# ------------------------------------------
# Exercise 13 - Sum numbers
# ------------------------------------------
# Create:
#
# numbers = [10, 20, 30, 40]
#
# Create a variable:
#
# total = 0
#
# Use a loop to add every number to total.
#
# Print total.
#
# Expected output:
#
# 100

numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total = total + number
print(total)


# ------------------------------------------
# Exercise 14 - Find numbers greater than 50
# ------------------------------------------
# Create:
#
# numbers = [20, 75, 40, 90, 30, 60]
#
# Use a loop and if statement.
#
# Print only numbers greater than 50.
#
# Expected output:
#
# 75
# 90
# 60

numbers = [20, 75, 40, 90, 30, 60]

for number in numbers:
    if number > 50:
        print(number)


# ------------------------------------------
# Exercise 15 - Count passing scores
# ------------------------------------------
# Create:
#
# scores = [45, 70, 82, 30, 90, 55]
#
# Count how many scores are greater than
# or equal to 50.
#
# Print the final count.
#
# Expected output:
#
# 4

count = 0

scores = [45, 70, 82, 30, 90, 55]

for score in scores:
    if score >= 50:
        count = count + 1
print(count)

# ------------------------------------------
# Exercise 16 - AI example
# ------------------------------------------
# Imagine these are token requests:
#
# requests = [500, 1200, 800, 1500, 700]
# max_tokens = 1000
#
# Loop through the requests.
#
# Print only the requests that are less than
# or equal to max_tokens.
#
# Expected output:
#
# 500
# 800
# 700

requests = [500, 1200, 800, 1500, 700]
max_tokens = 1000

for request in requests:
    if request <= max_tokens:
        print(request)


# ------------------------------------------
# Exercise 17 - AI counter
# ------------------------------------------
# Create:
#
# requests = [500, 1200, 800, 1500, 700]
# max_tokens = 1000
# accepted = 0
#
# Loop through the requests.
#
# If a request is less than or equal to
# max_tokens, increase accepted by 1.
#
# Print accepted.
#
# Expected output:
#
# 3

requests = [500, 1200, 800, 1500, 700]
max_tokens = 1000
accepted = 0

for request in requests:
    if request <= max_tokens:
        accepted = accepted + 1
print(accepted)

# ------------------------------------------
# Exercise 18 - Think before running
# ------------------------------------------
# Without running the code, predict the output:
#
# for i in range(3):
#     print(i)
#
# What will it print?

# Expected output
# 0
# 1
# 2


# ------------------------------------------
# Exercise 19 - Think before running
# ------------------------------------------
# Without running the code, predict the output:
#
# for i in range(2, 6):
#     print(i)
#
# What will it print?

# Expected Output
# 2
# 3
# 4
# 5


# ------------------------------------------
# Exercise 20 - Challenge
# ------------------------------------------
# Create:
#
# scores = [35, 60, 75, 42, 90, 55]
#
# Your program should:
#
# 1. Loop through the scores.
# 2. Print every passing score.
# 3. Count how many students passed.
# 4. Print the final number of students who passed.
#
# Expected passing scores:
#
# 60
# 75
# 90
# 55
#
# Expected final count:
#
# 4

scores = [35, 60, 75, 42, 90, 55]

passed = 0

for score in scores:
    if score >= 50:
        print(score)
        passed = passed + 1
print(passed)        