class serviceResponse:
    def __init__(self,statusCode=200,successful=True,error=None):
        self.successful=successful
        self.error=error
        self.statusCode =statusCode