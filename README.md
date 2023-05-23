# Particle Simulation with Gravitational and Electrostatic Forces  
#### This code repository contains a very *(really!)* basic particle simulation implemented using the Pygame and pymunk libraries. The simulation aims to replicate the behavior of subatomic particles under the influence of gravitational and electrostatic forces.  
*Note: Code for presentational purpose for learning how to implement various physics into python!*
## To be fixed/changed:
- setupy.py // __init__.py
- instr.txt
- Divide the code to separate python files to make it easier to read and modify,
- Create main.py responsible only for running the simulation,
- Make code easier to read,
- Delete unused code

## Short summary:
#### This particle simulation project provides a platform for visualizing the behavior of subatomic particles under gravitational and electrostatic forces. It offers control over simulation parameters, and the ability to save and load simulation states for further analysis. Feel free to explore and modify the code to suit your needs!

### Installation & Usage
#### To run the simulation, make sure you have the following dependencies installed:

- Pygame
- pymunk
- matplotlib

You can install the required packages using pip:

 `pip install pygame pymunk matplotlib`

To run the simulation, execute the following command:

 `python particle_simulation.py`
  
#### Upon running the simulation, a Pygame window will open, displaying the particles and their interactions. You can control various aspects of the simulation using the following keyboard inputs:

- Space: Pause/Resume the simulation.
- R: Reset the simulation.
- Esc: Quit the program.
- E / D: Increase/Decrease the electrostatic force.
- G / F: Increase/Decrease the gravitational force.
- I: Toggle display of particle information.
- S: Save the simulation state.
- L: Load a previously saved simulation state.

#### The simulation code consists of the following components:

- The create_particle function creates particles within the simulation space, initializing their mass, charge, radius, position, velocity, and van der Waals radius.

- The simulation calculates and applies forces between particles, including electrostatic forces using the electrostatic_force function, and van der Waals forces using the van_der_waals_force function.

- Collisions between particles and walls are handled by the handle_collision function, which ensures appropriate reactions and changes in particle velocities upon collision.

- The simulation is controlled by a main loop that processes user input, updates particle positions and forces, and renders the simulation on the Pygame screen. The loop includes functionality for pausing/resuming the simulation, resetting the simulation, adjusting force multipliers, displaying particle information, and saving/loading simulation states.

- The simulation renders the particles on the Pygame screen, with particle colors reflecting their kinetic energy. Additional information about particles, such as velocity, mass, charge, energy, momentum, and temperature, can be displayed if enabled.
  
If you have any questions or encounter any issues, please feel free to reach out or open an issue in this repository.
