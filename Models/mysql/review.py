from database import db
class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    sessionid = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=False)
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)

    # Define the relationship with the Session table
    session = db.relationship('Session', backref='reviews')