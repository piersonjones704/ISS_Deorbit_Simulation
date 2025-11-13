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

Our project is able to realistically simulate the deorbit of the ISS by dividing the proces into 4 smaller, manageable stages. Each represents a portion of the process with differing external variables and forces. The program allows initial conditions to be chosen for each stage of the product, which allows the effect small scale changes at any portion of the process to be clearly seen. These 4 separate stages are integrated into a main file to provide a full simulation. Starting from launching the deorbit vehicle, to orbital decay of the ISS, to docking the deorbit vehicle, to reentry, this simulation models and visualizes the overall ISS deorbit.

## Usage

### [Role 1] - Orbital Decay


### [Role 2] - Final Burn


### [Role 3] - Reentry Trajectory


### [Role 4] - Rocket Trajectory


## Testing

Testing our programs was an extremely involved process that required significant research to develop the domain knowledge necessary for creating effective test cases. Through this research and several calculations, we developed a series of cases that differed only by the values of a single variable to isolate its effect on the program’s output. We created successful and failing test cases to verify the program’s behavior and ensure that it handled all conditions correctly. Additionally, we focused on achieving  path coverage by designing our tests to ensure they exercised every possible execution path, allowing us to validate the logic and reliability of the code under all scenarios.

## Roadmap


## Authors and Acknowledgment

Authors: Justin Fu, Reid Korva, Pierson Jones, Rohan Deshmukh
