from app import create_app
from app.database import db

# app = create_app() for server add this line and comment below
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)