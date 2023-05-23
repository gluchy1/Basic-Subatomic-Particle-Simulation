import pickle
import random
import pymunk
from config import *
from particle import Particle


#   Dodanie logiki do czasteczek

def electrostatic_force(particle1, particle2, k=8.9875517923e6):
    distance = particle1.body.position.get_distance(particle2.body.position)
    force_magnitude = k * particle1.body.charge * particle2.body.charge / (distance ** 2)
    force_direction = (particle2.body.position - particle1.body.position).normalized()
    return force_direction * force_magnitude


def van_der_waals_force(particle1, particle2, a=1e-10, b=1e-3):
    distance = particle1.body.position.get_distance(particle2.body.position)
    force_magnitude = -a / (distance ** 2) + b / (distance ** 3)
    force_direction = (particle2.body.position - particle1.body.position).normalized()
    return force_direction * force_magnitude


def save_simulation_state(space, filename="simulation.pickle"):
    with open(filename, "wb") as file:
        pickle.dump(space, file)


def load_simulation_state(filename="simulation.pickle"):
    with open(filename, "rb") as file:
        space = pickle.load(file)
    return space


def handle_collision(arbiter):
    particle, wall = arbiter.shapes
    impulse = arbiter.total_impulse
    impulse_per_unit_mass = impulse / particle.body.mass
    particle.body.velocity = particle.body.velocity - 2 * impulse_per_unit_mass
    return True


#   Dodanie barier symulacji

def create_walls(space):
    walls = [
        pymunk.Segment(space.static_body, (0, 0), (0, SCREEN_HEIGHT), 1),
        pymunk.Segment(space.static_body, (0, SCREEN_HEIGHT), (SCREEN_WIDTH, SCREEN_HEIGHT), 1),
        pymunk.Segment(space.static_body, (SCREEN_WIDTH, SCREEN_HEIGHT), (SCREEN_WIDTH, 0), 1),
        pymunk.Segment(space.static_body, (SCREEN_WIDTH, 0), (0, 0), 1),
    ]

    for wall in walls:
        wall.elasticity = 1.0
        wall.friction = 0.9

    space.add(*walls)


#   reset symulacji ("R")
def reset_simulation(space, particles):
    for particle in particles:
        space.remove(particle.body, particle.shape)
    particles.clear()

    for _ in range(PARTICLE_COUNT):
        x = random.uniform(0, SCREEN_WIDTH)
        y = random.uniform(0, SCREEN_HEIGHT)
        mass = random.uniform(1, 10)
        charge = random.choice([-1, 1])
        velocity = pymunk.Vec2d(random.uniform(-100, 100), random.uniform(-100, 100))
        van_der_waals_radius = random.uniform(1e-10, 5e-10)
        particle = Particle(space, mass, charge, PARTICLE_RADIUS, (x, y), velocity, van_der_waals_radius)
        particles.append(particle)