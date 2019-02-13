def check_digits(number: int):
    num_str = str(number)
    if len(num_str) < 11:
        num_str = '0' * (11 - len(num_str)) + num_str 

    digits = [int(digit) for digit in num_str]

    m = ((sum(digits[::2]) * 3) + sum(digits[1::2])) % 10

    return (10 - m) % 10
