# ==========================================
# PHASE 1 - PYTHON FUNDAMENTALS
# LESSON 1: VARIABLES, DATA TYPES & CONVERSION
# ==========================================


# ------------------------------------------
# 1. VARIABLES
# ------------------------------------------

name = "Paul"
age = 21

print(name)
print(age)


# ------------------------------------------
# 2. DIFFERENT DATA TYPES
# ------------------------------------------

name = "Paul"          # str - text
age = 21               # int - whole number
height = 1.75          # float - decimal number
is_student = True      # bool - True or False

print(name)
print(age)
print(height)
print(is_student)


# ------------------------------------------
# 3. CHECKING THE TYPE OF A VALUE
# ------------------------------------------

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# ------------------------------------------
# 4. STRINGS
# ------------------------------------------

first_name = "Paul"
language = "Python"

print(first_name)
print(language)

print("My name is", first_name)
print("I am learning", language)


# ------------------------------------------
# 5. INTEGER AND FLOAT
# ------------------------------------------

age = 21
height = 1.75

print("Age:", age)
print("Height:", height)


# ------------------------------------------
# 6. BOOLEAN
# ------------------------------------------

is_learning = True
has_finished = False

print("Learning:", is_learning)
print("Finished:", has_finished)


# ------------------------------------------
# 7. INPUT
# ------------------------------------------

name = input("Enter your name: ")

print("Hello", name)


# ------------------------------------------
# 8. INPUT ALWAYS RETURNS A STRING
# ------------------------------------------

age = input("Enter your age: ")

print("Your age is:", age)
print("Type before conversion:", type(age))


# ------------------------------------------
# 9. STRING TO INTEGER
# ------------------------------------------

age = int(age)

print("Type after conversion:", type(age))
print("Next year you will be:", age + 1)


# ------------------------------------------
# 10. STRING TO FLOAT
# ------------------------------------------

price = "25.50"

price = float(price)

print("Price:", price)
print("Type:", type(price))


# ------------------------------------------
# 11. NUMBER TO STRING
# ------------------------------------------

score = 100

score = str(score)

print("Score:", score)
print("Type:", type(score))


# ------------------------------------------
# 12. A SMALL AI-ENGINEERING EXAMPLE
# ------------------------------------------

max_tokens = "500"

print("Before conversion:", type(max_tokens))

max_tokens = int(max_tokens)

print("After conversion:", type(max_tokens))

print("Maximum tokens:", max_tokens)