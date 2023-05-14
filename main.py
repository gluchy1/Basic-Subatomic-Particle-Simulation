import math
import random
import pygame
import pymunk
import pickle
from matplotlib import pyplot as plt

# ------------------------------------------------------------------------------------------------

pygame.init()
pygame.font.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
PARTICLE_RADIUS = 2
PARTICLE_COUNT = 100
TIME_STEP = 1 / 60.0
BACKGROUND_COLOR = (255, 255, 255)
MAGNETIC_FIELD_STRENGTH = 0.01
PLANCK_CONSTANT = 6.62607015e-34
BOLTZMANN_CONSTANT = 1.380649e-23
THERMAL_DIFFUSIVITY = 1e-6
charge = 5

space = pymunk.Space()
space.gravity = (0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Symulacja cząstek subatomowych')
clock = pygame.time.Clock()

# FAKE FOR SIMULATION PURPOSES
GRAVITATIONAL_CONSTANT = 4
ELECTROSTATIC_CONSTANT = 5
electrostatic_multiplier = 3
gravity_multiplier = 3

# REAL CONST
# GRAVITATIONAL_CONSTANT = 6.67430e-11
# ELECTROSTATIC_CONSTANT = 8.9875517923e9
# electrostatic_multiplier = 1e-12
# gravity_multiplier = 1e10

# ------------------------------------------------------------------------------------------------

# def create_particle(space, position, charge, mass):
#     shape = pymunk.Circle(None, PARTICLE_RADIUS)
#     shape.body = pymunk.Body(mass, float('inf'))
#     shape.body.position = position
#     shape.body.angle = random.uniform(0, 2 * math.pi)
#     shape.elasticity = 0.95
#     shape.friction = 0.9
#     shape.collision_type = 1  # Dodajemy typ kolizji
#     shape.charge = charge  # Dodajemy ładunek do kształtu
#     shape.body.shape = shape
#     space.add(shape.body)
#     return shape.body

def get_energy(particle):
    return 0.5 * particle.mass * (particle.velocity.length ** 2)


def get_momentum(particle):
    return particle.mass * particle.velocity.length


def get_temperature(particle):
    return get_energy(particle) / (particle.mass * BOLTZMANN_CONSTANT)


def get_larmor_radius(particle, magnetic_field_strength):
    return (particle.mass * particle.velocity.length) / (abs(particle.shape.charge) * magnetic_field_strength)


def get_de_broglie_wavelength(particle, planck_constant):
    return planck_constant / get_momentum(particle)


def get_boltzmann_distribution(energy, temperature, boltzmann_constant):
    return math.exp(-energy / (boltzmann_constant * temperature))


def get_thermal_conductivity(particles, thermal_diffusivity, distance):
    particle1, particle2 = particles
    temperature_difference = abs(get_temperature(particle1) - get_temperature(particle2))
    return thermal_diffusivity * temperature_difference / distance

def van_der_waals_force(particle1, particle2, C=1e-9):
    distance = particle1.position.get_distance(particle2.position)
    force_magnitude = C / (distance ** 6)
    force_direction = (particle2.position - particle1.position).normalized()
    return force_direction * force_magnitude

def create_particle(space, mass, charge, radius, position, velocity, van_der_waals_radius):
    body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
    body.position = position
    body.velocity = velocity
    body.charge = charge
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 1.0
    shape.friction = 0.0
    shape.van_der_waals_radius = van_der_waals_radius
    space.add(body, shape)
    return body

def electrostatic_force(particle1, particle2, k=8.9875517923e6):
    distance = particle1.position.get_distance(particle2.position)
    force_magnitude = k * particle1.charge * particle2.charge / (distance ** 2)
    force_direction = (particle2.position - particle1.position).normalized()
    return force_direction * force_magnitude

def save_simulation_state(space, filename="simulation.pickle"):
    with open(filename, "wb") as file:
        pickle.dump(space, file)

def load_simulation_state(filename="simulation.pickle"):
    with open(filename, "rb") as file:
        space = pickle.load(file)
    return space

def handle_collision(arbiter, space, data):
    particle, wall = arbiter.shapes
    impulse = arbiter.total_impulse
    impulse_per_unit_mass = impulse / particle.body.mass
    particle.body.velocity = particle.body.velocity - 2 * impulse_per_unit_mass
    return True


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


create_walls(space)

def reset_simulation(space, particles):
    space.remove(*particles)
    particles.clear()
    for _ in range(PARTICLE_COUNT):
        x = random.uniform(0, SCREEN_WIDTH)
        y = random.uniform(0, SCREEN_HEIGHT)
        mass = random.uniform(1, 10)
        charge = random.choice([-1, 1])
        velocity = pymunk.Vec2d(random.uniform(-100, 100), random.uniform(-100, 100))
        van_der_waals_radius = random.uniform(1e-10, 5e-10)
        particle = create_particle(space, mass, charge, PARTICLE_RADIUS, (x, y), velocity, van_der_waals_radius)
        particles.append(particle)

# ------------------------------------------------------------------------------------------------


particles = []
electrostatic_potential_energies = []
larmor_radii = []
de_broglie_wavelengths = []
boltzmann_distributions = []
thermal_conductivities = []

reset_simulation(space, particles)
space.add_collision_handler(1, 0).begin = handle_collision

plt.ion()
fig, ax = plt.subplots()

# -------------------------------- MAIN LOOP ------------------------------------------------------
running = True
paused = False
display_particle_info = False
font = pygame.font.SysFont('Arial', 16)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_r:
                reset_simulation(space, particles)
            elif event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_e:
                electrostatic_multiplier += 0.1
            elif event.key == pygame.K_d:
                electrostatic_multiplier -= 0.1
            elif event.key == pygame.K_g:
                gravity_multiplier += 0.1
            elif event.key == pygame.K_f:
                gravity_multiplier -= 0.1
            elif event.key == pygame.K_i:
                display_particle_info = not display_particle_info
            elif event.key == pygame.K_s:
                save_simulation_state(space)
            elif event.key == pygame.K_l:
                space = load_simulation_state()

    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            force = electrostatic_force(particles[i], particles[j])
            particles[i].apply_force_at_local_point(force, (0, 0))
            particles[j].apply_force_at_local_point(-force, (0, 0))

            van_der_waals = van_der_waals_force(particles[i], particles[j])
            particles[i].apply_force_at_local_point(van_der_waals, (0, 0))
            particles[j].apply_force_at_local_point(-van_der_waals, (0, 0))

    if not paused:
        space.gravity = (0, -GRAVITATIONAL_CONSTANT * gravity_multiplier)

        # space.step(TIME_STEP)
        space.step(1 / 60)

        # RENDER
        screen.fill(BACKGROUND_COLOR)
        max_kinetic_energy = max([0.5 * p.mass * (p.velocity.length ** 2) for p in particles])
        for particle in particles:
            pos = particle.position
            kinetic_energy = 0.5 * particle.mass * (particle.velocity.length ** 2)
            color = (255 * kinetic_energy / max_kinetic_energy, 0, 255 * (1 - kinetic_energy / max_kinetic_energy))
            pygame.draw.circle(screen, color, (int(pos.x), int(pos.y)), PARTICLE_RADIUS)

            if display_particle_info:
                velocity = particle.velocity.length
                mass = particle.mass
                # charge = particle.shape.charge  # Updated line
                charge = particle.charge
                energy = get_energy(particle)
                momentum = get_momentum(particle)
                temperature = get_temperature(particle)
                particle_info = f"V:{velocity:.1f} M:{mass:.1f} C:{charge} E:{energy:.1f} P:{momentum:.1f} T:{temperature:.1f}"
                particle_text_surface = font.render(particle_info, True, (0, 0, 0))
                screen.blit(particle_text_surface,
                            (int(pos.x) + PARTICLE_RADIUS + 10, int(pos.y) + PARTICLE_RADIUS + 10))


        description = [
            f"Particles: {len(particles)}",
            f"Space: {SCREEN_WIDTH}x{SCREEN_HEIGHT}",
            f"Paused: {paused}",
            f"Press 'R' to reset",
            f"Press 'Space' to pause/resume",
            f"Press 'Esc' to quit",
            f" ",
            f"Electrostatic constant: {ELECTROSTATIC_CONSTANT * electrostatic_multiplier:.1f}",
            f"Gravity constant: {GRAVITATIONAL_CONSTANT * gravity_multiplier:.1f}",
            f"Press 'E'/'D' to increase/decrease electrostatic force",
            f"Press 'G'/'F' to increase/decrease gravity",
            f"Press 'I' to toggle particle info",
            f" ",
            f" GRAVITATIONAL_CONSTANT = 6.67430e-11",
            f" ELECTROSTATIC_CONSTANT = 8.9875517923e9",
            f" electrostatic_multiplier = 1e-12",
            f" gravity_multiplier = 1e10"
        ]
        y_offset = 10

        for line in description:
            text_surface = font.render(line, True, (0, 0, 0))
            screen.blit(text_surface, (10, y_offset))
            y_offset += 20

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
plt.ioff()
plt.show()
