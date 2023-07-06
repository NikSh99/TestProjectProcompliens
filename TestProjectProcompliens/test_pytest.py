import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from ProjectProcompliens import app, files

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['JWT_SECRET_KEY'] = 'secretkey'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
    with app.test_client() as client:
        yield client

def test_login(client):
    with app.app_context():
        response = client.post('/login', json={'username': 'admin', 'password': 'password'})
        assert response.status_code == 200
        data = response.json
        assert 'access_token' in data

def test_login_invalid_credentials(client):
    with app.app_context():
        response = client.post('/login', json={'username': 'admin', 'password': 'wrong_password'})
        assert response.status_code == 401
        data = response.json
        assert 'message' in data
        assert data['message'] == 'Неверное имя пользователя или пароль'

def test_upload_file(client):
    with app.app_context():
        access_token = create_access_token(identity='admin')
        headers = {'Authorization': f'Bearer {access_token}'}
        file_data = {'file': (open('file.csv', 'rb'), 'file.csv')}
        response = client.post('/upload', headers=headers, data=file_data)
        assert response.status_code == 200
        assert 'Файл успешно загружен.' in response.data.decode()

def test_get_files(client):
    with app.app_context():
        access_token = create_access_token(identity='admin')
        headers = {'Authorization': f'Bearer {access_token}'}
        response = client.get('/files', headers=headers)
        assert response.status_code == 200
        data = response.json
        assert 'files' in data
        assert isinstance(data['files'], list)

def test_get_data(client):
    with app.app_context():
        access_token = create_access_token(identity='admin')
        headers = {'Authorization': f'Bearer {access_token}'}
        response = client.get('/data/file.csv', headers=headers)
        assert response.status_code == 200
        data = response.json
        assert isinstance(data, list)

def test_get_data_invalid_file(client):
    with app.app_context():
        access_token = create_access_token(identity='admin')
        headers = {'Authorization': f'Bearer {access_token}'}
        response = client.get('/data/nonexistent_file.csv', headers=headers)
        assert response.status_code == 404
        assert 'Файл не найден.' in response.data.decode()
