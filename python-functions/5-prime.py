def is_prime(number):
    if number == 0 or number == 1:
        return False
    no = abs(number)
    count = no - 1
    while (count > 1):
        if no%count ==0 :
            return True
        count=count-1
    return False
print(is_prime(15))
print(is_prime(17))
print(is_prime(-5))
print(is_prime(0))