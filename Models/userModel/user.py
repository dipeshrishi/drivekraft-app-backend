from database import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    contactNumber = db.Column(db.String(15))
    created = db.Column(db.TIMESTAMP)
    updated = db.Column(db.TIMESTAMP)
    firebaseId = db.Column(db.String(255))
    roleId = db.Column(db.Integer, db.ForeignKey('user_role.id'), nullable=False)  # Foreign key relationship
    balance = db.Column(db.DECIMAL(10, 2))
    isBlocked = db.Column(db.Boolean)

    userRole = db.relationship('UserRole', backref='users')
    