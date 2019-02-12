def check_digits(number: int):
    digits = []
    counter = len(str(abs(number))) - 1

    while counter >= 0:
        digit = (number // (10 ** counter)) % 10
        digits.append(digit)
        counter -= 1

    


check_digits(12345678)