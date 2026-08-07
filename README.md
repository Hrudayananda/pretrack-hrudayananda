# PrepTrack — Placement Preparation Performance Analyzer

## Project Overview

PrepTrack is a Python console-based application that evaluates a student's placement preparation performance. It collects student details, attendance, project completion status, profile verification status, and seven days of coding practice scores. The application validates all inputs, analyzes the student's performance, calculates scores and averages, and finally determines whether the student is ready for a placement mock interview or identifies the primary blocker with the next recommended action.

---

## Features Implemented

- Student profile input
- Student name validation
- Attendance validation (0–100)
- Graduation year validation
- Project completion (Yes/No) validation
- Profile verification (Yes/No) validation
- Seven-day coding practice score processing
- Practice score validation
- Absent day handling
- Score classification (Strong, Satisfactory, Needs Improvement, Critical)
- Passed and failed day counting
- Highest and lowest score detection
- First critical score detection
- Total score calculation
- Average score calculation
- Placement readiness evaluation
- Final report generation
- Primary blocker identification
- Next action recommendation

---

## Python Concepts Used

- Variables
- Data Types (String, Integer, Float, Boolean)
- User Input (`input()`)
- Type Conversion (`int()`, `float()`)
- Arithmetic Operators
- Relational Operators
- Logical Operators
- Assignment Operators
- Boolean Expressions
- `if`, `elif`, `else`
- Nested Conditions
- `while` Loops
- `for` Loops
- `range()`
- `break`
- `continue`
- Counters
- Accumulator Variables
- f-Strings

---

## How to Run

Run the program using:

```bash
python main.py
```

If your system uses Python 3:

```bash
python3 main.py
```

---

## Test Result Summary

| Test Scenario | Status |
|--------------|--------|
| Student Name Validation | Passed |
| Attendance Validation | Passed |
| Graduation Year Validation | Passed |
| Project Input Validation | Passed |
| Profile Verification Validation | Passed |
| Practice Score Validation | Passed |
| Absent Day Handling | Passed |
| Score Classification | Passed |
| Passed & Failed Count | Passed |
| Highest & Lowest Score Detection | Passed |
| Critical Score Detection | Passed |
| Average Calculation | Passed |
| Placement Readiness Evaluation | Passed |
| Final Report Generation | Passed |

---

# Individual Contribution

**Name:** B. Hrudayananda Reddy

**Repository URL:** https://github.com/Hrudayananda/pretrack-hrudayananda

**My Main Contribution:**

Developed the complete Python console application for evaluating placement readiness by implementing input validation, score processing, performance analysis, placement eligibility checks, and final report generation.

**Features I Implemented:**

- Student profile input
- Input validation
- Attendance validation
- Graduation year validation
- Practice score processing
- Score classification
- Highest and lowest score detection
- Critical score identification
- Average calculation
- Placement readiness evaluation
- Final report generation

**Python Concepts I Used:**

- Variables
- Data Types
- User Input
- Type Conversion
- Boolean Expressions
- Arithmetic Operators
- Relational Operators
- Logical Operators
- if-elif-else
- while Loop
- for Loop
- break
- continue
- Counters
- Accumulators
- f-Strings

**Most Difficult Logic:**

Implementing the placement readiness evaluation by checking multiple eligibility conditions in the correct priority order and identifying the first major blocker.

**Problem I Faced:**

Managing the highest and lowest score calculations while correctly ignoring absent practice days and preventing division-by-zero errors.

**How I Solved It:**

I used Boolean flags to initialize the first attempted score, applied the `continue` statement to skip absent days, and checked the number of attempted days before calculating the average.

---

# Code Review Completed

**Reviewed Member:** Sreekar

**Repository URL:** https://github.com/GSreekarReddy11/preptrack-sreekar

### What Was Done Well

- The program correctly validates user inputs before processing.
- The score classification and final report are easy to understand.

### Issues Identified

1. The program does not display **"Day X Result"** (Strong, Satisfactory, Critical, etc.) immediately after each day's score, as mentioned in the project requirements.
2. The final status messages use **"Not Eligible"** instead of the required project status names like **"Critical Support Required"**, **"Practice Incomplete"**, or **"Ready for Mock Interview"**.

### Suggested Improvement

- Print the classification result for each practice day after entering the score.
- Update the final status messages to exactly match the project specification.

---

# Feedback Received

**Reviewed By:** Sreekar

**Feedback Received:**

1. Display the daily practice result after each score is entered.
2. Use the exact final status names specified in the project requirements.

**Was the Feedback Valid?**

**Yes**

---

# Improvement Made After Review

**Change Made:**

- Added daily result messages (Strong, Satisfactory, Needs Improvement, Critical, or Absent) after processing each practice score.
- Updated the final status names to match the project requirements.

**Commit Message Used:**

```bash
git commit -m "review changes"
```