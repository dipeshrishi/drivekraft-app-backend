from app.Contract.Response.serviceResponse import serviceResponse
class updatePsychologistStatusResponse(serviceResponse):
    def __init__(self,user=None,statusCode=200,successful=True,error="None"):
        super().__init__(statusCode,successful,error)
        self.user = user