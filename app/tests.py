import unittest
from .particle import Particle
import pymunk


class ParticleTestCase(unittest.TestCase):
    def setUp(self):
        self.mass = 1
        self.charge = 1
        self.radius = 1
        self.position = pymunk.Vec2d(0, 0)
        self.velocity = pymunk.Vec2d(1, 1)
        self.van_der_waals_radius = 1e-10
        self.space = pymunk.Space()
        self.particle = Particle(self.space, self.mass, self.charge, self.radius, self.position, self.velocity,
                                 self.van_der_waals_radius)

    def test_particle_initialization(self):
        self.assertEqual(self.particle.body.mass, self.mass)
        self.assertEqual(self.particle.body.charge, self.charge)
        self.assertEqual(self.particle.body.position, self.position)
        self.assertEqual(self.particle.body.velocity, self.velocity)
        self.assertEqual(self.particle.shape.radius, self.radius)
        self.assertEqual(self.particle.shape.van_der_waals_radius, self.van_der_waals_radius)

    def test_particle_energy(self):
        energy = 0.5 * self.mass * (self.velocity.length ** 2)
        self.assertEqual(self.particle.get_energy(), energy)


if __name__ == '__main__':
    unittest.main()
