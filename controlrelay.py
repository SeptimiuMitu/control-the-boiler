#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# global variables
GPIO_PIN=18
def set_gpio ():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN,GPIO.OUT)

#trigger the bistable. it needs the change from high to low to switch state.
def trigger_bistable_relay(gpio_pin):
    GPIO.output(GPIO_PIN,GPIO.HIGH)
    GPIO.output(GPIO_PIN,GPIO.LOW)

#turn on the relay.
def trigger_relay_on():
    GPIO.output(GPIO_PIN,GPIO.HIGH)
    logger.info("control relay trigger_relay_on")

def trigger_relay_off():
    GPIO.output(GPIO_PIN,GPIO.LOW)
    logger.info("control relay trigger_relay_off")
def main():
    set_gpio()
    trigger_relay_on()
    sleep(10)
    trigger_relay_off()

if __name__=="__main__":
    main()
