from fastapi.testclient import TestClient
from main import app 


client = TestClient(app)

def test_get_by_id():
    response = client.get("/fooditem/29d3f800-541c-4d60-84df-dd9d22f49c45")
    assert response.status_code == 200
    assert response.json() == {"msg": "successfully get the food item"}
    
    