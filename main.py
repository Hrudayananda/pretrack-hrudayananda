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

# --------------------------------------------------
# 4. CALCULATE AVERAGE SCORE
# --------------------------------------------------

if attempted_days > 0:
    average_score = total_score / attempted_days
else:
    average_score = 0.0

# --------------------------------------------------
# 5. CREATE ELIGIBILITY CONDITIONS
# --------------------------------------------------

graduation_eligible = (2025 <= graduation_year <= 2027)
attendance_eligible = (attendance >= 75)
practice_count_eligible = (attempted_days >= 6)
average_eligible = (average_score >= 70)
critical_score_clear = not critical_score_found
passed_days_eligible = (passed_days >= 4)

placement_ready = (
    graduation_eligible
    and attendance_eligible
    and practice_count_eligible
    and average_eligible
    and critical_score_clear
    and passed_days_eligible
    and project_completed
    and profile_verified
)

# --------------------------------------------------
# 6. DETERMINE FINAL STATUS
# --------------------------------------------------

# Check conditions in this priority:
# 1. No practice attempted
# 2. Critical score found
# 3. Fewer than six attempts
# 4. Fewer than four passed days
# 5. Average below 70
# 6. Attendance below 75
# 7. Graduation year not eligible
# 8. Project incomplete
# 9. Profile not verified
# 10. Ready for Mock Interview

if attempted_days == 0:
    final_status = "Not Eligible"
    primary_blocker = "No practice days attempted"
    next_action = "Attempt at least 6 practice days"
elif critical_score_found:
    final_status = "Not Eligible"
    primary_blocker = f"Critical score found on Day {first_critical_day} (Score: {first_critical_score})"
    next_action = "Complete remedial practice for critical score"
elif attempted_days < 6:
    final_status = "Not Eligible"
    primary_blocker = f"Fewer than 6 practice attempts ({attempted_days}/7 attempted)"
    next_action = "Attempt more practice days to reach minimum 6 attempts"
elif passed_days < 4:
    final_status = "Not Eligible"
    primary_blocker = f"Fewer than 4 passed days ({passed_days} passed)"
    next_action = "Improve score on failed practice days to pass at least 4 days"
elif average_score < 70:
    final_status = "Not Eligible"
    primary_blocker = f"Average score below 70 ({average_score:.2f})"
    next_action = "Raise overall practice average score to 70 or higher"
elif attendance < 75:
    final_status = "Not Eligible"
    primary_blocker = f"Attendance below 75% ({attendance}%)"
    next_action = "Improve attendance percentage to at least 75%"
elif not graduation_eligible:
    final_status = "Not Eligible"
    primary_blocker = f"Graduation year ({graduation_year}) outside eligible range (2025-2027)"
    next_action = "Verify graduation year with administration"
elif not project_completed:
    final_status = "Not Eligible"
    primary_blocker = "Required project not completed"
    next_action = "Complete and submit the required project"
elif not profile_verified:
    final_status = "Not Eligible"
    primary_blocker = "Student profile not verified"
    next_action = "Complete student profile verification"
else:
    final_status = "Ready for Mock Interview"
    primary_blocker = "None"
    next_action = "Proceed to Mock Interview"

# --------------------------------------------------
# 7. DISPLAY FINAL REPORT
# --------------------------------------------------

print()
print("=" * 50)
print("              PREPTRACK REPORT")
print("=" * 50)

print("\nSTUDENT PROFILE\n")
print(f"Student Name             : {student_name}")
print(f"Registration Number      : {registration_number}")
print(f"Graduation Year          : {graduation_year}")
print(f"Attendance               : {attendance:.0f}%" if attendance.is_integer() else f"Attendance               : {attendance}%")
print(f"Project Completed        : {'Yes' if project_completed else 'No'}")
print(f"Profile Verified         : {'Yes' if profile_verified else 'No'}")

print("\nPRACTICE SUMMARY\n")
print(f"Total Practice Days      : 7")
print(f"Attempted Days           : {attempted_days}")
print(f"Absent Days              : {absent_days}")
print(f"Passed Days              : {passed_days}")
print(f"Failed Days              : {failed_days}")
print()
print(f"Strong Days              : {strong_days}")
print(f"Satisfactory Days        : {satisfactory_days}")
print(f"Needs Improvement Days   : {improvement_days}")
print(f"Critical Days            : {critical_days}")

print("\nPERFORMANCE ANALYSIS\n")
if attempted_days > 0:
    print(f"Total Score              : {total_score}")
    print(f"Average Score            : {average_score:.2f}")
    print(f"Highest Score            : {highest_score}")
    print(f"Highest Score Day        : Day {highest_score_day}")
    print(f"Lowest Score             : {lowest_score}")
    print(f"Lowest Score Day         : Day {lowest_score_day}")
else:
    print("Total Score              : Not Available")
    print("Average Score            : Not Available")
    print("Highest Score            : Not Available")
    print("Highest Score Day        : Not Available")
    print("Lowest Score             : Not Available")
    print("Lowest Score Day         : Not Available")

print("\nCRITICAL SCORE INFORMATION\n")
print(f"Critical Score Found     : {'Yes' if critical_score_found else 'No'}")
if critical_score_found:
    print(f"First Critical Day       : Day {first_critical_day}")
    print(f"First Critical Score     : {first_critical_score}")
else:
    print("First Critical Day       : Not Applicable")
    print("First Critical Score     : Not Applicable")

print("\nFINAL DECISION\n")
print(f"Final Status             : {final_status}")
print(f"Primary Blocker          : {primary_blocker}")
print(f"Next Action              : {next_action}")

print("=" * 50)
