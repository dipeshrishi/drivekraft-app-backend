from app.Contract.Response.serviceResponse import serviceResponse
class otpVerificationResponse(serviceResponse):
    def __init__(self,created=None,authToken=None,tokenType=None,statusCode=200,successful=False,error="None"):
        super().__init__(statusCode,successful,error)
        self.authToken = authToken
        self.created = created
        self.tokenType = tokenType