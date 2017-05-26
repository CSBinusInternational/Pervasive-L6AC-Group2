# Pervasive Alarm Security System (P.A.S.S)
 
Group 2
Project Report
 
By:
Adam Halim Waskito – 1801439734
Claudia Yohanna Haliz – 1801442935
Matthew Brian Kharli - 1801436575
 
COMP6124 - Pervasive Computing
Class 2016/2017
Computer Science Program
BINUS International
Jakarta

![Pervasive Alarm Security System](Pervasive-L6AC-Group2/images/pass.JPG?raw=true "Pervasive Alarm Security System")
 
 
## PROJECT DESCRIPTION
 
The idea of this project emerges from thoughts such as, “What if people want, or even must leave their valuables in some room which is unfamiliar to them?” When people leave their valuables somewhere inside a room, either it is in a familiar or unfamiliar condition, something unexpected could happen to their belongings. Either it is burglary, pranks, or other unwanted situations which can affect their valuables’ state. However, the owners would not know if something is done to their things, and will only know about it later when they get back to the room.
 
From the previous scenario, we see that people need to have a way to feel at ease and stay alert at the same time while leaving their valuables inside a closed room, especially one that has doors. We would like to address and help to solve this issue, by creating a system which enables the user to get notified if there was something unexpected happen to the room (for example, people managed to get in even though the door was locked). 

Pervasive Alarm Security System, or P.A.S.S, is a system which can help people guard their belongings when they are left in a room while the owners are away. We are using magnetic sensor attached to the door, camera to take images of the door condition should it change, buzzer to sound and Raspberry Pi module to control all the modules to be joined together.

We will connect Raspberry Pi to Pi Noir camera, magnetic sensors, and the buzzer. If the magnetic sensors are triggered by movements resulting in distance change between them (in this case, opening the door from its closed/initial state), this event will then make the buzzer to sound and trigger the camera to take an image. The sound will notify people around the area, while the image taken will be sent to the owner’s e-mail address, notifying him/her that the door to the room has been opened. 
 
 
## COMPONENTS REQUIRED
 
The components required for this project are as follows:

1. Raspberry Pi 3 Model B x1
![Raspberry Pi](Pervasive-L6AC-Group2/images/components/raspberry.JPG?raw=true "Raspberry Pi")
2. Pi Noir Camera Version 2 x1
![Camera](Pervasive-L6AC-Group2/images/components/camera.JPG?raw=true "Camera")
3. Magnetic sensor x1
![Sensor](Pervasive-L6AC-Group2/images/components/sensor.JPG?raw=true "Sensor")
4. Buzzer (Model YL-44) x1
![Buzzer](Pervasive-L6AC-Group2/images/components/buzzer.JPG?raw=true "Buzzer")
5. Male to male cable jumpers (as needed)
![Male to Male Cable Jumpers](Pervasive-L6AC-Group2/images/components/malemale.JPG?raw=true "Male to Male Cable Jumpers")
6. Female to female cable jumpers (as needed)
![Female to Female Cable Jumpers](Pervasive-L6AC-Group2/images/components/femalefemale.JPG?raw=true "Female to Female Cable Jumpers")
7. HDMI (Male) to VGA (Female) converter cable (For setup) x1
![Converter Cable](Pervasive-L6AC-Group2/images/components/converter.JPG?raw=true "Converter Cable")
8. Raspberry Pi 3 Model B Case (Optional) x1
![Case](Pervasive-L6AC-Group2/images/components/case.JPG?raw=true "Case")

 
## HOW DOES IT WORK? 
 
This system works by turning on the Raspberry Pi and keeping track of all connections to the modules. The Raspberry Pi must be connected to power socket or power supply. When it is on, code for P.A.S.S will be automatically executed. It will load the libraries and start the modules’ functionalities. The assembly for the modules are put below in Circuit Diagram section. Quantity of the jumper cables to be used may vary, depending on how far you would like the position of the sensor to be positioned away from the Raspberry Pi.

Firstly, attach the magnetic sensors separately, one to the static side of the door and other to the door itself. Set the camera position to be of desired, preferably near the door enabling it to capture images of face (point it approximately to the height of human upper body). Turn on the Raspberry Pi, and it will run the code and load the libraries needed. The system is now ready. Initially, when the door is closed, the sensor will produce “CLOSED” as the output. Next, if the door is opened, it will trigger the sensor to change its output to be “OPEN”.

