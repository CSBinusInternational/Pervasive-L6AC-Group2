# Pervasive-L6AC-Group2

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
1.	Sensing – Matthew
Setting Raspberry, sensor, and camera so they can connect and work properly
2.	Gateway – Adam
Setting Raspberry, sensor, and camera so they can connect and work properly
3.	Service – Claudia
This layer involves figuring out how the data is gathered from all layers, stored and/or passed to the user and provide data insights.
