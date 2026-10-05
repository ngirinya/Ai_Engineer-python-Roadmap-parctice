# ==========================================
# FOCUS AREA 3 - EXERCISES
# COMPARISONS & BOOLEAN LOGIC
# ==========================================


# Exercise 1
# Create two variables:
# a = 15
# b = 10
#
# Print the result of:
# a > b
# a < b
# a == b
# a != b

a = 15
b = 10

print(a > b)
print(a < b)
print(a == b)
print(a != b)


# Exercise 2
# Create:
# age = 20
#
# Check if age is greater than or equal to 18.
# Print the result.

age = 20

print(age >= 18)


# Exercise 3
# Create:
# password = "python123"
#
# Check if password is equal to "python123".
# Print the result.

password = "python123"

print(password == "python123")


# Exercise 4
# Create:
# age = 25
# has_id = True
#
# A person can enter only if:
# - they are 18 or older
# - AND they have an ID
#
# Use "and" to check this.
# Print the result.

age = 25
has_id = True

print(age >= 18 and has_id )


# Exercise 5
# Create:
# is_weekend = False
# is_holiday = True
#
# A person can relax if it is the weekend
# OR it is a holiday.
#
# Use "or" to check this.
# Print the result.

is_weekend = False
is_holiday = True

print(is_weekend or is_holiday)


# Exercise 6
# Create:
# is_logged_in = True
#
# Use "not" to print the opposite value.

is_logged_in = True

print(not is_logged_in)


# Exercise 7
# Create:
# score = 75
#
# Check if the score is:
# greater than or equal to 50
#
# Print the result.

score = 75

print(score >= 50)


# Exercise 8
# AI example:
#
# max_tokens = 1000
# requested_tokens = 1200
#
# Check whether requested_tokens is less than
# or equal to max_tokens.
#
# Print the result.

max_tokens = 1000
requested_tokens = 1200

print(requested_tokens <= max_tokens)


# ------------------------------------------
# Exercise 9 - Basic if statement
# ------------------------------------------
# Create a variable:
# age = 20
#
# Write an if statement that prints:
# "Adult"
#
# only when age is greater than or equal to 18.
age = 20
if age >= 18:
    print("Adult")


# ------------------------------------------
# Exercise 10 - Condition is False
# ------------------------------------------
# Create:
# age = 15
#
# Write an if statement that prints:
# "Adult"
#
# What happens when you run the code?
age = 15

if age == 15:
    print("Adult")



# ------------------------------------------
# Exercise 11 - Number comparison
# ------------------------------------------
# Create:
# score = 75
#
# If the score is greater than or equal to 50,
# print:
# "Pass"

score = 75

if score >= 50:
    print("Pass")


# ------------------------------------------
# Exercise 12 - Password
# ------------------------------------------
# Create:
# password = "python123"
#
# If the password is equal to "python123",
# print:
# "Access granted"

password = "python123"

if password == "python123":
    print("Access granted")
else:
    print("wronge password")

password = "python123"

if password == "python133":
    print("Access Granted")
else:
    print("wronge Password")

# ------------------------------------------
# Exercise 13 - Using !=
# ------------------------------------------
# Create:
# username = "Paul"
#
# If the username is NOT equal to "Admin",
# print:
# "Regular user"

username = "Paul"

if  username != "Admin":
    print("Regular User")


# ------------------------------------------
# Exercise 14 - Using Boolean
# ------------------------------------------
# Create:
# is_logged_in = True
#
# If is_logged_in is True,
# print:
# "Welcome back"

is_logged_in = True

if is_logged_in == True:
    print("Welcome Back")


# ------------------------------------------
# Exercise 15 - Using AND
# ------------------------------------------
# Create:
# age = 20
# has_id = True
#
# A person can enter if:
# - age is 18 or older
# - AND they have an ID
#
# If both conditions are true,
# print:
# "You can enter"

age = 20
has_id = True

if age >= 18 and has_id:
    print("You Can Enter")


# ------------------------------------------
# Exercise 16 - AI example
# ------------------------------------------
# Create:
# max_tokens = 1000
# requested_tokens = 800
#
# If requested_tokens is less than or equal
# to max_tokens, print:
# "Request accepted"

max_tokens = 1000
requested_tokens = 800

if requested_tokens <= max_tokens:
    print("Request Accepted")


# ------------------------------------------
# Exercise 17 - Think before running
# ------------------------------------------
# Without running the code, predict the output.
#
# age = 25
#
# if age >= 18:
#     print("Adult")
#
# What will Python print?

age = 25

if age >= 18:
    print("Adult")



# ------------------------------------------
# Exercise 18 - Think before running
# ------------------------------------------
# Without running the code, predict the output.
#
# score = 40
#
# if score >= 50:
#     print("Pass")
#
# Will "Pass" be printed?
# Explain why.

## No because the condition say if score is greater or equal to 50 which score is less than 50

## 40 >= 50



# ------------------------------------------
# Exercise 19 - Find the mistake
# ------------------------------------------
# What is wrong with this code?
#
# age = 20
#
# if age >= 18:
# print("Adult")
#
# Rewrite it correctly.

