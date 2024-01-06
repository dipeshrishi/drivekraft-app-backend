from app.database import db

class PsychologistData(db.Model):
    __tablename__ = 'psychologistData'
    id = db.Column(db.Integer, primary_key=True)
    psychologistId = db.Column(db.Integer, db.ForeignKey('psychologist.id', ondelete='CASCADE'), nullable=False)
    sessionCount = db.Column(db.Integer)
    rating = db.Column(db.Float)
    preferenceOrder = db.Column(db.Integer)
    isBusy = db.Column(db.Boolean)
    status = db.Column(db.Boolean)
    online = db.Column(db.Boolean)
    lastSeen = db.Column(db.TIMESTAMP)
    missedRequestCount = db.Column(db.Integer)
    totalRequestsReceivedCount = db.Column(db.Integer)
    firebaseId = db.Column(db.String(255))
    firebaseName = db.Column(db.String(255))
    firebaseEmail = db.Column(db.String(255))
    firebasePassword = db.Column(db.String(255))

    psychologist = db.relationship('Psychologist', backref='psychologistData')

        