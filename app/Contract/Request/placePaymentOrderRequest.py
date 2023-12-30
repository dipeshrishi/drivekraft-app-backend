
class placePaymentOrderRequest:
    def __init__(self,transaction_id,session_request_id,seconds_chatted,psychologist_id):
        self.transaction_id = transaction_id
        self.session_request_id = session_request_id
        self.seconds_chatted=seconds_chatted
        self.psychologist_id=psychologist_id
