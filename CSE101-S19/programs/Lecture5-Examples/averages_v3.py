# Given a list of exam scores for a group of students,
# this function returns a list of average exam scores.

scores = [[89, 85, 90], [78, 85, 72], [99, 86, 92], [82, 84, 79]]

def compute_averages(students):
    num_students = len(students)
    num_exams = len(students[0])  # each student took the same number of exams
    avgs = [0] * num_exams

    for student in students:
        for i in range(num_exams):  # nested loops
            avgs[i] += student[i]

    for i in range(num_exams):
        avgs[i] /= num_students

    return avgs

averages = compute_averages(scores)
print(averages)
