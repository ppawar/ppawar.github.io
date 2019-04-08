# CSE 101
# Lab #4
# your name:
# your email:

# 2. Interleave: Fix Error(s)
#
def interleave(nums):
    new_nums = []
    index = 0
    if len(nums) == 0:
        return new_nums
    for j in range(len(nums)):
        for i in range(len(nums[0])):
            new_nums.append(nums[j][index])
            index += 1
    return new_nums


# 3. Weighted GPA Calculator
def gpa_calculator(grades, credit_worth):
    return None # Replace this line with your implementation

# This shows some tests for the functions defied above.  You may add more
# tests to the code below.
def main():
    print("Testing Interleave:")
    print("Testing interleave() for nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]: " + str(interleave([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))  # 3 lists with 3 elements each
    print("Testing interleave() for nums = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]: " + str(interleave([[0, 1, 0], [1, 0, 0], [0, 0, 1]])))  # 3 lists with 3 elements each
    print("Testing interleave() for nums = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]: " + str(interleave([[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]])))  # 5 lists with 2 elements each
    print()

    print("Testing Weighted GPA Calculator:")
    print("Testing gpa_calculator() with grades = ['A', 'A', 'A', 'A'], credit_worth = [4, 3, 2, 3]: " + str(gpa_calculator(['A', 'A', 'A', 'A'], [4, 3, 2, 3])))  # Straight A's
    print("Testing gpa_calculator() with grades = ['F', 'F', 'F', 'F'], credit_worth = [2, 4, 3, 5]: " + str(gpa_calculator(['F', 'F', 'F', 'F'], [2, 4, 3, 5])))  # Straight F's
    print("Testing gpa_calculator() with grades = ['F','A','B','A','A'], credit_worth = [2,5,5,3,1]: " + str(gpa_calculator(['F', 'A', 'B', 'A', 'A'], [2, 5, 5, 3, 1])))  # Simple case
    print()

# Now call the main to execute the program
#
main()