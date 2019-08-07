scores = [[89, 85, 90], [78, 85, 72], [99, 86, 92], [82, 84, 79]]

averages = [0,0,0]
sum = [0,0,0]

for studentlist in scores:
    sum[0] += studentlist[0]
    sum[1] += studentlist[1]
    sum[2] += studentlist[2]

print(sum)
averages[0] = sum[0] / 3
averages[1] = sum[1] / 3
averages[2] = sum[2] / 3
print(averages)

