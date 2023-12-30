from app.database import db
class ListenerActiveStamps(db.Model):
    __tablename__ = 'listener_active_stamps'
    id = db.Column(db.Integer, primary_key=True)
    psyId = db.Column(db.String(255))
    startTime = db.Column(db.TIMESTAMP)
    endTime = db.Column(db.TIMESTAMP)
    startEpoch = db.Column(db.BigInteger)
    endEpoch = db.Column(db.BigInteger)
    duration = db.Column(db.Integer)