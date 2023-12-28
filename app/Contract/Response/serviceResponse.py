class serviceResponse:
    def __init__(self,statusCode,successful=True,error=None):
        self.successful=successful
        self.error=error
        self.statusCode =statusCode