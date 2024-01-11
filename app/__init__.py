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
import logging
from logging.handlers import TimedRotatingFileHandler

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/drivekraft_backend_v2'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['CACHE_TYPE'] = 'simple'
    cache.init_app(app)
    
    db.init_app(app)
    with app.app_context():
        db.create_all()
        customer_role = userRole.UserRole(type='CUSTOMER')
        psychologist_role = userRole.UserRole(type='PSYCHOLOGIST')
        db.session.add(customer_role)
        db.session.add(psychologist_role)
        db.session.commit()

    from .Routes import otpRoutes
    app.register_blueprint(otpRoutes.otpBlueprint)
    from .Routes import userRoutes
    app.register_blueprint(userRoutes.userBlueprint)
    from .Routes import roleRoutes
    app.register_blueprint(roleRoutes.roleBlueprint)
    from .Routes import paymentRoutes
    app.register_blueprint(paymentRoutes.paymentBlueprint)
    from .Routes import psychologistRoutes
    app.register_blueprint(psychologistRoutes.psychologistBlueprint)
    from .Routes import sessionRoutes
    app.register_blueprint(sessionRoutes.sessionBlueprint)
    from .Routes import versionRoutes
    app.register_blueprint(versionRoutes.versionBlueprint)

    app.logger.setLevel(logging.INFO)

    file_handler = TimedRotatingFileHandler('app.log', when='midnight', interval=1, backupCount=7)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    app.logger.addHandler(file_handler)

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


