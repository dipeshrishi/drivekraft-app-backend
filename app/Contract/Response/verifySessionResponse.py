
class verifySessionResponse:
    def __init__(self, id, listener_id, customer_id, status, session_type, customer_firebase_id, username,
                 is_cancelled,expiry_at):
        self.id = id
        self.listener_id = listener_id
        self.is_cancelled = is_cancelled
        self.customer_id = customer_id
        self.status = status
        self.session_type = session_type
        self.customer_firebase_id = customer_firebase_id
        self.username = username
        self.expiry_at = str(expiry_at)