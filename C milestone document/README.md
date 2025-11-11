# Our Super Awesome Project - ISS Deorbit Project

## Live Document Links
Tasks Planning Document - [Source](https://docs.google.com/spreadsheets/d/173YS2rmjjUFR3-em32RshCD2co25l5qMrgn1TTljqvA/edit?usp=sharing)

## Description

Nasa plans to address the issue that the ISS is reaching the end of its working lifetime. The chosen solution is to plan a safe, controlled re-entry of the spacecraft, however, NASA needs to simulate this re-entry. We strive to solve this problem through simulating the reentry in 4 phases. 

### Background

Due to the constant dynamic loads and thermal changes that the ISS faces, its constituent components, including modules, radiators, and truss structures, have a limited technical lifetime. As the working lifetime of these components comes to an end, NASA must consider what to do with the ISS. Possible options include disassembly and return to Earth, boosting to higher orbit, natural orbital decay with random re-entry, and controlled targeted re-entry. NASA has determined that the safest and most cost-effective plan is to conduct a controlled, targeted re-entry into a remote ocean area. This method strikes a good balance between cost-effectiveness and safety: it avoids the large propellant requirements of orbital boosting or disassembly and return, while intentional control of the deorbit location drastically reduces the risk of collision with infrastructure and people. Our project strives to simulate the controlled, targeted reentry of the ISS through 4 phases, orbital decay, final burn, re-entry trajectory, and rocket trajectory. We will be utilizing a numerical simulation for this project. This is a computational approach that approximates the behavior of complex systems using numerical methods and mathematical models. It allows us to study equations and physical systems that are too complex for exact analytical solutions. Euler’s method is a foundational technique that will be integrated in this simulation. This technique is used to solve ordinary differential equations. It works by using the tangent at a known point to estimate the value of the function at the next point, gradually replacing the curve with a straight-line approximation.
[Source](https://www.3d-scantech.com/solution/numerical-simulation/)
[Source](https://tutorial.math.lamar.edu/classes/de/eulersmethod.aspx) 

The scientific principles behind our project are: 
- Orbital decay: The gradual decrease in the altitude of a satellite's orbit over an extended period of time, resulting in a decline from its original stable position. [Source](https://taylorandfrancis.com/knowledge/Engineering_and_technology/Engineering_support_and_special_topics/Orbital_decay/)


- LEO (Low Earth Orbit): An orbit around the Earth with an altitude that lies towards the lower end of the range of possible orbits. 
[Source](https://www.space.com/low-earth-orbit)


- Deorbit: The act or process of deliberately leaving an orbital path, especially when a spacecraft is made to descend from its orbit, either to return to Earth or to eventually burn up in the atmosphere. 
[Source](https://www.dictionary.com/browse/deorbit)


- Controlled re-entry: Where the re-entry point is actively controlled to ensure that large fragments that survive re-entry do not pose an unacceptable hazard to people on the ground. 
[Source](https://www.sciencedirect.com/science/article/abs/pii/S0094576524006143)

### Features

Our project is able to simulate the deorbit of the ISS by dividing the proces into 4 smaller, manageable stages. Each represents a portion of the process with differing external variables and forces. The program allows initial conditions to be chosen for each stage of the product, which allows the effect small scale changes at any portion of the process to be clearly scene.

## Usage

### [Role 1] - Orbital Decay

The use of the program requires the input of an initial altitude, velocity, and the length of simualtion. The order of input is as follows:
* Initial Altitude: This is the height of the station above the earth, in the simulation it is treated as initial y position. (Given in kilometers)
* Velocity: This is the initial velocity of the station, all in the x direction, in the simulation it is treated as initial x velocity. (Given in meters per second)
* Length of the simuation: How long the user wants the program to simulate for. (Given in minutes)

Note: The example of the orbital_decay program has an initial altitude of 400 km, velocity of 7670 m/s, and runs for 90 minutes.

At the end of the simulation the program returns a list of the x-positions, y-positions, x-velocities, y-velocities, and time, for each iteration of the simulation. Additionally, it creates a plot of the x and y positions of the station. 

### [Role 2] - Final Burn

the program allows user to simulate the final burn of the phase of the rocket, plotting the x and y coordinates for the iss, some inputs value are recquired for the simulation to be optimal, altitude of the iss, the initial velocity of which the rocket is travling and how long the simulation will last is recquired. 

altitude: this is the height of the iss, which the altitude + the radius of the earth is the initial y coordinate of the ISS

velocity: this is the speed at which the iss is travelling in tangent to the earth, or in simple terms, the linear component of the orbital speed of the ISS, which is denoted as the initial speed in the x direction

time: this is an indicator on how long the  simulation will last, measured in minutes.

the output of the simulation will display the orbital path of the ISS on a x-y coordinate map, allowing the user to visualize the process of the final burn of the ISS.

### [Role 3] - Reentry Trajectory

Upon providing the initial altitude and x- and y-velocity parameters, this program is ran by pressing the play button while in the "reentry.py" file. 

For this milestone, the reentry trajectory and simulation depend entirly on the initial altitude and initial x and y velocity. Data can be input by altering the initial altitude and its units, and the initial velocity parameters in the "reentry.py" file. Ensure that after altering the parameters, the data is saved. These parameters appear as follows:
* Initial altitude = 130 
* Input units = 'km'
* Initial x-velocity = 7800 m/s 
* Initial y-velocity = 0 m/s 

In regards to the output, the simulation should output time, position, and velocity as list data types. It should also plot the x- and y- position of the mass. In this section these assumptions should be made:
- Drag is negligible.
- The ISS and deorbit vehicle remain docked for the duration of the descent.
- The simulation stops when the mass reaches zero altitude.
It will be apparent that the program ran succesfully if it outputs eveything previously outlined.

### [Role 4] - Rocket Trajectory

Given standard rocket parameters, and initial height, and an initial velocity, this program will run a 1D simulation of a rocket trajectory using explicit Euler's method. The program will output a lists of the rockets velocity and height, as well as times corresponding to these values. The program will then graph height vs time. The program will also return the maximum height of the rocket.

## Testing

### Orbital Decay testing:

### Final Burn testing:

### Reentry testing:
The reentry testing file checks the major components of the ISS reentry simulation, including unit conversions, how to handle invalid inputs - such as negative step sizes - and condiditons for the ISS to maintain orbit or escape orbit, and conditions for the ISS to impact the ground. The testing file utilizes strings to verify whether the program is running correctly, returning status messages such as "hit ground" or "invalid tstep value" based off the inputs. The file "test_reentry.py" is what executes the testing, printing "Test Passed" with the expected output, or "Test Failed" with the expected output and actual output. The provided tests in the file cover:
- ISS orbit and impact behavior: verifies using an expected outcome for different initial altitudes, velocities, and directions.
- Unit conversions: kilometers, meters, centimeters, feet, miles, and invalid unit inputs
- Input validation: ensures negative or zero "tstep" and "max_steps" values produce the correct error messages
- Edge cases: tests were included for an initial altitude of zero, very large time steps - "tstep" - and small and zero "max_steps" values.

To know a testing function output is correct the output line should state, "Test Passed". A "Test Failed" line suggests there is either an error in the function causing it to produce the wrong value, or the expected value is incorrect.

In Phase 2 for this simulation component, it may be beneficial to update the main() function to check the simulator's "status" before plotting to prevent the output of meaningless data. Additionally, setting the status strings as constants at the top of the file could minimize accidental typos between the code and test file. Regarding the function's output, it would be useful to create  means of distinguishing between the ISS maintaining orbit and it escaping orbit, currently they are grouped as one status rather than two. The function could also be improved to simulate actual physics, with an updated Eulers method that adjusts gravity's influence based off the ISS's position/altitude.

### Rocket Trajectory testing:
To test the simulated rocket trajectory, the initial velocity and initial height were both set to zero (the provided initial conditions). Then, the trajectory was evaluated by looking at the slope of the graph and how its magnitude and direction changed with time. 
### Previous testing overview (could be removed)
Testing our programs was an extremely involved process that required significant research to develop the domain knowledge necessary for creating effective test cases. Through this research and several calculations, we developed a series of cases that differed only by the values of a single variable to isolate its effect on the program’s output. We created successful and failing test cases to verify the program’s behavior and ensure that it handled all conditions correctly. Additionally, we focused on achieving  path coverage by designing our tests to ensure they exercised every possible execution path, allowing us to validate the logic and reliability of the code under all scenarios.

## Roadmap

In Phase 2 we plan to combine the programs from the four individual stage of the deorbit process into one cohesive program that remains highly responsive to changes in forces, conditions, and other external variables. Additionally, we aim to refine the program and improve the clarity of the resulting plots to greatly improve readability and overall quality.

## Authors and Acknowledgment
Authors: Justin Fu, Reid Korva, Pierson Jones, Rohan Deshmukh

