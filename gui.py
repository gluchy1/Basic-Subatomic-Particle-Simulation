from importlib.machinery import SourceFileLoader
from app.main import main

"""
This gui.py file is intended to be a feature for an user to give him ability to choose what type of simulation
he wants to run. Definitely it needs more work and polishing done, since it's very unstable, memory consuming 
and made in a wrong way.

The best case scenario would be to make a file that sets different values for Particle class instead of creating
a set of different Particle classes. This way it'd be more efficient without taking that much of a memory.
"""

DEFAULT_PARTICLE_FILE_PATH = "app/particle.py"

if __name__ == "__main__":
    desc = (f"\n"
            f"Choose option for particle simulation:\n"
            f"1 -- Default Particle (proper physics theories etc.)\n"
            f"2 -- Particle 2 (different)\n"
            f"3 -- Particle 3\n"
            f"4 -- Particle 4\n"
            f"5 -- Particle 5\n"            
            f"\n")

    particle_option = input(desc)
    particle_path = ""

    if particle_option == "1":
        particle_path = DEFAULT_PARTICLE_FILE_PATH
    elif particle_option == "2":
        particle_path = "app/options/particles-options/particle2.py"
    elif particle_option == "3":
        particle_path = DEFAULT_PARTICLE_FILE_PATH  # pass <-- rest yet to be implemented. Just testing some features.
    elif particle_option == "4":
        particle_path = DEFAULT_PARTICLE_FILE_PATH  # pass
    elif particle_option == "5":
        particle_path = DEFAULT_PARTICLE_FILE_PATH  # pass
    else:
        particle_path = DEFAULT_PARTICLE_FILE_PATH
        print("Incorrect option, choose (1-5). Setting the default and running the simulation...")

    Particle = SourceFileLoader("Particle", particle_path).load_module().Particle
    main()
