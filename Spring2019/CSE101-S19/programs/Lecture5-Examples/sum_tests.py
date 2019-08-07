def sum(nums):
    total = 0
    for num in nums:
        total += num
    return total

def main():
    scores = [3, 5, 1]
    print('Sum of scores[]: ' + str(sum(scores)))

main()

# if __name__  == '__main__’:
# I did not use this line above in this example.
# Debugger did not like that.