age = 20

if age >= 18:
    print("Adult")


# ------------------------------------------
# Exercise 20 - Challenge
# ------------------------------------------
# Create:
# age = 22
# has_ticket = True
#
# A person can enter an event only when:
# - they are 18 or older
# - AND they have a ticket
#
# Write an if statement that prints:
# "Entry allowed"
#
# when both conditions are true.

age = 22
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry Allowed")


# ==========================================
# FOCUS AREA 3 - EXERCISES
# IF, ELIF, ELSE
# ==========================================


# ------------------------------------------
# Exercise 21 - if and else
# ------------------------------------------
# Create:
# age = 15
#
# If age is 18 or older, print:
# "Adult"
#
# Otherwise, print:
# "Minor"

age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")

# ------------------------------------------
# Exercise 22 - Pass or Fail
# ------------------------------------------
# Create:
# score = 45
#
# If score is greater than or equal to 50,
# print:
# "Pass"
#
# Otherwise, print:
# "Fail"

score = 45

if score >= 50:
    print("Pass")
else:
    print("Fail")

# ------------------------------------------
# Exercise 23 - if, elif, else
# ------------------------------------------
# Create:
# score = 75
#
# Use:
# if
# elif
# else
#
# Rules:
# 80 or above  -> "Excellent"
# 50 to 79     -> "Pass"
# Below 50     -> "Fail"

score = 75

if score >= 80:
    print("Excellent")
elif score >= 50:
        print("Pass")
else:
    print("Fail")

# ------------------------------------------
# Exercise 24 - Test different scores
# ------------------------------------------
# Use the same rules from Exercise 23.
#
# Test these scores one at a time:
#
# score = 85
# score = 60
# score = 30
#
# Predict the output before running each one.

score = 75

if score >= 85:
    print("Excellent")
elif score >= 60:
    print("Pass")
else :
    print("Fail")
# ------------------------------------------
# Exercise 25 - Order matters
# ------------------------------------------
# Look at this code:
#
# score = 85
#
# if score >= 50:
#     print("Pass")
# elif score >= 80:
#     print("Excellent")
#
# Without running it:
#
# 1. What will it print?
# 2. Why doesn't it print "Excellent"?

score = 85

if score >= 50:
     print("Pass")
elif score >= 80:
    print("Excellent")


# ------------------------------------------
# Exercise 26 - Fix the order
# ------------------------------------------
# Rewrite Exercise 25 so that:
#
# 80 or above -> "Excellent"
# 50 or above -> "Pass"
# Below 50    -> "Fail"
#
# Test it with:
# score = 85

score = 85

if score >= 80:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Fail")

    
# ------------------------------------------
# Exercise 27 - Age categories
# ------------------------------------------
# Create:
# age = 16
#
# Use if, elif and else:
#
# 18 or older -> "Adult"
# 13 to 17    -> "Teenager"
# Below 13    -> "Child"

age = 16

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# ------------------------------------------
# Exercise 28 - Password
# ------------------------------------------
# Create:
# password = "python123"
#
# If the password is correct:
# print("Access granted")
#
# Otherwise:
# print("Access denied")

password = "python123"

if password == "python123":
    print("Access Granded")
else:
    print("Access Denied")
# ------------------------------------------
# Exercise 29 - AND with if/else
# ------------------------------------------
# Create:
# age = 20
# has_id = True
#
# A person can enter only if:
# - age is 18 or older
# - AND they have an ID
#
# If both are true:
# print("Access granted")
#
# Otherwise:
# print("Access denied")

age = 20
has_id = True

if age  >= 35 and has_id:
    print("Access Granted")
else:
    print("Access Denied")

# ------------------------------------------
# Exercise 30 - OR with if/else
# ------------------------------------------
# Create:
# is_weekend = False
# is_holiday = True
#
# A person can relax if:
# - it is the weekend
# - OR it is a holiday
#
# If either condition is true:
# print("You can relax")
#
# Otherwise:
# print("You have work")

is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("You Can Relax")
else:
    print("You Have Work")

# ------------------------------------------
# Exercise 31 - AI example
# ------------------------------------------
# Create:
# max_tokens = 1000
# requested_tokens = 1200
#
# If requested_tokens is less than or equal
# to max_tokens:
#     print("Request accepted")
#
# Otherwise:
#     print("Request too large")

max_tokens = 1000
requested_tokens = 1200

if requested_tokens <= max_tokens:
    print("Request Accepted")
else:
    print("Request Too Large")

# ------------------------------------------
# Exercise 32 - Challenge
# ------------------------------------------
# Create:
# score = 92
#
# Classify the score:
#
# 90 or above -> "A"
# 80 to 89    -> "B"
# 70 to 79    -> "C"
# 50 to 69    -> "D"
# Below 50    -> "F"
#
# Use if, elif and else.
#
# Test your code with:
# 92
# 85
# 73
# 55
# 40   

score = 92

if score >= 90:
    print("A")
elif  score >= 80:
        print("B")    
elif  score >= 70:
        print("C")
elif  score >= 60:
        print("D")
elif  score >= 50:
        print("D")
else:
    print("F")                                