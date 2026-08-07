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
