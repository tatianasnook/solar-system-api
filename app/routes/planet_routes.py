from flask import Blueprint, abort, make_response, request, Response
from ..models.planet import Planet
from ..db import db

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    num_of_moons = request_body["num_of_moons"]

    new_planet = Planet(name=name, description=description, num_of_moons=num_of_moons)
    db.session.add(new_planet)
    db.session.commit()

    response = new_planet.to_dict()
    return response, 201

@planet_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)

    planets_response = [planet.to_dict() for planet in planets]
    return planets_response


@planet_bp.get("/<planet_id>")
def get_one_planet(planet_id):

    planet = validate_planet(planet_id)

    return planet.to_dict()


@planet_bp.put("/<planet_id>")
def update_planet(planet_id):

    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.num_of_moons = request_body["num_of_moons"]

    db.session.commit()

    return Response(status=204, mimetype="application/json")


@planet_bp.delete("/<planet_id>")
def delete_planet(planet_id):

    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} is invalid"}, 400))
    
    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        abort(make_response({"message": f"planet {planet_id} not found"}, 404))

    return planet
