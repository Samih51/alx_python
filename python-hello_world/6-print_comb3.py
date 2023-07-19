combinations = []
for num1 in range(9):
    for num2 in range(num1 + 1, 10):
        combinations.append("{:d}{:d}".format(num1, num2))

output = ", ".join(combinations)
print(output)


