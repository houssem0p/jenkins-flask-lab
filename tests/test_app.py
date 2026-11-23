import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Jenkins CI/CD Lab" in response.data

def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}