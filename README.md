# Video capture from network camera

This simple script can be used to save a video from a network attached camera. It is pre-configured to work with the Axis cameras and the D-Link cameras. (The D-link cameras are the property of Tommy Alm (NFC).)

To use this the computer has to be connected to the same network as he cameras. The cameras have fixed IP:s (except for the Dlink DSC90 which has dynamic; check in router software what IP it got and change accordingly in code. This is annoying but the camera was not cooperative :-) ) 

Each camera has a web-interface that is reached by typing in the camera IP-adress into a web-browswer. 

Axis cams have username / password:

root / bildg

Dlink cams have username / password:

admin / [no password]

## Usage
> $ python3 vid-cap.py -c [camera] -o [output]

[output] is replaced by the desired output file-name.
You can do 
> $ python3 vid-cap.py -h

for brief help and list of options for [camera]. Also inspect the code to make sure IP-adresses are correct.

## Examples:
> $ python3 vid-cap.py -c axis1 -o vid-file

Above will save a file:
> $ vid-file.avi

To run multiple cameras simultaneously (with BASH):
> $ python3 vid-cap.py -c axis1 -o vid-file0 & python3 vid-cap.py -c axis2 -o vid-file1

This saves to video files using axis1 and axis2 cameras respectively.

## Requirements
Requires Python 3 and OpenCV

> $ pip install opencv-python
