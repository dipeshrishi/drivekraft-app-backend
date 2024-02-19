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

def test_get_user_details(client,user_session):
    # Extract the auth token from the login response
    auth_token = user_session.json['authToken']

    # Use the auth token in the headers
    headers = {'Authorization': f'Bearer {auth_token}'}

    # Send a GET request to the endpoint
    response = client.get('/api/user',headers=headers)

    # Check if the response status code is 200
    assert response['statusCode']== 200

    # Check if the response contains user details
    user_response = response.json
    assert user_response['id'] is not None
    assert user_response['name'] is not None
    assert user_response['email'] is not None

def test_get_user_details_no_auth(client):

    headers = {'Authorization': f'Bearer afdjkahkdfhkahdfjkchskfdjh123'}

    response = client.get('/api/user',headers=headers)
    assert response['statusCode']== 401

def test_get_user_details_wrong_auth(client):

    response = client.get('/api/user')
    assert response['statusCode']== 400

def test_check_username_existing(client,user_session):
    auth_token = user_session.json['authToken']

    # Use the auth token in the headers
    headers = {'Authorization': f'Bearer {auth_token}'}

    # Send a POST request to check the existing username
    response = client.post('/api/username/check', json={'username': "Joker"},headers=headers)

    assert response.json['statusCode'] == 200

    assert response.json['status'] == 'false'
    assert 'message' in response.json


def test_check_username_non_existing(client,user_session):
    auth_token = user_session.json['authToken']

    # Use the auth token in the headers
    headers = {'Authorization': f'Bearer {auth_token}'}

    # Send a POST request to check the non-existing username
    response = client.post('/api/username/check', json={'username': "virender"},headers=headers)

    # Check if the response status code is 200
    assert response.json['statusCode'] == 200

    assert response.json['status'] == 'true'
    assert 'message' in response.json


def test_confirm_username_non_existing(client,user_session):
    auth_token = user_session.json['authToken']

    # Use the auth token in the headers
    headers = {'Authorization': f'Bearer {auth_token}'}

    # Send a POST request to check the non-existing username
    response = client.post('/api/username/check/confirm', json={'username': "virender"},headers=headers)

    # Check if the response status code is 200
    assert response.json['statusCode'] == 200

    assert response.json['status'] == 'true'

def test_fetch_user_balance_details(client, user_session):
    """Test fetching user balance details."""
    # Extract the auth token from the login response
    auth_token = user_session.json['authToken']

    # Use the auth token in the headers
    headers = {'Authorization': f'Bearer {auth_token}'}

    # Send a GET request to fetch user balance details with the auth token in the headers
    response = client.get('/api/check/user/bal', headers=headers)

    # Check the response
    assert response.status_code == 200
    assert response.json['statusCode'] == 200
    assert 'balance' in response.json

