from app.database import db;

class SessionRequest(db.Model):
    __tablename__ = "sessionRequest"
    id = db.Column(db.Integer, primary_key=True)
    psychologistId = db.Column(db.Integer, db.ForeignKey('psychologist.id'), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.TIMESTAMP)
    updated = db.Column(db.TIMESTAMP)
    expired = db.Column(db.TIMESTAMP)
    sessionRequestStatusId = db.Column(db.Integer, db.ForeignKey('sessionRequestStatusMapping.id'), nullable=False)
    mode = db.Column(db.String(10), nullable=False)

    user = db.relationship('User', backref='sessionRequests', foreign_keys=[userId])
    psychologist = db.relationship('Psychologist', backref='sessionRequests', foreign_keys=[psychologistId])
    sessionRequestStatus = db.relationship('SessionRequestStatusMapping', backref='sessionRequests', foreign_keys=[sessionRequestStatusId])

