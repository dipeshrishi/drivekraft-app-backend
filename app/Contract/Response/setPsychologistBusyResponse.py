from app.Contract.Response.serviceResponse import serviceResponse
class setPsychologistBusyResponse(serviceResponse):
    def __init__(self,is_busy=None,is_Online=None,statusCode=200,successful=True,error=None):
        super().__init__(statusCode,successful,error)
        self.is_busy = is_busy
        self.is_Online = is_Online