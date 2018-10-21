# Farm Aid Jr
## Inspiration
Inspired by the work of plantvillage.psu.edu and iita.org, we wanted to build an Arduino-based autonomous robot that can move in a farm environment without damaging existing plants or soil and use object detection to find crops and categorize them as diseased or healthy.

## What it does
It is a disease detection robot that autonomously moves around farms and reports the location of diseased plants.

## How we built it
I used the Smart Bot 3.0 kit, raspberry-pi for image streaming. The network camera is connected to the raspberry-pi, which in turn is connected to a mobile hotspot. The laptop is connected to the same hotspot. This allows for the network camera to stream to the computer. Then, we run the stream through a convolutional neural network based on mobilenet SSD (built on TensorFlow) and do the plant classification and identification in real-time. Then, we transmitted the stream through a network port to a Wix website through a desktop encoder (OBS).

## Challenges we ran into
Continuous live streaming from the raspberry-pi on to a Wix website was difficult at first. However, we were able to look at some of the in-depth documentation and figure out how to stream it through an encoder. Earlier, we tried using Google Vision and Video Intelligence API. However, due to network connectivity issues (as a lot of students were on the network at the venue), the program would crash. Eventually, we ended up replacing it with a pre-trained neural network from GitHub. We also wanted to map a crop field in a matrix. Changing the matrix representation dynamically and then adding it to the Wix platform was challenging too, especially since we got to that part later during the project. 

## Accomplishments that we're proud of
- We used a robotic kit for the first time and were able to assemble it and get it running fairly quickly. 
- For some of our teammates, it was the first time learning JS. By the end of the project, each of us was more confident in our JS skills than before.
- Learning WIX for the first time and being able to show a live stream on it.
- Taking part in a hackathon for the first time for some of our members.
- The diversity of our group. We are all from different universities (and even different countries) yet we made something useful together.


## What we learned
- JS
- Wix
- New libraries in python, especially the google API ones.
- Robotics for some members. Still, first time using the kit for everyone.
- Building on the strengths of each of our teammates.
- Friendship <3

## What's next for Farmaid Jr.
Some parts of the control and code will be used for the full version of Farmaid. If this prototype is successful, a larger robot can be designed for autonomous disease detection.
