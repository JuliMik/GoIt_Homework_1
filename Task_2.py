import random


def get_numbers_ticket(min, max, quantity):
    numbers_list = []
    if 0 < min < max <= 1000 and 0 < quantity <= max - min:
        i = 0
        while i < quantity:
            number = random.randrange(min, max)
            if number not in numbers_list:
                numbers_list.append(number)
                i += 1
        return sorted(numbers_list)
    else:
        return numbers_list


lottery_numbers = get_numbers_ticket(1, 100, 5)
print(f"Your lottery numbers: {lottery_numbers}" )
