from app.database import db
class otp(db.Model):
    __tablename__ = 'otp'
    id = db.Column(db.Integer, primary_key=True)
    userId=db.Column(db.Integer)
    otp = db.Column(db.Integer)
    created = db.Column(db.TIMESTAMP)