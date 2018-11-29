# ass2

robotics ros assigment 2
in order to activate gazebo for this assigment use the command
 roslaunch assigment2 turtlebot3_bgu_world.launch 
in order to use the assigmnet use the command


assigment description:


(0) exit the program

(1) Move forward moves the robot forward 50cm if there is no obstacle that is closer than 50 cm. Otherwise, the robot does not move.

(2) Prompts for an angle alpha and turns around the robot in place alpha degrees clockwise.

(3) Distance to object with color X return the distance to an object with color X in the robot's current frame. If there is none, it returns NULL. You can assume there is a single object in the frame with each color.

(4) Find object with color X moves around autonomously while searching for an object with color X, then approach it up to 50 cm. Assume an object of the requested color will be in the room.

In (3) and (4) the robot awaits for a color to be typed from the terminal after it enters the appropriate function. 
