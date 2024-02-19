import pytest


@pytest.fixture(scope='function')
def user_session(client):
    """Create a user session for testing."""
    # Send a POST request to get the OTP
    otp_response = client.post('/api/login-send-otp', json={'mobile': '919850900194'})
    response_json = otp_response.json
    assert response_json['statusCode'] == 200
    otp = response_json['otp']

    # Send a POST request to log in with the OTP
    login_response = client.post('/api/login', json={'mobile': '919850900194','otp': str(otp)})
    assert login_response.json['statusCode'] == 200

    yield login_response

def test_get_role(client,user_session):
    """Test the getRole endpoint."""

    auth_token = user_session.json['authToken'];

    headers = {'Authorization': f'Bearer {auth_token}'}
    response = client.get('/api/role',headers=headers)

    assert response.status_code == 200
    assert response.json['id'] is not None