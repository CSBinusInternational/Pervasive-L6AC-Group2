# Pervasive-L6AC-Group2

Title: Pervasive Alarm Security System (P.A.S.S)

Scenario: When people leave their valuables somewhere inside a room, either it is in a familiar or unfamiliar condition, something unexpected could happen to their belongings. Either it is burglary, pranks, or other unwanted situations which can affect their valuables’ state.

Problem:  People need to have a way to feel at ease and stay alert at the same time while leaving their valuables inside a closed room, especially one that has doors. 

Design: The design of the system will enable user or owner to get notified if there was something unexpected happen to the room (for example, people managed to get in even though the door was locked). We are using magnetic sensor attached to the door to detect whether the door is opened/closed, camera to take images of the door condition should it change, buzzer to sound and Raspberry Pi module to control all the modules to be joined together.

Hardware needed:
1 Raspberry Pi 3 Model B
1 Pi Noir Camera Version 2
1 Magnetic sensor
1 Buzzer (Model YL-44)
Male to Male cable jumpers (as needed)
Female to Female cable jumpers (as needed)
1 Converter cable HDMI (Male) to VGA (Female) (For setup)
1 Raspberry Pi 3 Model B Case

Setting: We will connect Raspberry Pi to Pi Noir camera, magnetic sensors, and the buzzer. If the magnetic sensors are triggered by movements resulting in distance change between them (in this case, opening the door from its closed/initial state), this event will then make the buzzer to sound and trigger the camera to take an image. The sound will notify people around the area, while the image taken will be sent to the owner’s e-mail address, notifying him/her that the door to the room has been opened. 

Framework and job description: 
1.	Sensing – Matthew
Configure sensors, set the connections for all modules
2.	Gateway – Adam
Configure camera and buzzer, set the connections for all modules
3.	Service – Claudia
Configure sending email and set the connections for all modules