When the sensor status changes to “OPEN”, this will provoke actions from the camera, alarm and from the Raspberry. The camera will snap an image of the door’s condition and the alarm will sound for some time, Then the Raspberry will send an email to the owner’s email address with an attached image taken from the camera. This email can be accessed or opened from the user’s smartphone, so the owner is notified when the door is opened when it should not be able to open (locked), and if something happened to their left valuables inside the room. 

This system is applicable anywhere with a door system installed, not limited to a room only. With P.A.S.S, you can stay safe and alert at the same time without having to worry about your belongings left behind.


## CIRCUIT DIAGRAM
 
Connect the camera to the Raspberry Pi as follows:
Camera module to camera port on Raspberry Pi.
 
Connect the sensor to the Raspberry Pi as follows:
Pin 1 on the sensor to Ground pin 9 on the Raspberry Pi.
Pin 2 on the sensor to GPIO27 pin 13 on the Raspberry Pi.
 
Connect the YL-44 buzzer to the Raspberry Pi as follows:
VCC on the YL-44 buzzer to 5V Power pin 2 on the Raspberry Pi.
I/O on the YL-44 buzzer to GPIO17 pin 11 on the Raspberry Pi.
GND on the YL-44 buzzer to Ground pin 6 on the Raspberry Pi.
 
The design of this project is as follows:
![Project Design](Pervasive-L6AC-Group2/images/components/Design.JPG?raw=true "Project Design")

PROJECT VIDEO
https://drive.google.com/open?id=0B4CU1OXYBdK3SjBmTDNTRWZfbnc
 
PROJECT CODING
https://github.com/claudiayhaliz/Pervasive-L6AC-Group2


## INDIVIDUAL WEEKLY PROGRESS
### Adam Halim Waskito – 1801439734
Week 1
Topic/Title: Smart Home Surveillance System
Setting: There are a lot of important things that people leave behind in their house when they want to go out, whether it is valuables, pet, or even children. Sometimes, people worry about the activities that are going on inside their house, or they just want to see what their pet is doing.
Problems or Issues: 
When people are outside of their house, they need a way to monitor the conditions inside their houses from afar.
Design:
To solve this problem that we have, we are going to make a home surveillance prototype.
We are using: 
- Raspberry Pi
- Micro SD card
- male-female Wire
- breadboard
- 2x Pi camera
Your Responsible:
Buying Raspberry Pi and learning how to utilize it.
 
Week 2: 
For this week, we are gathering the hardware for our final project. The hardware are:
1 x Raspberry Pi 3 Model B
1 x Raspberry Pi 3 Model B Case
1 x Raspberry Pi NOIR Camera V2
1 x Converter cable HDMI (Male) to VGA (Female)
Scenario: The camera will be connected to the Raspberry Pi and will receive inputs in the form of a video that will be stored on a server. Then, users could access the stream from a browser.
The items we ordered should arrive in three days. Other things maybe added to the project as we know more about the nature of our project.
Also, we have divided our group into three: Adam - Gateway
Claudia - Service
Matthew - Sensors
For next week, we will be connecting the hardware and figuring out how to transfer the data.
 
Week 3
For this week, I have gotten most of the parts needed for my team's final project for Pervasive Computing (which may change), and have connected the parts and learned the basic usage of the devices.
From what I've gathered from the internet, the camera could not only store pictures, but also videos.
Next Progress: Learning how to code using Python and how to operate the Raspberry Pi NOIR Camera using Python. Learn how to store videos into a server to be accessed by other devices.
![Week 3](Pervasive-L6AC-Group2/images/progress/week 3.JPG?raw=true "Week 3")

