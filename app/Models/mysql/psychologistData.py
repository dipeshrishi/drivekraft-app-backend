from app.database import db

class PsychologistData(db.Model):
    __tablename__ = 'psychologist_data'
    id = db.Column(db.Integer, primary_key=True)
    psyId = db.Column(db.Integer, db.ForeignKey('psychologist.id'), nullable=False)
    sessionCount = db.Column(db.Integer)
    rating = db.Column(db.Float)
    preferenceOrder = db.Column(db.Integer)
    lastSeen = db.Column(db.TIMESTAMP)
    missedRequestCount = db.Column(db.Integer)
    totalRequestsReceivedCount = db.Column(db.Integer)

    psychologist = db.relationship('Psychologist', backref='psychologist_data')
        