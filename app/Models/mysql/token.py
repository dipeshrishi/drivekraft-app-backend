from app.database import db

class Token(db.Model):
    __tablename__ = 'token'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    value = db.Column(db.String(255))
    created = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    expired = db.Column(db.TIMESTAMP)
    
    user = db.relationship('User', backref='tokens')