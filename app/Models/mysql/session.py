from app.database import db
class Session(db.Model):
    __tablename__ = 'session'
    id = db.Column(db.Integer, primary_key=True)
    SessionRequestid = db.Column(db.Integer, db.ForeignKey('session_request.id'), nullable=False)
    Created = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    updated = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)
    Duration = db.Column(db.Integer)
    review_id = db.Column(db.Integer, db.ForeignKey('review.id'))
    droppedby = db.Column(db.String(255))

    session_request = db.relationship('SessionRequest', backref='sessions')

    review = db.relationship('Review', backref='session')