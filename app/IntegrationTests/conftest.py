import pytest
from app import create_app
from ..database import db
from ..Models.mysql import userRole

@pytest.fixture(scope='module')
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/drivekraft_backend_v2'
    with app.app_context():
        db.create_all()
    yield app
    # Clean up the database and app context
    with app.app_context():
        db.session.rollback()

@pytest.fixture(scope='module')
def client(app):
    """A test client for the app."""
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='module')
def add_test_data(app):
    """Add test data to the database."""
    with app.app_context():
        customer_role = userRole.UserRole(id=3, type='CUSTOMER')
        psychologist_role = userRole.UserRole(id=2, type='PSYCHOLOGIST')
        db.session.merge(customer_role)
        db.session.merge(psychologist_role)
        db.session.commit()

