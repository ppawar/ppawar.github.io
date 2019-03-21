# Given a list of exam scores for a group of students,
# this code computes the average score on each exam.

scores = [[89, 85, 90], [78, 85, 72], [99, 86, 92], [82, 84, 79]]

num_students = len(scores)
num_exams = len(scores[0])  # each student took the same number of exams
averages = [0] * num_exams

for student in scores:
    for i in range(num_exams):  # nested loops
        averages[i] += student[i]

for i in range(num_exams):
    averages[i] /= num_students

print(averages)
