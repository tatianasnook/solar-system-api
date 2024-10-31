def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_success(client, two_saved_planets):
    response = client.get("planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "similar size to Earth's moon",
        "num_of_moons": 0
    }

def test_get_one_planet_failure(client):
    response = client.get("planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": f"planet 1 not found"}

def test_get_all_planets_success(client, two_saved_planets):
    response = client.get("planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Mercury",
        "description": "similar size to Earth's moon",
        "num_of_moons": 0
    },
    {
        "id": 2,
        "name": "Venus",
        "description": "hotter than Mercury",
        "num_of_moons": 0
    }]

def test_create_one_planet(client):
    response = client.post("/planets", json={
        "name": "Pluto",
        "description": "dwarf planet",
        "num_of_moons": 5
    })
    response_body = response.get_json()
    
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Pluto",
        "description": "dwarf planet",
        "num_of_moons": 5
    }