Week 4: Pivot - Changed project idea and specification, gather hardware
Our team decided to change our final project idea because we think the new one will be more applicable and useful to have. The project will still use Raspberry Pi and Pi camera, but the scenario is different.
Topic/title: Car Security Sensor
Scenario: When people park their cars on the parking lots even on the roadside, something unexpected could happen to their cars. Either it is burglary, pranks, unintentional car bumps, or other unwanted situations which can affect their cars' state. However, the owners would not know if something is done to their cars, and will only know about it later when they get there.
Problem: People need to have a way to feel at ease and stay alert at the same time while leaving their cars at stationary state anywhere.
Design: To solve this problem that we have, we are going to make a camera surveillance prototype which can take a picture if there is a vibration detected to the car. Then this picture will be forwarded to user, so the user will be notified with some information if something happened with his car. Initial design is attached and may change as we learn more about our project.
Hardware needed (other hardware components might be added as we learn more about our project):
1 Raspberry Pi 3 Model B
1 Raspberry Pi 3 Model B Case
1 Pi Noir Camera Version 2
1 Converter cable HDMI (Male) to VGA (Female)
1 Breadboard
Male-female wire
1 Vibration sensor SW420
Setting: We will connect Raspberry Pi to Pi Noir camera and vibration sensor. If the sensor was triggered by vibration or shock, the camera would capture and send a picture to the owner’s smartphone.
Framework and job description: 
1. Sensing – Matthew
Setting Raspberry, sensor, and camera so they can connect and work properly
2. Gateway – Adam
Setting Raspberry, sensor, and camera so they can connect and work properly
3. Service – Claudia
This layer involves figuring out how the data is gathered from all layers, stored and/or passed to the user and provide data insights
My responsibility: 
- Buy breadboard, wire and vibration sensor
- Figure out how to connect the hardware, how to transfer data from the camera to Raspberry, how to transfer data from Raspberry to user’s smartphone
Progress: 
- Acquired all hardware
- Tried connected Raspberry to Pi camera
- Tried connecting and code “blinking lights”
- Researched ways about how to send picture to user’s smartphone from Raspberry
Goals for next week: 
- Try to connect Raspberry with camera
- Find a mock model to put the camera on/in
	
Week 5 - Connect camera and add buzzer to project specification
What have been done: 
- Connect camera to Raspberry
- Changing project specification
- Adding buzzer component to system's functionality
Goals: 
- Connect vibration sensor to Raspberry
- Connect buzzer to sensor
- Try sending email from Raspberry so it can reach the user
 
Week 6 - Did research
What have been done:
-        Connect camera to Raspberry
Goals (Same as week 5):
-        Connect vibration sensor to Raspberry
-        Connect buzzer to sensor
-        Try sending email from Raspberry so it can reach the user
 
Week 7
After connecting our physical modules and implementing basic GPIO functions inside our code, we are currently working on getting the input from our vibration sensor. We have also successfully sent emails from the Raspberry Pi with attachments in them.
For the next stage, we are going to complete the sensor implementation for our project and compile them into a single .py file.
![Week 7](Pervasive-L6AC-Group2/images/progress/week 7.JPG?raw=true "Week 7")
 
Week 8
The sensor is changed to magnetic sensors, which consists of 2 separate small magnets. These magnets then will react and produce output based on changes of distance between them. The implementation of this change to our project is, when unexpected person comes and open the car door, this sensor will detect the change, snap a picture and send it to the car owner. We have successfully make the sensor to work by producing the expected output (The output is “CLOSE” if the magnets are attached to each other, and “OPEN” otherwise).
The code is up on our group’s GitHub repository. Next, we are going to connect the camera module along with the sensor.
![Week 8](Pervasive-L6AC-Group2/images/progress/week 8.JPG?raw=true "Week 8")
 
Week 9
We have been able to connect the sensor to camera module. What happens is when magnets of the magnetic sensor are far away from each other (Output: “OPEN”), the camera module will take a picture and save it in /pi directory.
We compile and test the code in a single .py file for next use. Our next plan is to connect the buzzer to current “connected” modules (camera and sensor) so it will activate the sound feature.
![Week 9](Pervasive-L6AC-Group2/images/progress/week 9.JPG?raw=true "Week 9")
![Week 9-2](Pervasive-L6AC-Group2/images/progress/week 9-2.JPG?raw=true "Week 9-2")

Week 10: We have finished the project.
Problem found and covered during project development:
We have problems during the process of trying the buzzer and sensor because we misunderstood some of the functions. In the end we handled all problems and finish this project.
 
### Claudia Yohanna Haliz – 1801442935
Week 1: Determining project specification
Topic/Title: Smart Home Surveillance System
Setting: There are a lot of important things that people leave behind in their house when they want to go out, whether it is valuables, pet, or even children. Sometimes, people worry about the activities that are going on inside their house, or they just want to see what their pet is doing.
Problems or Issues: When people are outside of their house, they need a way to monitor the conditions inside their houses from afar.
Design: To solve this problem that we have, we are going to make a home surveillance prototype which can monitor activities inside a place.
We are using: 
- Raspberry Pi 3 B+
- Micro SD card
- male-female Wire
- breadboard
- 2x Pi camera
My Responsibility: 
- Buying Pi Camera and learn what are needed to install it
- Research more to connect the system
 
