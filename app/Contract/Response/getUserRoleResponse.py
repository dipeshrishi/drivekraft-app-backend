from app.Contract.Response.serviceResponse import serviceResponse
class UserRoleDetailResponse(serviceResponse):
    def __init__(self, statusCode=200,successful=False,error="None",user_role=None):
        super().__init__(statusCode,successful,error)
        self.role = user_role