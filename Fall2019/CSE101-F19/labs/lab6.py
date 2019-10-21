# CSE 101
# Lab #6
# Name: < Write your name here >
# Email: < Write your Stony Brook Email here >

# Part 1
def sequence(n):
    return None  # Replace this line with your solution


# Part 2
def session_simulator(clients, regular):
    return None  # Replace this line with your solution


# Part 3
def cafe_day(orders):
    return None  # Replace this line with your solution


# Part 4
def premium_airlines(membership, price, points):
    return None  # Replace this line with your solution


# Part 5
def unfair_hiring_system(applications, mood):
    return None  # Replace this line with your solution


def main():
    # Part 1
    print("Testing Part 1")
    print("sequence(4): " + str(sequence(4)))
    print("sequence(12): " + str(sequence(12)))
    print("sequence(24): " + str(sequence(24)))
    print()

    # Part 2
    print("Testing Part 2")
    print("session_simulator([5, 5], 10): " + str(session_simulator([5, 5], 10)))
    print("session_simulator([1, 5, 4, 11], 10): " + str(
        session_simulator([1, 5, 4, 11], 10)))
    print("session_simulator([5, 7, 5, 6], 20): " + str(
        session_simulator([5, 7, 5, 6], 20)))
    print()

    # Part 3
    orders1 = [['P', 5, 0, 4]]
    orders2 = [['B', 1, 2, 3], ['P', 5, 0, 4], ['G', 4, 4, 2]]
    orders3 = [['G', 4, 3, 2], ['S', 0, 0, 10], ['P', 1, 4, 3]]
    print("Testing Part 3")
    print("cafe_day(orders1): " + str(cafe_day(orders1)))
    print("cafe_day(orders2): " + str(cafe_day(orders2)))
    print("cafe_day(orders3): " + str(cafe_day(orders3)))
    print()

    # Part 4
    print("Testing Part 4")
    print("premium_airlines('Diamond', 4999, 700): " + str(premium_airlines('Diamond', 4999, 700)))
    print("premium_airlines('Regular', 5000, 300): " + str(premium_airlines('Regular', 5000, 300)))
    print("premium_airlines('Platinum', 500, 1000): " + str(premium_airlines('Platinum', 500, 1000)))
    print()

    # Part 5
    application1 = ['Strong', 'Fair', 'Disaster']
    application2 = []
    application3 = ['Disaster', 'Poor', 'Disaster', 'Disaster', 'Disaster', 'Poor', 'Disaster', 'Poor']
    print("Testing Part 5")
    print("unfair_hiring_system(application1, 100): ", str(unfair_hiring_system(application1, 100)))
    print("unfair_hiring_system(application2, 50): ", str(unfair_hiring_system(application2, 50)))
    print("unfair_hiring_system(application3, 200): ", str(unfair_hiring_system(application3, 200)))


if __name__ == '__main__':
    main()
