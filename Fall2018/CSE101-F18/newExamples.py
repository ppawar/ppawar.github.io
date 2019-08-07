
#
# Reverses a list
#


a = [1,2,3,4,5]

def reverse(a):
    newlist = []
    for item in a:
        newlist = [item] + newlist
        print ("item = ", item, " newlist = ", newlist)
    return newlist


#
# Returns largest two values of a list
#
def largestTwo(a):
    large = 0
    secondlarge = 0

    for item in a:
        if item > large:
            secondlarge = large
            large = item
        elif item > secondlarge:
            secondlarge = item
    return (large, secondlarge)



#
# Checks (recursively) if a string is a palindrome
#
def isPalindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])
#
#   Less efficient version
#        result = s[0] == s[-1]
#        if result:
#            return isPalindrome(s[1:-1])
#        else:
#            return False

#
# sums (recursivly) the values in a list
#
def sumList(a):
    # base
    if len(a) == 0:
        return 0
    return a[0] + sumList(a[1:])

def doubleAll(a):
    #base
    if len(a) == 0:
        return []
    else:
        return [2*a[0]] + doubleAll(a[1:])


print("doubleAll: [1, 2, 3, 4, 5]")
print(doubleAll([1, 2, 3, 4, 5]))

print("reverse:")
mylist = reverse([1, 2, 3, 4, 5])
print("Mylist = " + str(mylist))

print("Largest 2: ")
(big_guy, big_guy2) = largestTwo([20, 15, 105, 99, 1501, 2])
print("Largest 2 of [20, 15, 105, 99, 1501, 2]: " + str(big_guy) + " " + str(big_guy2))


print("Palindromes:")
print(isPalindrome('abcdedcba'))
print(isPalindrome('abcdeecba'))


print("sumList:")
print("Sum of : [5,10,15,99,105]: " + str(sumList([5,10,15,99,105])))
