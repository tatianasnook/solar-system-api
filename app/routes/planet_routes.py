from flask import Blueprint
from ..models.planet import planets

planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@planet_bp.get("")
def get_all_planets():
    results_list = []

    for planet in planets:
        results_list.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            num_of_moons=planet.num_of_moons
        ))

    return results_list

@planet_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return {"message": f"planet {planet_id} invalid"}, 400

    for planet in planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "num_of_moons": planet.num_of_moons
            }
        
    return {"message": f"planet {planet_id} not found"}, 404
