import pytest
from app import create_app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


# tests/test_routes.py
def test_generate_otp_success(client):
    # Send a POST request with JSON data
    response = client.post('/api/login-send-otp', json={'mobile': '917889085355'})

    # Check if the response status code is 200
    assert response.json['statusCode'] == 200

    # Check if the response contains an OTP field
    assert 'otp' in response.json

    # Check if the OTP is not null or empty
    otp = response.json['otp']
    assert otp is not None and otp != ""

    # Check if the OTP is a 6-digit number
    assert len(str(otp)) == 6

def test_generate_otp_invalid_phone_length(client):
    """Test generating OTP with an invalid phone number length."""
    # Send a request with a phone number that is not 12 characters long
    response = client.post('/api/login-send-otp', json={'mobile': '12345'})
    assert response.json['statusCode'] == 400

def test_generate_otp_empty_phone_number(client):
    """Test generating OTP with an empty phone number."""
    # Send a request with an empty phone number
    response = client.post('/api/login-send-otp', json={'mobile': ''})
    assert response.json['statusCode'] == 400

def test_generate_otp_invalid_phone_number(client):
    """Test generating OTP with an invalid phone number."""
    # Send a request with a phone number that is not a valid format
    response = client.post('/api/login-send-otp', json={'mobile': '123abc'})
    assert response.json['statusCode'] == 400


def test_verify_otp_success(client):
    response = client.post('/api/login-send-otp', json={'mobile': '919812000194'})
    assert response.status_code == 200
    assert 'otp' in response.json
    otp = response.json['otp']
    # Use the OTP value for verification
    response = client.post('/api/login', json={'otp': otp,'mobile': '919812000194'})
    assert response.status_code == 200
    assert 'verified' in response.json
    assert response.json['verified'] is True



