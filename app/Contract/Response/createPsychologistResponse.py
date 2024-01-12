from app.Contract.Response.serviceResponse import serviceResponse
class createPsychologistResponse(serviceResponse):
    def __init__(self,psychologistId=None,psychologistDataId=None,statusCode=200,successful=False,error="None"):
        super().__init__(statusCode,successful,error)
        self.psychologistId = psychologistId
        self.psychologistDataId = psychologistDataId