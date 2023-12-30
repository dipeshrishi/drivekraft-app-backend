from app.database import db
class Session(db.Model):
    __tablename__ = 'session'
    id = db.Column(db.Integer, primary_key=True)
    sessionRequestId = db.Column(db.Integer, db.ForeignKey('sessionRequest.id'), nullable=False)
    Created = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    updated = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)
    duration = db.Column(db.Integer)
    reviewId = db.Column(db.Integer, db.ForeignKey('review.id'))
    droppedby = db.Column(db.String(255))

    sessionRequest = db.relationship('SessionRequest', backref='sessions', foreign_keys=[sessionRequestId])
    review = db.relationship('Review', backref='sessions', foreign_keys=[reviewId])