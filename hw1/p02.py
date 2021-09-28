import math

score_by_grading = {
    "A+": 4.3,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "F": 0,
    "X": 0,
}

total_score = 0
total_credit = 0

for i in range(3):
    grading = input()
    credit = int(input())
    total_credit += credit
    total_score += score_by_grading[grading] * credit

avg_score = math.floor((total_score / total_credit + 1e-10)*100)/100

print(f"{avg_score:.2f}")
