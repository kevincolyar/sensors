from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_errors():
    client.delete("/errors")
    response = client.get("/errors")
    assert response.status_code == 200
    assert response.json() == []

def test_delete_errors():
    response = client.delete("/errors")
    assert response.status_code == 200
    assert response.json() == 'Errors cleared'

def test_post_temp_empty():
    response = client.post("/temp", json={
        "data": ""
    })

    assert response.status_code == 400
    assert response.json() == {'error': 'bad request'}

def test_post_missing_value():
    response = client.post("/temp", json={
        "data": "365951380:1640995229697:'Temperature'"
    })

    assert response.status_code == 400
    assert response.json() == {'error': 'bad request'}

def test_errors_return():
    client.delete('/errors')
    response = client.post("/temp", json={
        "data": "365951380:1640995229697:'Temperature'"
    })

    response = client.post("/temp", json={
        "data": "365951380:1640995229697:'Temp':58.48256793121914"
    })

    assert response.status_code == 400
    assert response.json() == {'error': 'bad request'}

    assert client.get('/errors').json() == [
        "365951380:1640995229697:'Temperature'",
        "365951380:1640995229697:'Temp':58.48256793121914"
    ]

def test_post_unsupported_measurement():
    response = client.post("/temp", json={
        "data": "365951380:1640995229697:'Temp':58.48256793121914"
    })

    assert response.status_code == 400
    assert response.json() == {'error': 'bad request'}

def test_post_temp():
    response = client.post("/temp", json={
        "data": "365951380:1640995229697:'Temperature':58.48256793121914"
    })
    assert response.status_code == 200
    assert response.json() == {'overtemp': False}

def test_post_temp_overtemp():
    response = client.post("/temp", json={
        "data": "365951380:1640995229697:'Temperature':90.0"
    })
    assert response.status_code == 200
    assert response.json() == {
        'overtemp': True,
        'device_id': 365951380,
        'formatted_time': '2022/01/01 00:00:29'
    }
