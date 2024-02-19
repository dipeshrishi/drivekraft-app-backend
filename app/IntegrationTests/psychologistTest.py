import pytest


@pytest.fixture(scope='function')
def psychologist_session(client):
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

def test_get_all_psychologists(client):
    """Test getting all psychologists."""
    response = client.get('/api/psychologists')
    assert response.status_code == 200
    assert 'psychologists' in response.json

def test_set_psychologist_as_busy(client, psychologist_session):
    """Test setting a psychologist as busy."""
    auth_token = psychologist_session.json['authToken']
    headers = {'Authorization': f'Bearer {auth_token}'}
    response = client.post('/api/users/status/busy', headers=headers, json={'psychologistId': 1, 'isBusy': 1})
    assert response.status_code == 200
    assert response.json['message'] == 'Psychologist status updated successfully'

def test_check_psychologist_status(client, psychologist_session):
    """Test checking psychologist status."""
    auth_token = psychologist_session.json['authToken']
    headers = {'Authorization': f'Bearer {auth_token}'}
    response = client.post('/api/check/user/busy', headers=headers, json={'psychologistId': 1})
    assert response.status_code == 200
    assert 'isBusy' in response.json

def test_check_psychologist_online_status(client, psychologist_session):
    """Test checking psychologist online status."""
    auth_token = psychologist_session.json['authToken']
    headers = {'Authorization': f'Bearer {auth_token}'}
    response = client.get('/api/psychologist/isOnline', headers=headers)
    assert response.status_code == 200
    assert 'isOnline' in response.json

def test_create_psychologist(client):
    """Test creating a psychologist."""
    request_data = {
        'name': 'John Doe',
        'profile_image': 'https://example.com/profile.jpg',
        'contactNumber': '919898989898',
        'emailId': 'john.doe@example.com',
        'description': 'Psychologist description',
        'shortDescription': 'Short description',
        'yearsOfExp': 5,
        'education': 'PhD',
        'gender': 'Male',
        'age': 25,
        'interest': 'Psychology',
        'language': 'English',
        'sessionCount': 0,
        'rating': 4.5,
        'preferenceOrder': 1
    }
    response = client.post('/api/psychologist/create', json=request_data)
    assert response.json['statusCode']== 200
    assert response.json['psychologistId'] is not None
    assert response.json['psychologistDataId'] is not None

def test_change_status(client, psychologist_session):
    """Test changing psychologist online status."""
    auth_token = psychologist_session.json['authToken']
    headers = {'Authorization': f'Bearer {auth_token}'}
    response = client.post('/api/user/online', headers=headers, json={'isOnline': "1"})
    assert response.status_code == 200
    assert response.json['message'] == 'User online status changed successfully'
