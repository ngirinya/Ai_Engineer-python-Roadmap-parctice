# ==========================================
# PHASE 1 - PYTHON FUNDAMENTALS
# FOCUS AREA 3: COMPARISONS & BOOLEAN LOGIC
# ==========================================

# ------------------------------------------
# 1. COMPARISON OPERATORS
# ------------------------------------------

a = 10
b = 5

print(a > b)    # Greater than
print(a < b)    # Less than
print(a >= b)   # Greater than or equal to
print(a <= b)   # Less than or equal to
print(a == b)   # Equal to
print(a != b)   # Not equal to


# ------------------------------------------
# 2. COMPARING NUMBERS
# ------------------------------------------

age = 20

print(age > 18)
print(age == 20)
print(age < 18)


# ------------------------------------------
# 3. COMPARING STRINGS
# ------------------------------------------

name = "Paul"

print(name == "Paul")
print(name == "John")


# ------------------------------------------
# 4. BOOLEAN VALUES
# ------------------------------------------

is_student = True
has_finished = False

print(is_student)
print(has_finished)


# ------------------------------------------
# 5. AND
# ------------------------------------------

age = 20
has_id = True

print(age >= 18 and has_id)


# ------------------------------------------
# 6. OR
# ------------------------------------------

is_weekend = False
is_holiday = True

print(is_weekend or is_holiday)


# ------------------------------------------
# 7. NOT
# ------------------------------------------

is_logged_in = True

print(not is_logged_in)


# ------------------------------------------
# 8. COMBINING COMPARISONS
# ------------------------------------------

age = 25
has_ticket = True

can_enter = age >= 18 and has_ticket

print(can_enter)


# ------------------------------------------
# 9. BOOLEAN IN AN IF STATEMENT
# ------------------------------------------

age = 20

if age >= 18:
    print("You are an adult")


# ------------------------------------------
# 10. AI-RELATED EXAMPLE
# ------------------------------------------

max_tokens = 1000
requested_tokens = 500

if requested_tokens <= max_tokens:
    print("Request accepted")
else:
    print("Request is too large")