class otpVerificationResponse:
    def __init__(self,authToken,created,tokenType):
        self.authToken = authToken
        self.created = created
        self.tokenType = tokenType