
def calculate_average(numbers):
    if not numbers:
        raise ValueError("numbers must not be empty")

    total = sum(numbers)
    return total / len(numbers)


def calculate_discount(price, discount):
    return price - (price * discount / 100)
