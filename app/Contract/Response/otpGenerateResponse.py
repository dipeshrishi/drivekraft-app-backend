from app.Contract.Response.serviceResponse import serviceResponse
class otpGenerateResponse(serviceResponse):
    def __init__(self, statusCode=200,successful=False,error="None",otp=None, created=None):
        super().__init__(statusCode,successful,error)
        self.otp = otp
        self.created = created