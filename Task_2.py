import random


def get_numbers_ticket(min, max, quantity):
    numbers_list = []
    i = 0
    while i < quantity:
        number = random.randrange(min, max)
        if number not in numbers_list:
            numbers_list.append(number)
            i += 1
    return sorted(numbers_list)


while True:
    try:
        min_number = int(input('Please enter the minimum possible number in the set (not less than 1): '))
        if min_number > 0:
            max_number = int(input('Please enter the maximum possible number in the set (no more than 1000): '))
            if 1000 >= max_number > min_number:
                quantity = int(input('Please enter the number of numbers to select (value between min and max): '))
                if quantity <= max_number - min_number:
                    break
                else:
                    print('Please, try again!')
            else:
                print('Please, try again!')
        else:
            print('Please, try again!')
    except ValueError:
        print('Invalid value! Please, try again!')

print(get_numbers_ticket(min_number, max_number, quantity))
