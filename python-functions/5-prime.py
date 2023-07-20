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
