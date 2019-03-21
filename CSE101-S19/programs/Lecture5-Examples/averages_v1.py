# Given a fixed number of students (4) and exam scores (3),
# this code computes the average score on each exam.

scores = [[89, 85, 90], [78, 85, 72], [99, 86, 92], [82, 84, 79]]

averages = [0, 0, 0]

for student in scores:
    averages[0] += student[0]
    averages[1] += student[1]
    averages[2] += student[2]
    
for i in range(3):
    averages[i] /= 4

print(averages)
