from app.Contract.Response.serviceResponse import serviceResponse

class otpGenerateResponse(serviceResponse):
    def __init__(self, otp, created, successful=True, error=None):
        super().__init__(statusCode=200, successful=successful, error=error)
        self.otp = otp
        self.created = created