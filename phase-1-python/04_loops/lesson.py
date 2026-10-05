# ==========================================
# PHASE 1 - PYTHON FUNDAMENTALS
# FOCUS AREA 4 - LOOPS
# ==========================================


# ------------------------------------------
# 1. BASIC FOR LOOP
# ------------------------------------------

for i in range(5):
    print(i)


# ------------------------------------------
# 2. range()
# ------------------------------------------

# range(5) gives:
# 0, 1, 2, 3, 4

for number in range(5):
    print(number)


# ------------------------------------------
# 3. range(start, stop)
# ------------------------------------------

# Starts at 2
# Stops before 6

for number in range(2, 6):
    print(number)


# ------------------------------------------
# 4. range(start, stop, step)
# ------------------------------------------

# Start at 2
# Stop before 10
# Move by 2

for number in range(2, 10, 2):
    print(number)


# ------------------------------------------
# 5. LOOPING THROUGH A LIST
# ------------------------------------------

names = ["Paul", "John", "Mary"]

for name in names:
    print(name)


# ------------------------------------------
# 6. LOOP + IF
# ------------------------------------------

scores = [40, 55, 80, 35, 90]

for score in scores:
    if score >= 50:
        print(score)


# ------------------------------------------
# 7. COUNTING WITH A LOOP
# ------------------------------------------

passed = 0

for score in scores:
    if score >= 50:
        passed = passed + 1

print("Passed:", passed)


# ------------------------------------------
# 8. SUMMING WITH A LOOP
# ------------------------------------------

numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total = total + number

print("Total:", total)