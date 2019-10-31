
# Computes n! (n factorial)
def factorial(n):
    pass

# Returns the n-th Fibonacci number
def fib(n):
    pass

# Returns the reverse of a string passed in as the argument 's'.
def rev(s):
    pass

# Recursively compute the sum of 1 + 1/2 + 1/3 + ... + 1/n
def sum_fracs(n):
    pass

# Recursively compute a sum of values in a list.
def rsum(nums):
    pass

# Recursively compute "base" raised to the power "exponent"
def power(base, exponent):
    pass

# Counts the number of occurrences of a character in a string
def count_occurrences(string, ch):
    pass

# Return True if the argument is a palindrome, and False if not
def is_palindrome(s):
    pass

# Replaces all multiples of 5 in the list with a substitute.
def replace_mult5(nums, sub):
    pass

def replace_mult5_helper(nums, sub, i):
    pass

# Finds the index of the first occurrence of a character in a string.
# Returns None if the character is not in the string.

def rindex(string, target):
    pass


# Function tests

# factorial() tests
print()
for n in range(6):
    print('factorial(' + str(n) + '): ' + str(factorial(n)))

# fib() tests
print()
for n in range(6):
    print('fib(' + str(n) + '): ' + str(fib(n)))

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
