
class verifySessionResponse:
    def __init__(self, id, listener_id=None, customer_id=None, status=None, session_type=None, customer_firebase_id=None, username=None,
                 is_cancelled=None,expiry_at=None):
        self.id = id
        self.listener_id = listener_id
        self.is_cancelled = is_cancelled
        self.customer_id = customer_id
        self.status = status
        self.session_type = session_type
        self.customer_firebase_id = customer_firebase_id
        self.username = username
        self.expiry_at = None if expiry_at is None else str(expiry_at)
