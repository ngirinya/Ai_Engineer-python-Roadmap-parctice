# ==========================================
# PHASE 1 - PYTHON FUNDAMENTALS
# EXERCISES 1: VARIABLES, DATA TYPES
# ==========================================


# Exercise 1
# ----------
# Create variables for:
#
# 1. Your name
# 2. Your age
# 3. Your height
# 4. Whether you are a student
#
# Then print all four values.
name = "Ezemor"
age = 25
height = 5.67
is_student = True

print(name)
print(age)
print(height)
print(True)

# Exercise 2
# ----------
# Print the type of each variable you created
# in Exercise 1.
name = "Ezemor"
age = 25
height = 5.67
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(True))


# Exercise 3
# ----------
# Create a variable called "favorite_language"
# and store your favorite programming language in it.
#
# Print:
# "My favorite programming language is Python"
#
# using the variable instead of writing "Python"
# directly inside the print statement.
favorite_language = "Python"

print("My favorite programming language is",favorite_language)


# Exercise 4
# ----------
# Ask the user to enter their age.
#
# Remember:
# input() gives you a string.
#
# Convert the user's answer into an integer.
#
# Then print:
# "Next year you will be ___ years old."

age = "26"

age = (int(age))

print("Next year you will be",age+1,"year old")


# Exercise 5
# ----------
# Ask the user to enter the price of a product.
#
# Convert the answer into a float.
#
# Then print the price and its type.
price = 95000

price = (float(price))

print(price)
print(type(price))


# Exercise 6
# ----------
# Create this variable:
#
# number = "100"
#
# Convert it into an integer.
#
# Then add 50 to it and print the result.

number = "100"

number = (int(number))

print("Number:",number+50)


# Exercise 7
# ----------
# Create:
#
# age = "25"
#
# Try to add 5 to age.
#
# Observe what happens.
#
# Then fix the problem using type conversion.

age = "25"

age = (int(age))

print("Age:",age+5)


# Exercise 8
# ----------
# AI ENGINEER EXERCISE
#
# Imagine an AI API gives you:
#
# max_tokens = "1000"
#
# Convert max_tokens into the correct type
# so that you can perform mathematics with it.
#
# Then calculate:
#
# max_tokens + 500
#
# Print the result.