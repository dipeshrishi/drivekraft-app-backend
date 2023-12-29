from app import create_app
from app.database import db

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all(bind='user_role')
        db.create_all()
    app.run(debug=True)