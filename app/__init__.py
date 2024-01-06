from flask import Flask
from .cache import cache
from .Models.mysql import (otp,
paymentGateway,
listenerActiveStamps,
psychologist,
psychologistData,
review,
sessionRequestStatusMapping,
session,
sessionRequest,
token,
user,
userRole)
from .database import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/drivekraft_backend_v2'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['CACHE_TYPE'] = 'simple'
    cache.init_app(app)
    
    db.init_app(app)
    with app.app_context():
        db.create_all()
        # app.wsgi_app = RequestFormatMiddleware(app.wsgi_app)

    from .Routes import otpRoutes
    app.register_blueprint(otpRoutes.otpBlueprint)
    from .Routes import userRoutes
    app.register_blueprint(userRoutes.userBlueprint)

    

    @app.route('/')
    # @create_db_session
    def home():
        # session = g.session
        # now = currentTime.getCurrentTime()
        # new_otp = otp.otp(otp="12314323",userId="1", created=now)

        # session.add(new_otp)
        # session.commit()

        return "Welcome to driveKraft"
    
    return app


