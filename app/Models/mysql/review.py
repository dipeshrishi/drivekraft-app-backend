from app.database import db
class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=False)
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)

    session = db.relationship('Session', backref='reviews', foreign_keys=[sessionId])
