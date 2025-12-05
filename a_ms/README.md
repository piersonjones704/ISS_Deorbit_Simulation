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

This project is a numerical simulation - provided by the Runge Kutta method - of the deorbit of the ISS given a set of initial conditions. The simulation is divided into four distinct stages each represented by a function call:
1. orbital_decay
2. final_burn
3. reentry
4. rocket

Each stage models a different portion of the process with differing external variables and forces. The functions are called sequentially, with the final position and velocity of each being used as the initial condition of the subsequent function, excluding rocket which has initial conditions provided by function parameters.

The program calls 4 functions, orbital_decay, final_burn, reentry, and rocket (in that order), with each representing a different portion of the process with differing external variables and forces. Each portion of the simulation uses the final position and velocity of the preeceding part as initial conditions, with the exception of rocket which has initial conditions determined in the function parameters, resulting in a full deorbit simulation.

Each stage represents a portion of the process with differing external variables.

Our project is able to simulate the deorbit of the ISS by dividing the proces into 4 smaller, manageable stages. Each represents a portion of the process with differing external variables and forces. The program allows initial conditions to be chosen for each stage of the product, which allows the effect small scale changes at any portion of the process to be clearly scene.

## Usage

The use of the program requires the input of an initial ISS altitude, velocity, orbital decay simulation duration, final burn simulation duration, rocket altitude, rocket launch velocity, and rocket launch simulation time. The order of input is as follows:
* Initial Altitude: This is the height of the station above the earth, in the simulation it is treated as initial y position. (Given in kilometers)
* Velocity: This is the initial velocity of the station, all in the x direction, in the simulation it is treated as initial x velocity. (Given in meters per second)
* Orbital Decay Simulation Duration: How long the user wants the orbital decay component to run for. (Given in minutes)
* Final Burn Simuation Duration: How long the user wants the final burn component to run for. (Given in minutes)
* Initial Rocket Altitude: This is the height the rocket launch begins at (Given in kilometers)
* Initial Rocket Launch Velocity: The initial velocity of the rocket when it is launched (Given in meters per second)
* Rocket Launch Simulation Duration: How long the rocket launch portion of the simulation should run (calculated based on additional factors such as wet mass, dry mass, and rocket exhaust mass flow rate)

### [Role 1] - Orbital Decay
The orbital decay acceleration function corresponds to the second phase of the ISS simulation. It takes two parameters in the following order:
1. A 1D position array given as [x-pos,y-pos] 
2. A 1D velocity array given as [x-velo,y-velo]
The orbital decay acceleration function returns a 1D accelerationa array given as [x-accel,y-accel].

The orbital decay phase uses the Runge-Kutta method and 3 paramters taken from extraneous calculations:
1. A 1D position array given as [x-pos,y-pos]
2. A 1D velocity array given as [x-velo,y-velo]
3. A timestep
The orbital decay phase updates the simulation's 2D position and velocity arrays with 1D arrays of the position, [x,y] and velocity, [Vx,Vy] for every timestep of the simulation.

### [Role 2] - Final Burn

Similar to the previous milestone, the final burn function is corresponded to the second phase of the whole function. the final burn function takes four parameters:

* final position of the ISS (x and y coordinate) from stage 1 as the initial position of stage 2
* final velocity (x and y components) from stage 1 as the initial velocity of stage 2
* final burn simulation time, which is responsible for controlling how long this portion of the simulation is ran 
* tstep, which is responsible for controlling the interval at which data is calculated and plotted 

### [Role 3] - Reentry Trajectory

Similar to the previous milestone, the reentry function corresponds to the third phase of the whole simulation. It takes three parameters:

* final position of the ISS (x and y coordinate) from the final burn stage as the initial position for this stage
* final velocity (x and y components) from the final burn stage as the initial velocity for this stage
* tstep, which is responsible for controlling the interval at which data is calculated and plotted 
* max_steps which is responsible for controlling how long this portion of the simulation is ran 

