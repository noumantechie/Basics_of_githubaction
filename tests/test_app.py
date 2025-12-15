import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home page."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Flask Docker App" in rv.data

def test_health_endpoint(client):
    """Test the health check endpoint."""
    rv = client.get('/api/health')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['status'] == 'healthy'
    assert json_data['container'] is True
