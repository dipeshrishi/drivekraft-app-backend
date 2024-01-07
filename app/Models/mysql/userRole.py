from app.database import db

class UserRole(db.Model):
    __tablename__ = 'userRole'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum('CUSTOMER', 'PSYCHOLOGIST'), nullable=False)
    
    