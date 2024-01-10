from app.Contract.Response.serviceResponse import serviceResponse
class userBalanceResponse(serviceResponse):
    def __init__(self, statusCode=200,successful=False,error="None",balance=None):
        super().__init__(statusCode,successful,error)
        self.balance = balance
