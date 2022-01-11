# Covid-19 Simulator

* Awarded 3rd place out of 45 competing teams at Carnegie Mellon University's 15-112 Hackathon. 
* This project was developed in collaboration with Jason Stentz, Andrew Thrasher, & Fayyad Zakaria

## Project Description:

Welcome to COVID-19 Simulator! 

With certain restrictions, the purpose of our program is to model the
the behavior of the spread of coronavirus amongst a group of individuals
over the course of a user's specified time.

We begin by populating a room with dots representing people. Each person is
described by their symptoms, whether or not they are infected, and if they have
masks.

Un-infected persons (green dots) will steer clear of infected (red dots) and
will have no negative behavior towards the asymptomatic (yellow dots). Both red
and yellow will infect green based upon social distancing and presence of masks.

**Modules Used:**
 - cmu_112_graphics

**To Run Program:**
 - Run the main.py file

## Instructions:

#### Mouse Presses:

##### When Building Room:
 - click where you want the top left corner of the room to be
 - then click where you want the bottom right corner to be (the order here can be flipped)
 - toggle 't' to place tables
    
##### When Adding People:
 - click on the screen to add people (can not add outside of room)
 - Use the popup menu to toggle your person's attributes and click "Submit"
 - Duplicate a desired player by clicking inside a person's circle.
        Then click to place the duplicated player.
    
##### Scaling Popup:
 - Toggle the simulation's scaling factor and speed with this popup menu
 - Click "Submit" on the scaling pop up to begin the simulation.

##### Key Presses:
- 'r'     => reset the simulation
- 'Escape'=> end the simulation and display results
- 'a'     => create/add and place a random person
- 'Up'    => Speed up time in the simulation
- 'Down'  => Slow down time in the simulation
- 't'     => Toggle tables in the simulation