With the input of these parameters, the function will run, simulating the reentry trajectory of the ISS. Unlike the previous milestone, this reentry component will simulate the ISS's travel until it reaches an altitude of 100 km. Once it reaches this alitutde, it will model the ISS and truss separating during its descent. With the separation of these components the truss's position and velocity will be calculated and plotted to its point of impact.

### [Role 4] - Rocket Trajectory

Given standard rocket parameters (wet mass, mass ratio, mass flow rate, surface area, drag coefficient, and specific impulse), an initial height, and an initial velocity, this program will run a 1D simulation of a rocket trajectory using a second order Runge-Kutta simulation. The program plugs these inital parameters into a function that calculates the acceleration of the rocket based on the net force on the rocket and the changing mass, and outputs a lists of the rockets velocity and height, as well as times corresponding to these values. The program will then graph height vs time. 

## Testing

### Orbital Decay, Final Burn, and Reentry Testing

The full testing file checks each components of the ISS simulation, including how to handle invalid inputs - such as negative step sizes - and condiditons for the ISS to maintain orbit or escape orbit, and conditions for the ISS to impact the ground. 

The testing file utilizes strings to verify whether the program is running correctly, returning status messages such as "hit ground" or "invalid tstep value" based on the inputs. These strings are integrated throughout the full simulation function for every stage, except for "Rocket Trajectory." This is because orbital decay, final burn, and reentry are the stages of the ISS's deorbit, while the rocket's launch trajectory is a separate stage from the ISS's position and velocity during its deorbit - "Rocket Trajectory" will get its own testing overview. These strings are validated by determining whether the altitude ever reaches zero during the function to output a "hit ground" status or a "orbiting or escaped orbit" status if it did not make impact. The file "test_A_ms_simulation.py" executes the testing, printing "Test Passed" with the expected output or "Test Failed" with the expected output and the actual output. The provided tests in the file cover:
- ISS orbit and impact behavior: verifies using an expected outcome for different initial altitudes and velocity.
- Input validation: ensures negative or zero "tstep" values produce the correct error messages
- Edge cases: tests were included for an initial altitude of zero and very large time steps - "tstep" - values.

To know that a testing function output is correct, the output line should state, "Test Passed". A "Test Failed" line suggests there is either an error in the function, causing it to produce the wrong value, or the expected value is incorrect.

### Rocket Trajectory Testing

To test the rocket trajectory, the slope of the graph was evaluated and compared to the burn time. For example, at the end of the burn time, the slope of the graph should stop increasing and start decreasing, demonstrating a change in direction of net force from up to down due to loss of thrust. In addition, with an initial height and velocity of zero, the inital height of the rocket as represented on the graph should be zero, and the line tangent to the graph at t = 0 should be horizontal. 

## Roadmap

Our roadmap through this project can be split into three phases so far: background research, individual stages coding and final integration. 

During the background research stage, our background research focused on the foundation of domain knowledge for an ISS deorbit milestone by explaining what the ISS is, why and how it will be decommissioned, the key safety and physical considerations involved, and the scientific principles—laws, forces, trajectories, and numerical methods—needed for each role to model the deorbit process accurately. 

Through this background research, we then divided each section to a designated member to write code for each individual stage of the iss deorbit simulation, which includes orbital decay, final burn, reentry trajectory and the rocket trajectory stages. we then coded each simulation using the parameters given and imported matplotlib to plot our individual simulation. 

After completing our assigned task for simulation, we then approached the final integration of individual simulation in a full simulation file. Similar to the chronological order describe in the previous paragraph, the ISS first experience orbital decay with given initial prarmeters, then the final position and velocity output from orbital decay will then be the initial position and velocity input for the next stage - final burn, and so on. the final stage - rocket trajectory will then return a final position and velocity of the rocket, completing the simulation. 

Here, we reached the last step of the project where we use a higher order numerical method to better approximate the trajectory of the ISS station. this process is identical to the final integration of the individual simulation into a full simulation file. We utilised the Runge-Kunta method for a more optimal approximation using the higher order method.

## Authors and Acknowledgment

Authors: Justin Fu, Reid Korva, Pierson Jones, Rohan Deshmukh

## AI statement
No AI was used in the development of the code or the writing in the md file. 