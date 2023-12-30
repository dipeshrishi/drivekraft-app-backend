from app.database import db
class PaymentOrder(db.Model):
    __tablename__ = 'payment_order'
    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.String(100))
    paymentId = db.Column(db.String(100),  nullable=True)
    signature = db.Column(db.String(100), nullable=True)
    amount = db.Column(db.String(6))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    paymentGateway = db.Column(db.String(30))
    created = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    updated = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    user = db.relationship('User', backref='payment_order')


