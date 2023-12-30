from app import create_app
from app.database import db

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)