from flask import Flask
from .database import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/drivekraft_backend_v2'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)


    from .Routes import otpRoutes
    app.register_blueprint(otpRoutes.otpBlueprint)

    @app.route('/')
    def home():
        return 'Welcome to DriveKraft!'
    
    return app


