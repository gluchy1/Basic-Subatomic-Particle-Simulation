
# Particle Simulation Documentation

## Introduction

Welcome to the documentation for the Particle Simulation project. This project provides a platform for visualizing the behavior of subatomic particles under gravitational and electrostatic forces. It offers control over simulation parameters and the ability to save and load simulation states for further analysis. Feel free to explore and modify the code to suit your needs!

## Installation

To run the Particle Simulation, you need to have Python and the required dependencies installed. Follow the steps below to get started:

1.  Clone the project repository from GitHub: [GitHub - gluchy1/Basic-Subatomic-Particle-Simulation](https://github.com/gluchy1/Basic-Subatomic-Particle-Simulation)
2.  Navigate to the project directory.
3.  Install the required dependencies by running the following command in your console:
    
    `pip install -r requirements.txt` 
    

## Project Overview

The Particle Simulation project consists of the following files and directories:

-   `main.py`: This is the entry point of the simulation. Run this file to start the simulation.
-   `app/`: This directory contains the simulation logic and utility functions.
    -   `simulation.py`: This file contains the main logic of the particle simulation.
    -   `config.py`: This file contains configuration settings for the simulation.
    -   `particle.py`: This file defines the Particle class and its methods.
-   `requirements.txt`: This file lists the required Python dependencies for the project.

## Usage

To run the Particle Simulation, follow these steps:

1.  Make sure you have installed the required dependencies as mentioned in the Installation section.
2.  Open a terminal or command prompt and navigate to the project directory.
3.  Run the following command to start the simulation:
    
    
    `python gui.py` 
    
    Or without a GUI, in the `/app/` folder:
    
    `python main.py` 
    

Once the simulation window opens, you can interact with it using the following controls:

-   Press the Space key to pause/resume the simulation.
-   Press the R key to reset the simulation.
-   Use the E and D keys to increase/decrease the electrostatic force.
-   Use the G and F keys to increase/decrease the gravity force.
-   Press the I key to toggle the display of particle information.
-   Press the S key to save the simulation state.
-   Press the L key to load a saved simulation state.

## Simulation Logic

The Particle Simulation is based on the interaction between particles, including gravitational and electrostatic forces. The main loop of the simulation handles events, updates particle positions, and renders the particles on the screen.

The simulation follows these steps:

1.  Initialize the Pygame library and set up the simulation environment.
2.  Create a space for the particles using the Pymunk physics engine.
3.  Handle user events, such as keyboard inputs and window close events.
4.  Update the positions and forces of the particles based on the simulation parameters.
5.  Render the particles on the screen using Pygame's drawing functions.
6.  Display simulation information, such as particle count, simulation space, and control instructions.
7.  Repeat the above steps until the user exits the simulation.

## Particle Class

The Particle class represents a subatomic particle in the simulation. It has the following properties and methods:

### Properties:

-   `body`: A Pymunk Body object representing the physical properties of the particle.
-   `shape`: A Pymunk Shape object representing the shape of the particle.

### Methods:

-   `get_energy()`: Calculates the kinetic energy of the particle.
-   `get_momentum()`: Calculates the momentum of the particle.
-   `get_temperature()`: Calculates the temperature of the particle.
-   `get_larmor_radius(magnetic_field_strength)`: Calculates the Larmor radius of the particle in a given magnetic field.
-   `get_de_broglie_wavelength()`: Calculates the De Broglie wavelength of the particle.
-   `get_boltzmann_distribution(energy, temperature)`: Calculates the Boltzmann distribution for a given energy and temperature.
-   `get_thermal_conductivity(other_particle, distance)`: Calculates the thermal conductivity between two particles.

## Utility Functions

The `simulation.py` file contains utility functions used in the simulation:

-   `electrostatic_force(particle1, particle2)`: Calculates the electrostatic force between two particles.
-   `van_der_waals_force(particle1, particle2)`: Calculates the van der Waals force between two particles.
-   `save_simulation_state(space, filename)`: Saves the current simulation state to a file.
-   `load_simulation_state(filename)`: Loads a saved simulation state from a file.
-   `handle_collision(arbiter)`: Handles collision events between particles and walls.
-   `create_walls(space)`: Creates the walls that form the boundaries of the simulation.
-   `reset_simulation(space, particles)`: Resets the simulation by removing existing particles and creating new ones.

## Additional Information

You can find the complete source code and documentation for the Particle Simulation project on GitHub: [GitHub - gluchy1/Basic-Subatomic-Particle-Simulation](https://github.com/gluchy1/Basic-Subatomic-Particle-Simulation)

If you have any questions or suggestions, feel free to reach out to gluchy1 on GitHub.

**Note:** This project serves as a learning experience for coding and is treated as a main structure for learning purposes.
