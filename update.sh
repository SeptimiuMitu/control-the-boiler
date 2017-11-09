#!/bin/bash
echo updating the control-the-boiler based on Github
git -C /home/pi/control-the-boiler/ pull
python /home/pi/control-the-boiler/monitor.py
