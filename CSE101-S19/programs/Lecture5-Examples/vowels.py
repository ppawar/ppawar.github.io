# This function counts the number of lowercase vowels in a word.

def count_vowels(word):
    vowels = 'aeiou'
    num_vowels = 0
    for letter in word.lower():  # search through a lowercase copy of word
        if letter in vowels:
            num_vowels += 1
    return num_vowels

term = 'Antidisestablishmentarianism'
print('The number of vowels in ' + term + ' is ' + str(count_vowels(term)))