
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)


def calculate_discount(price, discount):
    return price - (price * discount / 100)
