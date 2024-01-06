from app.Contract.Response.serviceResponse import serviceResponse

class createRazorpayOrderResponse(serviceResponse):
    def __init__(self,order_id,currency,amount):
        self.order_id = order_id
        self.currency = currency
        self.amount=amount