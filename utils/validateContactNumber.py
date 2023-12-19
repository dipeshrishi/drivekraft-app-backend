def validatePhoneNumber(phone_number: str):
    if len(phone_number) == 10 and phone_number.isdigit():
        return True
    else:
        return False