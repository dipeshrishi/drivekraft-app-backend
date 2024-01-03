from app.database import db
class SessionRequestStatusMapping(db.Model):
    __tablename__ = 'sessionRequestStatusMapping'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum('CREATED','ACCEPTED', 'REJECTED', 'CANCELLED', 'MISSED'), nullable=False)
