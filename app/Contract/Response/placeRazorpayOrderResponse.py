class placeRazorpayOrderResponse:
    def __init__(self,transaction_id,user_credits,status,msg,credits_availablility,credits_sufficient_for_five_minutes):
        self.transaction_id= transaction_id
        self.user_credits = user_credits
        self.status = status
        self.msg = msg
        self.credits_availablility=credits_availablility
        self.credits_sufficient_for_five_minutes=credits_sufficient_for_five_minutes