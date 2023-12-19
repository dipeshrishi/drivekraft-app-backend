from flask import Flask
from database import db_session
from Routes import otpRoutes
app = Flask(__name__)

app.register_blueprint(otpRoutes.otpBlueprint)

@app.route('/')
def home():
    return 'Hello, Flask!'


if __name__ == '__main__':
    app.run(debug=True)