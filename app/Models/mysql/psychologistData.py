from app.database import db

class PsychologistData(db.Model):
    __tablename__ = 'psychologistData'
    id = db.Column(db.Integer, primary_key=True)
    psychologistId = db.Column(db.Integer, db.ForeignKey('psychologist.id', ondelete='CASCADE'), nullable=False)
    sessionCount = db.Column(db.Integer)
    rating = db.Column(db.Float)
    preferenceOrder = db.Column(db.Integer)
    isBusy = db.Column(db.Boolean,default=False)
    status = db.Column(db.Boolean,default=False)
    online = db.Column(db.Boolean,default=False)
    lastSeen = db.Column(db.TIMESTAMP)
    missedRequestCount = db.Column(db.Integer, default=0)
    totalRequestsReceivedCount = db.Column(db.Integer, default=0)
    firebaseId = db.Column(db.String(255))
    firebaseName = db.Column(db.String(255))
    firebaseEmail = db.Column(db.String(255))
    firebasePassword = db.Column(db.String(255))
    is_call = db.Column(db.Boolean,default=False)
    is_chat = db.Column(db.Boolean,default=False)

    psychologist = db.relationship('Psychologist', backref='psychologistData',foreign_keys=[psychologistId])

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

