![Vanilla-1s-234px (1)](https://github.com/gluchy1/Basic-Subatomic-Particle-Simulation/assets/70800019/6a62b2bd-78ae-4c81-876c-c9c4447bd5f9)![Vanilla-1s-234px (2)](https://github.com/gluchy1/Basic-Subatomic-Particle-Simulation/assets/70800019/5adc1325-cb79-4fd2-95d4-4632ada74bf7)![Vanilla-1s-122px](https://github.com/gluchy1/Basic-Subatomic-Particle-Simulation/assets/70800019/82ed93f6-c0f9-45bb-9f7e-7ba886553f7a)![Vanilla-1s-289px](https://github.com/gluchy1/Basic-Subatomic-Particle-Simulation/assets/70800019/7520708d-df82-45da-8d0d-89425783d0c1)![Vanilla-1s-155px](https://github.com/gluchy1/Basic-Subatomic-Particle-Simulation/assets/70800019/49452e2b-068c-4479-878b-da9168c084d5)![Vanilla-1s-289px (1)](https://github.com/gluchy1/Basic-Subatomic-Particle-Simulation/assets/70800019/5dd58d79-b6ce-475a-a65e-ce8c0f3fd65f)![Vanilla-1s-187px](https://github.com/gluchy1/Basic-Subatomic-Particle-Simulation/assets/70800019/c7d5adec-0373-45a3-b6ad-6ebd08d4a3ea)  
  
![ezgif com-gif-maker](https://github.com/gluchy1/Basic-Subatomic-Particle-Simulation/assets/70800019/b0a54d83-bdeb-443a-a9dd-03f4353295ce)


# Particle Simulation with Gravitational and Electrostatic Forces  
#### This code repository contains a very *(really!)* basic particle simulation implemented using the Pygame and pymunk libraries. The simulation aims to replicate the behavior of subatomic particles under the influence of gravitational and electrostatic forces.  
*note: presentational purpose, it's not serving any real needs. only a side-side-side project that helps me to learn overall important git etc. mechanics*
## To be fixed/changed:
- added documentation in Sphinx, but I got still a lot to learn.
- fix GUI inefficiency
- create rest of options for Particles

## Short summary:
#### This particle simulation project provides a platform for visualizing the behavior of subatomic particles under gravitational and electrostatic forces. It offers control over simulation parameters, and the ability to save and load simulation states for further analysis. Ready to be modified, as it's really really basic.

Be sure to install requirements.txt
using: `pip install -r requirements.txt` in your console.

To run the simulation, execute the following command:

 `python particle_simulation.py`
  
#### Upon running the simulation, a Pygame window will open, displaying the particles and their interactions.
#### You can control various aspects of the simulation using the following keys:

- Space: Pause/Resume the simulation.
- R: Reset the simulation.
- Esc: Quit the program.
- E / D: Increase/Decrease the electrostatic force.
- G / F: Increase/Decrease the gravitational force.
- I: Toggle display of particle information.
- S: Save the simulation state.
- L: Load a previously saved simulation state.

#### Functions:

- The create_particle function creates particles within the simulation space, initializing their mass, charge, radius, position, velocity, and van der Waals radius.

- The simulation calculates and applies forces between particles, including electrostatic forces using the electrostatic_force function, and van der Waals forces using the van_der_waals_force function.

- Collisions between particles and walls are handled by the handle_collision function, which ensures appropriate reactions and changes in particle velocities upon collision via. physics implemented in various methods.

- The simulation is controlled by a main loop that processes user input, updates particle positions and forces, and renders the simulation on the Pygame screen. The loop includes functionality for pausing/resuming the simulation, resetting the simulation, adjusting force multipliers, displaying particle information, and saving/loading simulation states.

- The simulation renders the particles on the Pygame screen, with particle colors reflecting their kinetic energy. Additional information about particles, such as velocity, mass, charge, energy, momentum, and temperature, can be displayed if enabled by clicking the right key ("I").
  
Feel free to do whatever suits your needs with this repository.
