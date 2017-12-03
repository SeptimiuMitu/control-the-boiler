#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
# global variables
gpio_pin=18
def set_gpio (gpio_pin):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio_pin,GPIO.OUT)

#trigger the bistable. it needs the change from high to low to switch state.
def trigger_bistable_relay(gpio_pin):
    GPIO.output(gpio_pin,GPIO.HIGH)
    GPIO.output(gpio_pin,GPIO.LOW)

#turn on the relay.
def trigger_relay_on(gpio_pin):
    GPIO.output(gpio_pin,GPIO.HIGH)

def trigger_relay_off(gpio_pin):
    GPIO.output(gpio_pin,GPIO.LOW)

def main():
    set_gpio(gpio_pin)
    trigger_relay_on(gpio_pin)
    sleep(10)
    trigger_relay_off(gpio_pin)
    
if __name__=="__main__":
    main()
