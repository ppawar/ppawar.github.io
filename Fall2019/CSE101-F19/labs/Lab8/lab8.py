
# Part 1
def dictionary_test():

    d = {'one': 'hana', 'two': 'dul', 'three': 'set'}

    # As you try these 6 examples below, be sure to understand what
    # each example is trying to teach you about dictionaries.

    print('\n1. keys')
    for key in d:
        print(key)

    """ Uncomment one more example at a time until you are done with Part 0.

    print('\n2. keys once more')
    for key in d.keys():
        print(key)

    print('\n3. values')
    for value in d.values():
        print(value)

    print('\n4. items')
    for item in d.items():
        print(item)

    print('\n5. items once more')
    for item in d.items():
        print(item[0], item[1])

    print('\n6. items yet once more')
    for key, value in d.items():
        print(key, value)
    """
    return None

# Part 2
def price_check():
    prices = {
        "banana": 4,
        "apple": 2,
        "kiwi": 6,
        "orange": 1.5,
        "pear": 3.3,
        "mango": 4.5,
    }

    orange_price = prices["orange"]
    print("Orange: ", orange_price)

    # Write code to calculate the price of a pear
    #  by using the prices dictionary
    pear_price = 0
    print("Pear: ", pear_price)

    # Write code to calculate the price of a banana + kiwi
    #  by using the prices dictionary
    total = 0
    print("Banana + Apple = ", total)

    # Write code to check for the price of a papaya, which
    #  is not in the dictionary. This will crash your program
    #  so use an if statement check if papaya is in the dictionary
    #  and print out -1 when the price does not exist
    papaya_price = 0


    print("Papaya: ", papaya_price)

    # Set papaya to have a price of 5 in the dictionary


    # Now copy the above code that checks for the price of papaya
    #  and run it again. Confirm the price is 5
    papaya_price = 0

    print("Papaya (after adding a price): ", papaya_price)

# Part 3
# Implement this function as described in the lab instructions
def destination(max_distance, places):

    return None

def main():
    # Part 1
    dictionary_test()
    print()

    """ Uncomment one part at a time until you are done.
    # Part 2
    price_check()
    print()

    # Part 3

    # This is a dictionary of distances from Seoul to other cities (in kilometers)
    distances = {'Busan': 330, 'Incheon': 27, 'Daegu': 237, 'Addis Ababa': 9230,
                 'Bishkek': 4409, 'Nay Pyi Taw': 3572, 'Taipei': 1482,
                 'London': 8845, 'New York City': 11038, 'Shanghai': 867,
                 'Mumbai': 5587, 'Buenos Aires': 19406, 'Paris': 8945}

    print("The farthest city <= 400 km: ", destination(400, distances)) # prints Busan
    print("The farthest city <= 0 km: ", destination(0, distances))  # prints None
    print("The farthest city <= 4500 km: ", destination(4500, distances)) # prints Bishkek
    print("The farthest city <= 10 km: ", destination(10, distances)) # prints "Nowhere"

    # end of block comment
    """

if __name__ == '__main__':
    main()