Week 2: Updated project specification
Project title: Smart Home Video Surveillance System
Scenario: Pi Noir camera will act as the input device that can be put anywhere to monitor a particular place. We will connect the Pi Noir camera to Raspberry Pi, so that the camera can capture video and transfer it to the Raspberry. Then Raspberry will send the data to the user so the user can see the surveillance videos. (We are thinking the videos to be opened from browser, so the user can access it through their smartphones.)
Design: Attached. This is the initial design and may change as we learn more about our project.
Framework and job description:
1. Service - Claudia
This layer involves figuring out how the data is gathered, stored and passed to the user from Raspberry.
2. Gateway - Adam
This layer involves tweaking with the Raspberry and its connection with the camera.
3. Sensors - Matthew
This layer involves configuring the camera settings and connecting with the Raspberry.
Hardware needed (other hardware components might be added as we learn more about our project):
1 Raspberry Pi 3 Model B
1 Raspberry Pi 3 Model B Case
1 Pi Noir Camera Version 2
1 Converter cable HDMI (Male) to VGA (Female)
Progress: Acquiring all the components needed.
Target for next week:
- Configure Raspberry (Adam)
- Connect Raspberry with camera (Adam & Matthew)
- Figure out how to transfer the data from the camera to Raspberry (Claudia).
 
Week 3: Did research and gather hardware
So far I have learned the basic usage of the devices, get all necessary hardware for my team's project, connect pi camera to raspberry and learn that it is better to stream surveillance video through browser rather than to store it entirely because it will take huge space of data storage. The surveillance system will act as security measure to monitor a place's condition. Some motion sensors can also be implemented in the system triggering some events like sending notification to computer and store pictures.
For the goals, we will try the code to light up lamps and try to setup raspberry as webcam server to stream video through browser from raspberry.
![Week 3](Pervasive-L6AC-Group2/images/progress/week 3.JPG?raw=true "Week 3")

Week 4: Pivot - Changed project idea and specification, gather hardware
Our team decided to change our final project idea because we think the new one will be more applicable and useful to have. The project will still use Raspberry Pi and Pi camera, but the scenario is different.
Topic/title: Car Security Sensor
Scenario: When people park their cars on the parking lots even on the roadside, something unexpected could happen to their cars. Either it is burglary, pranks, unintentional car bumps, or other unwanted situations which can affect their cars' state. However, the owners would not know if something is done to their cars, and will only know about it later when they get there.
Problem: People need to have a way to feel at ease and stay alert at the same time while leaving their cars at stationary state anywhere.
Design: To solve this problem that we have, we are going to make a camera surveillance prototype which can take a picture if there is a vibration detected to the car. Then this picture will be forwarded to user, so the user will be notified with some information if something happened with his car. Initial design is attached and may change as we learn more about our project.
Hardware needed (other hardware components might be added as we learn more about our project):
1 Raspberry Pi 3 Model B
1 Raspberry Pi 3 Model B Case
1 Pi Noir Camera Version 2
1 Converter cable HDMI (Male) to VGA (Female)
1 Breadboard
Male-female wire
1 Vibration sensor SW420
Setting: We will connect Raspberry Pi to Pi Noir camera and vibration sensor. If the sensor was triggered by vibration or shock, the camera would capture and send a picture to the owner’s smartphone.
Framework and job description: 
1. Sensing – Matthew
Setting Raspberry, sensor, and camera so they can connect and work properly
2. Gateway – Adam
Setting Raspberry, sensor, and camera so they can connect and work properly
3. Service – Claudia
This layer involves figuring out how the data is gathered from all layers, stored and/or passed to the user and provide data insights
My responsibility: 
- Buy breadboard, wire and vibration sensor
- Figure out how to connect the hardware, how to transfer data from the camera to Raspberry, how to transfer data from Raspberry to user’s smartphone
Progress: 
- Acquired all hardware
- Tried connected Raspberry to Pi camera
- Tried connecting and code “blinking lights”
- Researched ways about how to send picture to user’s smartphone from Raspberry
Goals for next week: 
- Try to connect Raspberry with camera
- Find a mock model to put the camera on/in
![Week 4](Pervasive-L6AC-Group2/images/progress/week 4.JPG?raw=true "Week 4")

