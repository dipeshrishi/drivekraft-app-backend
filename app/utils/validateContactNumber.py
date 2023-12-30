def validateContactNumber(contactNumber: str):
    if len(contactNumber) == 10 and contactNumber.isdigit():
        return True
    else:
        return False