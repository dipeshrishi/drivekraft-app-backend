import pytest


@pytest.fixture(scope='function')
def user_session(client):
    """Create a user session for testing."""
    # Send a POST request to get the OTP
    otp_response = client.post('/api/login-send-otp', json={'mobile': '919812000194'})
    response_json = otp_response.json
    assert response_json['statusCode'] == 200
    otp = response_json['otp']

    # Send a POST request to log in with the OTP
    login_response = client.post('/api/login', json={'mobile': '919812000194','otp': str(otp)})
    assert login_response.json['statusCode'] == 200

    yield login_response



def test_create_new_order(client, user_session):
    """Test creating a new payment order."""
    # Extract the auth token from the login response
    auth_token = user_session.json['authToken']

    # Use the auth token in the headers
    headers = {'Authorization': f'Bearer {auth_token}'}
    response = client.post('/api/order/create', json={'amount': '100'},headers=headers)
    print(response)
    assert response.json['order_id'] is not None
    assert response.json['amount'] == 100

def test_create_new_order_negative_value(client, user_session):
    """Test creating a new payment order."""
    # Extract the auth token from the login response
    auth_token = user_session.json['authToken']

    # Use the auth token in the headers
    headers = {'Authorization': f'Bearer {auth_token}'}
    response = client.post('/api/order/create', json={'amount': '-100'},headers=headers)
    assert response.json['order_id'] is None
