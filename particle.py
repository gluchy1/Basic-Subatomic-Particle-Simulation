import math
import pymunk
from config import *


#   logika czasteczki


class Particle:
    def __init__(self, space, mass, charge, radius, position, velocity, van_der_waals_radius):
        self.body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
        self.body.position = position
        self.body.velocity = velocity
        self.body.charge = charge
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = 1.0
        self.shape.friction = 0.0
        self.shape.van_der_waals_radius = van_der_waals_radius
        space.add(self.body, self.shape)

    def get_energy(self):
        return 0.5 * self.body.mass * (self.body.velocity.length ** 2)

    def get_momentum(self):
        return self.body.mass * self.body.velocity.length

    def get_temperature(self):
        return self.get_energy() / (self.body.mass * BOLTZMANN_CONSTANT)

    def get_larmor_radius(self, magnetic_field_strength):
        return (self.body.mass * self.body.velocity.length) / (abs(self.shape.charge) * magnetic_field_strength)

    def get_de_broglie_wavelength(self):
        return PLANCK_CONSTANT / self.get_momentum()

    def get_boltzmann_distribution(self, energy, temperature):
        return math.exp(-energy / (BOLTZMANN_CONSTANT * temperature))

    def get_thermal_conductivity(self, other_particle, distance):
        temperature_difference = abs(self.get_temperature() - other_particle.get_temperature())
        return THERMAL_DIFFUSIVITY * temperature_difference / distance