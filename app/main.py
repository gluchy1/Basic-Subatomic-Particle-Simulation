import pygame
import sys
from matplotlib import pyplot as plt
from app.simulation import *

"""
This particle simulation project provides a platform for visualizing
the behavior of subatomic particles under gravitational and electrostatic forces.
It offers control over simulation parameters, and the ability to save and load simulation states for further analysis.
Feel free to explore and modify the code to suit your needs!

Be sure to install requirements.txt
using: 'pip install -r requirements.txt' in your console.

I've recently added some improvements to the code, since I've gained more knowledge, like:
- divided one, long code to segments
- added config.py
- added tests.py (to be improved, since this is just a copy-paste)
- added setupy.py (to be improved, not used rly.)
- added requirements.txt which is necessary

More to be included in the code, once I learn about it more.

Note: I treat this repo not only as a side project, but as a main structure for learning coding.

---- @gluchy1 ---- 
---- https://github.com/gluchy1/Basic-Subatomic-Particle-Simulation ----
"""

introduction = (f"\n"
                f"{'-' * 72}\n"
                f"{'-' * 4} CC: @gluchy1 {'-' * 54}\n"
                f"{'-' * 4} https://github.com/gluchy1/Basic-Subatomic-Particle-Simulation {'-' * 4}\n"
                f"{'-' * 72}\n"
                f"{'-' * 2} Reach out: gluchy#9422 {'-' * 46}\n")

print(introduction)

"""
------------------------------------------------------------------------------------------------
                                      PARTICLE SIMULATION
------------------------------------------------------------------------------------------------
"""

#   matplotlib
#       - komentarze do usunięcia wtedy kiedy zamiarem jest stworzenie grafu.
#         Na ten moment graf nie działa i nie ma żadnej funkcji.

# plt.ion()
# fig, ax = plt.subplots()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def main():
    #   main loop symulacji, ustawienia, inicjacja pygame itd.

    pygame.init()
    pygame.font.init()

    handle_events()

    space = pymunk.Space()
    space.gravity = (0, 0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Subatomic Particle Simulation')
    clock = pygame.time.Clock()

    GRAVITATIONAL_CONSTANT = 4
    ELECTROSTATIC_CONSTANT = 5
    electrostatic_multiplier = 3
    gravity_multiplier = 3

    create_walls(space)

    particles = []
    reset_simulation(space, particles)
    space.add_collision_handler(1, 0).begin = handle_collision

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
                particles[i].body.apply_force_at_local_point(force, (0, 0))
                particles[j].body.apply_force_at_local_point(-force, (0, 0))

                van_der_waals = van_der_waals_force(particles[i], particles[j])
                particles[i].body.apply_force_at_local_point(van_der_waals, (0, 0))
                particles[j].body.apply_force_at_local_point(-van_der_waals, (0, 0))

        if not paused:
            space.gravity = (0, -GRAVITATIONAL_CONSTANT * gravity_multiplier)
            space.step(TIME_STEP)

            screen.fill(BACKGROUND_COLOR)
            max_kinetic_energy = max([0.5 * p.body.mass * (p.body.velocity.length ** 2) for p in particles])

            for particle in particles:
                pos = particle.body.position
                kinetic_energy = 0.5 * particle.body.mass * (particle.body.velocity.length ** 2)
                color = (
                    255 * kinetic_energy / max_kinetic_energy,
                    0,
                    255 * (1 - kinetic_energy / max_kinetic_energy),
                )

                pygame.draw.circle(screen, color, (int(pos.x), int(pos.y)), PARTICLE_RADIUS)

                if display_particle_info:
                    velocity = particle.body.velocity.length
                    mass = particle.body.mass
                    charge = particle.body.charge
                    energy = particle.get_energy()
                    momentum = particle.get_momentum()
                    temperature = particle.get_temperature()
                    particle_info = (
                        f"V:{velocity:.1f} M:{mass:.1f} C:{charge} E:{energy:.1f} "
                        f"P:{momentum:.1f} T:{temperature:.1f}"
                    )
                    particle_text_surface = font.render(particle_info, True, (0, 0, 0))
                    screen.blit(
                        particle_text_surface,
                        (int(pos.x) + PARTICLE_RADIUS + 10, int(pos.y) + PARTICLE_RADIUS + 10),
                    )

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
                "GRAVITATIONAL_CONSTANT = 6.67430e-11",
                "ELECTROSTATIC_CONSTANT = 8.9875517923e9",
                "electrostatic_multiplier = 1e-12",
                "gravity_multiplier = 1e10",
            ]
            y_offset = 10

            for line in description:
                text_surface = font.render(line, True, (0, 0, 0))
                screen.blit(text_surface, (10, y_offset))
                y_offset += 20

            pygame.display.flip()
            clock.tick(60)

    plt.ioff()
    plt.show()


if __name__ == "__main__":
    main()
