
# Computes n! (n factorial)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Returns the n-th Fibonacci number
def fib(n):
    if n == 0 or n == 1:  # two base cases
        return 1
    return fib(n - 1) + fib(n - 2)  # two recursive calls

# Returns the reverse of a string passed in as the argument 's'.
def rev(s):
    if len(s) == 1:
        return s
    return s[-1] + rev(s[:-1])

# Solution to Towers of Hanoi problem
# The argument 'n' is the number of disks in the problem.
def move_disks(n, from_tower, to_tower, aux_tower):
    if n == 1:
        print('Move disk ' + str(n) + ' from ' + from_tower + ' to ' + to_tower)
    else:
        move_disks(n-1, from_tower, aux_tower, to_tower)
        print('Move disk ' + str(n) + ' from ' + from_tower + ' to ' + to_tower)
        move_disks(n-1, aux_tower, to_tower, from_tower)

# Recursively compute the sum of 1 + 1/2 + 1/3 + ... + 1/n
def sum_fracs(n):
    if n == 1:
        return 1
    return 1/n + sum_fracs(n - 1)

# Recursively compute a sum of values in a list.
def rsum(nums):
    if len(nums) == 1:
        return nums[0]
    return nums[0] + rsum(nums[1:])

# Recursively compute "base" raised to the power "exponent"
def power(base, exponent):
    if exponent == 0:
        return 1  # base case
    elif exponent % 2 == 0:  # even exponent
        temp = power(base, exponent // 2)
        return temp * temp
    else:  # odd exponent
        temp = power(base, exponent // 2)
        return temp * temp * base

# Counts the number of occurrences of a character in a string
def count_occurrences(string, ch):
    if len(string) == 0:
        return 0
    if string[0] == ch:
        return count_occurrences(string[1:], ch) + 1
    return count_occurrences(string[1:], ch)

# Return True if the argument is a palindrome, and False if not
def is_palindrome(s):
    if len(s) <= 1:     # a string of 0 or 1 characters is a palindrome
        return True
    elif s[0] != s[-1]: # the first and last characters don't match
        return False
    else:
        return is_palindrome(s[1:-1])

# Replaces all multiples of 5 in the list with a substitute.
def replace_mult5(nums, sub):
    replace_mult5_helper(nums, sub, 0)

def replace_mult5_helper(nums, sub, i):
    if i == len(nums):  # base case
        return
    if nums[i] % 5 == 0:
        nums[i] = sub
    replace_mult5_helper(nums, sub, i+1)

# Iterative version of replace_mult5_helper():
"""
def replace_mult5_helper(nums, sub, i):
    for i in range(len(nums)):
        if nums[i] % 5 == 0:
            nums[i] = sub
"""

# Finds the index of the first occurrence of a character in a string.
# Returns None if the character is not in the string.

def rindex(string, target):
    return rindex_helper(string, target, 0)

def rindex_helper(string, target, i):
    if i >= len(string):
        return None
    elif string[i] == target:
        return i
    else:
        return rindex_helper(string, target, i+1)


# Function tests

# factorial() tests
print()
for n in range(6):
    print('factorial(' + str(n) + '): ' + str(factorial(n)))

# fib() tests
print()
for n in range(6):
    print('fib(' + str(n) + '): ' + str(fib(n)))

# move_disks() -- Towers of Hanoi problem
print('\nTowers of Hanoi:')
move_disks(4, 'A', 'B', 'C')

# sum_fracs() tests
print('\nsum_fracs(4): ' + str(sum_fracs(4)))
print('sum_fracs(1): ' + str(sum_fracs(1)))

# rsum() tests
print('\nrsum([8,1,4,5]): ' + str(rsum([8, 1, 4, 5])))
print('rsum([6]): ' + str(rsum([6])))

# power() tests
print('\npower(3,4): ' + str(power(3, 4)))
print('power(2,3): ' + str(power(2, 3)))
print('power(5,0): ' + str(power(5, 0)))

# rev() tests
string = 'stony'
print('\nrev(' + string + '): ' + rev(string))

# count_occurrences() tests
print('\ncount_occurrences("stat", "t"): ' +
      str(count_occurrences("stat", "t")))
print('count_occurrences("stonybrook", "o"): ' +
      str(count_occurrences("stonybrook", "o")))
print('count_occurrences("wolfie", "z"): ' +
      str(count_occurrences("wolfie", "z")))

# is_palindrome() tests
print('\nis_palindrome("racecar"): ' + str(is_palindrome("racecar")))
print('is_palindrome("hannah"): ' + str(is_palindrome("hannah")))
print('is_palindrome("struts"): ' + str(is_palindrome("struts")))

# replace_mult5() tests
nums = [5, 3, 15, 50, 2, 4, 6, 60]
print('\nreplace_mult5(' + str(nums) + '): ', end='')
replace_mult5(nums, 77)
print(nums)

# rindex() tests
s = 'stony brook university'
t = 'k'
print('\nrindex("' + s + '", "' + t + '"): ' + str(rindex(s, t)))
t = 'z'
print('rindex("' + s + '", "' + t + '"): ' + str(rindex(s, t)))
