from app.Contract.Response.serviceResponse import serviceResponse


class checkPsychologistOnlineStatusResponse(serviceResponse):
    def __init__(self, email, is_Online, statusCode=200, successful=True, error=None):
        super().__init__(statusCode, successful, error)
        self.is_Online = is_Online
        self.email = email
