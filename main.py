# ==================================================
# PREPTRACK — BOILERPLATE CODE
# Complete every section marked TODO.
# ==================================================

print("=" * 50)
print("              PREPTRACK APPLICATION")
print("=" * 50)

# --------------------------------------------------
# 1. COLLECT STUDENT DETAILS
# --------------------------------------------------

# Validate that the student name is not empty.
while True:
    student_name = input("Enter student name: ").strip()
    if student_name != "":
        break
    print("Student name cannot be empty.")

registration_number = input("Enter registration number: ").strip()

while True:
    graduation_year = int(input("Enter graduation year: "))
    if 2025 <= graduation_year <= 2027:
        break
    print("Graduation year must be between 2025 and 2027.")

# Validate attendance between 0 and 100.
while True:
    attendance = float(input("Enter attendance percentage: "))
    if 0 <= attendance <= 100:
        break
    print("Invalid attendance. Enter a value between 0 and 100.")

# Accept only yes or no.
while True:
    project_input = input(
        "Has the student completed the required project? Enter yes or no: "
    ).strip().lower()
    if project_input in ("yes", "no"):
        break
    print("Invalid input. Enter only yes or no.")

# Convert project_input into True or False.
project_completed = (project_input == "yes")

# Accept only yes or no.
while True:
    profile_input = input(
        "Is the student profile verified? Enter yes or no: "
    ).strip().lower()
    if profile_input in ("yes", "no"):
        break
    print("Invalid input. Enter only yes or no.")

# Convert profile_input into True or False.
profile_verified = (profile_input == "yes")

# --------------------------------------------------
# 2. INITIALIZE COUNTERS AND VARIABLES
# --------------------------------------------------

total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 0
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0

# --------------------------------------------------
# 3. PROCESS SEVEN PRACTICE DAYS
# --------------------------------------------------

for day in range(1, 8):

    # Use a while loop to accept only -1 or a score between 0 and 100.
    while True:
        score = int(
            input(
                f"Enter Day {day} score from 0 to 100, "
                "or -1 for absent: "
            )
        )
        if score == -1 or (0 <= score <= 100):
            break
        print("Invalid score. Enter -1 or a value between 0 and 100.")

    # Handle absence: Increase absent_days and use continue.
    if score == -1:
        absent_days += 1
        continue

    # Increase attempted_days and total_score.
    attempted_days += 1
    total_score += score

    # Initialize or update highest/lowest scores and days.
    if not first_attempt_found:
        highest_score = score
        highest_score_day = day
        lowest_score = score
        lowest_score_day = day
        first_attempt_found = True
    else:
        if score > highest_score:
            highest_score = score
            highest_score_day = day
        if score < lowest_score:
            lowest_score = score
            lowest_score_day = day

    # Classify the score:
    # 75–100  -> Strong
    # 60–74   -> Satisfactory
    # 40–59   -> Needs Improvement
    # 0–39    -> Critical
    if 75 <= score <= 100:
        strong_days += 1
    elif 60 <= score <= 74:
        satisfactory_days += 1
    elif 40 <= score <= 59:
        improvement_days += 1
    else:
        critical_days += 1

    # Count passed and failed days.
    if score >= 60:
        passed_days += 1
    else:
        failed_days += 1

    # Store only the first critical day and score.
    if score < 40 and not critical_score_found:
        critical_score_found = True
        first_critical_day = day
        first_critical_score = score
