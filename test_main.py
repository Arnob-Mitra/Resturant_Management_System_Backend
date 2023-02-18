from fastapi.testclient import TestClient
from main import app 


client = TestClient(app)

def test_get_by_id():
    response = client.get("/fooditem/d0a0ef14-6dec-4aac-b377-2ddc193ea674")
    assert response.status_code == 200