Week 5 - Connect camera and add buzzer to project specification
What have been done: 
- Connect camera to Raspberry
- Changing project specification
- Adding buzzer component to system's functionality
Goals: 
- Connect vibration sensor to Raspberry
- Connect buzzer to sensor
- Try sending email from Raspberry so it can reach the user
 
Week 6 - Did research
What have been done:
-        Connect camera to Raspberry
Goals (Same as week 5):
-        Connect vibration sensor to Raspberry
-        Connect buzzer to sensor
-        Try sending email from Raspberry so it can reach the user
 
Week 7
After connecting our physical modules and implementing basic GPIO functions inside our code, we are currently working on getting the input from our vibration sensor. We have also successfully sent emails from the Raspberry Pi with attachments in them.
For the next stage, we are going to complete the sensor implementation for our project and compile them into a single .py file.
![Week 7](Pervasive-L6AC-Group2/images/progress/week 7.JPG?raw=true "Week 7")
 
Week 8
The sensor is changed to magnetic sensors, which consists of 2 separate small magnets. These magnets then will react and produce output based on changes of distance between them. The implementation of this change to our project is, when unexpected person comes and open the car door, this sensor will detect the change, snap a picture and send it to the car owner. We have successfully make the sensor to work by producing the expected output (The output is “CLOSE” if the magnets are attached to each other, and “OPEN” otherwise).
The code is up on our group’s GitHub repository. Next, we are going to connect the camera module along with the sensor.
![Week 8](Pervasive-L6AC-Group2/images/progress/week 8.JPG?raw=true "Week 8")
 
Week 9
We have been able to connect the sensor to camera module. What happens is when magnets of the magnetic sensor are far away from each other (Output: “OPEN”), the camera module will take a picture and save it in /pi directory.
We compile and test the code in a single .py file for next use. Our next plan is to connect the buzzer to current “connected” modules (camera and sensor) so it will activate the sound feature.
![Week 9](Pervasive-L6AC-Group2/images/progress/week 9.JPG?raw=true "Week 9")
![Week 9-2](Pervasive-L6AC-Group2/images/progress/week 9-2.JPG?raw=true "Week 9-2")
 
Week 10
Finally, finally the system is complete! We tried the modules one by one until we managed to connect them all into a single system. We have also compiled the test scripts for each individual module into a single python file. There were some errors happening at first trials (such as the buzzer sounds as soon as the Raspberry Pi is on, the sensors do not work as we would like it to be, and setting the camera position to be able to precisely capture a whole door’s image) but we managed to go through it all. I personally think that there are rooms for improvements that can be made to this project as we still learn, this project can *really* happen because of my team! Thanks and great job guys!
 
Problem found and covered during project development: 
Finding project’s idea → Discussion
Not sure how things will work, the components and its structures → Research and brainstorming
Sensor testing → Configure the timing
Buzzer testing → Figure out that we had the wrong function to use as the output
Connecting all modules and pack them into a single container → Replace sensors position, set camera position, use small-sized box
 
### Matthew Brian Kharli - 1801436575
Week 1
Topic/Title: Smart Home Surveillance System
Setting: There are a lot of important things that people leave behind in their house when they want to go out, whether it is valuables, pet, or even children. Sometimes, people worry about the activities that are going on inside their house, or they just want to see what their pet is doing.
Problems or Issues: When people are outside of their house, they need a way to monitor the conditions inside their houses from afar.
Design: To solve this problem that we have, we are going to make a home surveillance prototype which can monitor activities inside a place.
We are using: 
- Raspberry Pi 3 B+
- Micro SD card
- male-female Wire
- breadboard
- 2x Pi camera
My Responsibility: 
- Buying Pi Camera and learn what are needed to install it
- Research more to connect the system
 
Week 2
For now, we are trying to find these following modules: 1 x raspberry pi, 1 x wifi shield, 1 x camera
We have divided our group into three:
Adam - Gateway
Claudia - Service
Matthew - Sensors
 
Week 3
We have gathered most of the parts needed for the team's final project in Pervasive Computing, and have connected the parts also learned the basic usage of the devices.
Next progress: Learning on how to code and operate the Raspberry Pi NOIR Camera using Python.
![Week 3](Pervasive-L6AC-Group2/images/progress/week 3.JPG?raw=true "Week 3")

