import random

class Planet:
    def __init__(self):
        self.size = self.generate_size()
        self.mass = self.generate_mass()
        self.orbital_distance, self.orbital_period = self.generate_orbital_parameters()
        self.eccentricity = self.generate_eccentricity()
        self.rotation_period = self.generate_rotation_period()
        self.axial_tilt = self.generate_axial_tilt()
        self.atmospheric_composition = self.generate_atmospheric_composition()
        self.surface_composition = self.generate_surface_composition()
        self.geological_activity = self.generate_geological_activity()
        self.climate_patterns = self.generate_climate_patterns()
        self.magnetic_field = self.generate_magnetic_field()
        self.satellites = self.generate_satellites()
        self.biosphere = self.generate_biosphere()
        self.technological_aspects = self.generate_technological_aspects()
        self.star_type = self.generate_star_type()
        self.cosmic_environment = self.generate_cosmic_environment()
        self.resource_distribution = self.generate_resource_distribution()

    def generate_size(self):
        # Sizes range from Earth-size (1) to Jupiter-size (10)
        return random.uniform(1, 10)

    def generate_mass(self):
        # Mass is correlated with size
        return self.size * random.uniform(0.8, 1.2)

    def generate_orbital_parameters(self):
        distance = random.uniform(0.5, 20) # in AU
        period = distance ** 1.5 # Simplified Kepler's Third Law
        return distance, period

    def generate_eccentricity(self):
        return random.uniform(0, 0.8)

    def generate_rotation_period(self):
        return random.uniform(10, 50) # in hours

    def generate_axial_tilt(self):
        return random.uniform(0, 45) # in degrees

    def generate_atmospheric_composition(self):
        return random.choice(["Nitrogen-Oxygen", "Carbon Dioxide", "Methane", "Hydrogen-Helium"])

    def generate_surface_composition(self):
        return random.choice(["Mostly Water", "Rocky", "Icy", "Gaseous"])

    def generate_geological_activity(self):
        return random.choice(["High", "Moderate", "Low"])

    def generate_climate_patterns(self):
        return random.choice(["Temperate", "Arid", "Frozen", "Stormy"])

    def generate_magnetic_field(self):
        return random.choice(["Strong", "Moderate", "Weak", "None"])

    def generate_satellites(self):
        return random.randint(0, 10) # Number of moons

    def generate_biosphere(self):
        return random.choice(["Diverse", "Sparse", "Microbial", "None"])

    def generate_technological_aspects(self):
        return random.choice(["Advanced", "Primitive", "Nonexistent"])

    def generate_star_type(self):
        return random.choice(["Red Dwarf", "Yellow Dwarf", "Blue Giant", "White Dwarf", "Neutron Star"])

    def generate_cosmic_environment(self):
        return random.choice(["Asteroid Belt Nearby", "In a Cluster", "Solitary", "Binary System"])

    def generate_resource_distribution(self):
        return random.choice(["Rich in Minerals", "Energy Abundant", "Scarce Resources"])

    def print_description(self):
        print("Planet Description:")
        print(f"Size: {self.size:.2f} (Earth-size units)")
        print(f"Mass: {self.mass:.2f} (Earth-mass units)")
        print(f"Distance from Star: {self.orbital_distance:.2f} AU")
        print(f"Orbital Period: {self.orbital_period:.2f} Earth years")
        print(f"Eccentricity of Orbit: {self.eccentricity:.2f}")
        print(f"Rotation Period: {self.rotation_period:.2f} hours")
        print(f"Axial Tilt: {self.axial_tilt:.2f} degrees")
        print(f"Atmospheric Composition: {self.atmospheric_composition}")
        print(f"Surface Composition: {self.surface_composition}")
        print(f"Geological Activity: {self.geological_activity}")
        print(f"Climate Patterns: {self.climate_patterns}")
        print(f"Magnetic Field: {self.magnetic_field}")
        print(f"Number of Satellites: {self.satellites}")
        print(f"Biosphere: {self.biosphere}")
        print(f"Technological Aspects: {self.technological_aspects}")
        print(f"Star Type: {self.star_type}")
        print(f"Cosmic Environment: {self.cosmic_environment}")
        print(f"Resource Distribution: {self.resource_distribution}")

def main():
    planet = Planet()
    planet.print_description()

main()
