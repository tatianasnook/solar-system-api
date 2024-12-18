def test_get_one_planet_succeeds(client, two_saved_planets):
    response = client.get("planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "similar size to Earth's moon",
        "num_of_moons": 0
    }


def test_get_one_planet_not_found_in_empty_db(client):
    response = client.get("planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": f"Planet 1 not found"}


def test_get_one_planet_not_found_with_planets_in_db(client, two_saved_planets):
    response = client.get("planets/3")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": f"Planet 3 not found"}


def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_all_planets_with_planets_in_db(client, two_saved_planets):
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


def test_create_one_planet_in_empty_db(client):
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


def test_create_one_planet_with_planets_already_in_db(client, two_saved_planets):
    response = client.post("/planets", json={
        "name": "Pluto",
        "description": "dwarf planet",
        "num_of_moons": 5
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "id": 3,
        "name": "Pluto",
        "description": "dwarf planet",
        "num_of_moons": 5
    }


def test_update_planet_succeeds(client, two_saved_planets):
    response = client.put("planets/1", json={
        "name": "Mercury",
        "description": "first planet in the solar system",
        "num_of_moons": 0
    })
    assert response.status_code == 204
    assert response.content_length is None


def test_delete_one_planet_with_planets_already_in_db(client, two_saved_planets):
    response = client.delete("planets/1")
    assert response.status_code == 204
    assert response.content_length is None
