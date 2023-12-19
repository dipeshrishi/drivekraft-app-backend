from database import db

class UserRole(db.Model):
    __tablename__ = 'user_role'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum('CUSTOMER', 'LISTENER'), nullable=False)
    
    