Week 4: Pivot - Changed project idea and specification, gather hardware
Our team decided to change our final project idea because we think the new one will be more applicable and useful to have. The project will still use Raspberry Pi and Pi camera, but the scenario is different.
Topic/title: Car Security Sensor
Scenario: When people park their cars on the parking lots even on the roadside, something unexpected could happen to their cars. Either it is burglary, pranks, unintentional car bumps, or other unwanted situations which can affect their cars' state. However, the owners would not know if something is done to their cars, and will only know about it later when they get there.
Problem: People need to have a way to feel at ease and stay alert at the same time while leaving their cars at stationary state anywhere.
Design: To solve this problem that we have, we are going to make a camera surveillance prototype which can take a picture if there is a vibration detected to the car. Then this picture will be forwarded to user, so the user will be notified with some information if something happened with his car. Initial design is attached and may change as we learn more about our project.
Hardware needed (other hardware components might be added as we learn more about our project):
1 Raspberry Pi 3 Model B
1 Raspberry Pi 3 Model B Case
1 Pi Noir Camera Version 2
1 Converter cable HDMI (Male) to VGA (Female)
1 Breadboard
Male-female wire
1 Vibration sensor SW420
Setting: We will connect Raspberry Pi to Pi Noir camera and vibration sensor. If the sensor was triggered by vibration or shock, the camera would capture and send a picture to the owner’s smartphone.
Framework and job description: 
1. Sensing – Matthew
Setting Raspberry, sensor, and camera so they can connect and work properly
2. Gateway – Adam
Setting Raspberry, sensor, and camera so they can connect and work properly
3. Service – Claudia
This layer involves figuring out how the data is gathered from all layers, stored and/or passed to the user and provide data insights
My responsibility: 
- Buy breadboard, wire and vibration sensor
- Figure out how to connect the hardware, how to transfer data from the camera to Raspberry, how to transfer data from Raspberry to user’s smartphone
Progress: 
- Acquired all hardware
- Tried connected Raspberry to Pi camera
- Tried connecting and code “blinking lights”
- Researched ways about how to send picture to user’s smartphone from Raspberry
Goals for next week: 
- Try to connect Raspberry with camera
- Find a mock model to put the camera on/in
	
Week 5 - Connect camera and add buzzer to project specification
What have been done: 
- Connect camera to Raspberry
- Changing project specification
- Adding buzzer component to system's functionality
Goals: 
- Connect vibration sensor to Raspberry
- Connect buzzer to sensor
- Try sending email from Raspberry so it can reach the user
 
Week 6 - Did research
What have been done:
-        Connect camera to Raspberry
Goals (Same as week 5):
-        Connect vibration sensor to Raspberry
-        Connect buzzer to sensor
-        Try sending email from Raspberry so it can reach the user
 
Week 7
After connecting our physical modules and implementing basic GPIO functions inside our code, we are currently working on getting the input from our vibration sensor. We have also successfully sent emails from the Raspberry Pi with attachments in them.
For the next stage, we are going to complete the sensor implementation for our project and compile them into a single .py file.
![Week 7](Pervasive-L6AC-Group2/images/progress/week 7.JPG?raw=true "Week 7")
 
Week 8
The sensor is changed to magnetic sensors, which consists of 2 separate small magnets. These magnets then will react and produce output based on changes of distance between them. The implementation of this change to our project is, when unexpected person comes and open the car door, this sensor will detect the change, snap a picture and send it to the car owner. We have successfully make the sensor to work by producing the expected output (The output is “CLOSE” if the magnets are attached to each other, and “OPEN” otherwise).
The code is up on our group’s GitHub repository. Next, we are going to connect the camera module along with the sensor.
![Week 8](Pervasive-L6AC-Group2/images/progress/week 8.JPG?raw=true "Week 8")
 
Week 9
We have been able to connect the sensor to camera module. What happens is when magnets of the magnetic sensor are far away from each other (Output: “OPEN”), the camera module will take a picture and save it in /pi directory.
We compile and test the code in a single .py file for next use. Our next plan is to connect the buzzer to current “connected” modules (camera and sensor) so it will activate the sound feature.
![Week 9](Pervasive-L6AC-Group2/images/progress/week 9.JPG?raw=true "Week 9")
![Week 9-2](Pervasive-L6AC-Group2/images/progress/week 9-2.JPG?raw=true "Week 9-2")
 
Week 10
We have finished the project successfully, although there are problems during the implementation when we wanted to connect all the components, we solved them by doing more research and tweak the modules.
Problem found and covered during project development:
Configuring sensor, we solve this by doing more research about the module. Configuring buzzer, also solved by doing research. When connecting all components, we did it step-by-step so the script can work properly.

