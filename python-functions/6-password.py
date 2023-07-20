def validate_password(password):
    length = len(password)
    check_uppercase=0
    check_lowercase=0
    if length<8:
        return False
    for num in range(length):
        if password[num].isupper():
            check_uppercase+=1
        if password[num].islower():
            check_lowercase+=1
        if password[num] == " ":
            return False
    if check_uppercase == 0 or check_lowercase == 0:
        return False
    return True

