from app.database import db
class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    transactionId = db.Column(db.String(100))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    psychologistId = db.Column(db.Integer, db.ForeignKey('psychologist.id'), nullable=False)
    sessionRequestId= db.Column(db.Integer, nullable=False)
    secondsChatted = db.Column(db.Integer, nullable=False)
    amountDeducted = db.Column(db.Integer, nullable=False)
    sessionType = db.Column(db.String(100),  nullable=True)
    created = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    updated = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    user = db.relationship('User', backref='transactions',foreign_keys=[userId])
    psychologist = db.relationship('Psychologist',backref='transactions',foreign_keys=[psychologistId])


