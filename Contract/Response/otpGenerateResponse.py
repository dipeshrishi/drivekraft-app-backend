from Response import serviceResponse
class otpGenerateResponse(serviceResponse):
    def __init__(self,otp,created):
        self.otp = otp
        self.created = created