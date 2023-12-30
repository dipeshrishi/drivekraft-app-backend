from app.Contract.Response.serviceResponse import serviceResponse

class confirmRazorpayOrderResponse(serviceResponse):

    def __init__(self,msg,status,title):
        self.msg = msg
        self.status = status
        self.title=title