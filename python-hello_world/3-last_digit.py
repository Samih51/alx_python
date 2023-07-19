import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10

output = "The string Last digit of, " + str(number) + ", is " + str(last_digit) + " and is"

output += " greater than 5" * (last_digit > 5)
output += " 0" * (last_digit == 0)
output += " less than 6 and not 0" * (last_digit < 6 and last_digit != 0)

print(output)
