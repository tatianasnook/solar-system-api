class Planet:
    def __init__(self, id, name, description, num_of_moons):
        self.id = id
        self.name = name
        self.description = description
        self.num_of_moons = num_of_moons

planets = [
    Planet(1, "Mercury", "smallest planet in Solar system", 0),
    Planet(2, "Venus", "Earth neighbor", 0),
    Planet(3, "Earth", "home planet for NASA", 1),
    Planet(4, "Mars", "dusty, cold, desert world", 2),
    Planet(5, "Jupiter", "largest planet in Solar system", 95),
    Planet(6, "Saturn", "second largest planet in Solar system", 146),
    Planet(7, "Uranus", "third largest planet in Solar system", 28),
    Planet(8, "Neptune", "most distant planet in Solar System", 16),
]
