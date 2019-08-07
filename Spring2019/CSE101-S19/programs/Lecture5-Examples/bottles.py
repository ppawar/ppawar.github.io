# This program prints verses from the song 100 Bottles of Beer/Milk.

age = int(input('How old are you? '))

if age < 21:
    drink_type = 'milk'
else:
    drink_type = 'beer';

num_bottles = int(input('How many bottles of ' + drink_type +
                        ' do you have? '))

for bottle in range(num_bottles, -1, -1):
    if bottle > 1:
        print(str(bottle) + ' bottles of ' + drink_type +
              ' on the wall!')
    elif bottle == 1:
        print('1 bottle of ' + drink_type + ' on the wall!')
    else:
        print('No bottles of ' + drink_type + ' on the wall!')
