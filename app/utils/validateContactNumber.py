def validateContactNumber(contactNumber: str):
    print(contactNumber)
    if len(contactNumber) == 12 and contactNumber:
        return True
    else:
        return False