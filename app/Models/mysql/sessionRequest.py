from app.database import db;

class SessionRequest(db.Model):
    __tablename__="session_request"
    id = db.Column(db.Integer,primary_key= True)
    psychologistId = db.Column(db.Integer,db.ForeignKey('psychologist.id'),nullable=False)
    userId = db.Column(db.integer,db.ForeignKey('user.id',nullable=False))
    created = db.Column(db.TIMESTAMP)
    updated = db.Column(db.TIMESTAMP)
    expired = db.Column(db.TIMESTAMP)
    sessionRequestStatusId = db.Column(db.Integer,db.ForeignKey('sessionRequestStatusMapping.id'),nullable=False)
    mode = db.Column(db.String,nullable="false")

    user = db.relationship('User',backref='session_requests')
    psychologist = db.relationship('Psychologist',backref='session_requests')
    sessionRequestStatus = db.relationship('SessionRequestStatusMapping',backref='session_requests')