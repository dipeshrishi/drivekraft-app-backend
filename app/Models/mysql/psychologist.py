from app.database import db
class Psychologist(db.Model):
    __tablename__ = 'psychologist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    profile_image = db.Column(db.String(255))
    enabled = db.Column(db.Boolean)
    description = db.Column(db.Text)
    yearsOfExp = db.Column(db.Integer)
    education = db.Column(db.String(255))
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    interest = db.Column(db.String(255))
    language = db.Column(db.String(20))
    online = db.Column(db.Integer)
    busy = db.column(db.Integer)

    user = db.relationship('User', backref='psychologists')

