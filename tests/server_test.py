import json
# from flask import Flask
# from flask.testing import FlaskClient
# from core import app

# Initialize Flask app
# app.testing = True

# Assign the Flask app to the client
# client = FlaskClient(client())


def test_ready_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data.decode("utf-8"))
    assert 'status' in data and data['status'] == 'ready'
    assert 'time' in data


def test_error_handling(client):
   
    # Test HTTPException handling
    response = client.get('/http_exception')
    assert response.status_code == 404
   


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])
