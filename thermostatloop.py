#!/usr/bin/env python
import time
import config
import gmailhelper
import os
import glob
import datetime
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('thermostatloop.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
# get temerature
# returns None on error, or the temperature as a float
def get_temp(devicefile):
    try:
        fileobj = open(devicefile,'r')
        lines = fileobj.readlines()
        fileobj.close()
    except:
        return None
    # get the status from the end of line 1
    status = lines[0][-4:-1]

    # is the status is ok, get the temperature from line 2
    if status=="YES":
        tempstr= lines[1][-6:-1]
        tempvalue=float(tempstr)/1000
        return tempvalue
    else:
        logger.error("thermostat loop get_temp error" + str(e))
        return None

# main function
def main():
    # enable kernel modules
    os.system('sudo modprobe w1-gpio')
    os.system('sudo modprobe w1-therm')

    # search for a device file that starts with 28
    devicelist = glob.glob('/sys/bus/w1/devices/28*')
    if devicelist=='':
        logger.error("thermostat loop device list empty - sensor not found")
        return None
    else:
        # append /w1slave to the device file
        w1devicefile = devicelist[0] + '/w1_slave'
    while True:
        temperature = get_temp(w1devicefile)
        if temperature == None:
            logger.error("thermostatloop error reading temperature")
            gmailhelper.send_gmail("error reading temperature" + datetime.now(),"")
        else:
            gmailhelper.send_gmail (temperature,"currenttemp")
            logger.info("thermostatloop sent temperature over email: " + str(temperature))
        time.sleep(300)

if __name__=="__main__":
    main()
