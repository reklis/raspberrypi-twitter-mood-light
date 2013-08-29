#!/usr/bin/python

import time
import RPi.GPIO as GPIO
 
#Setup Active states
#Common Cathode RGB-LEDs
RGB_ENABLE = 1
RGB_DISABLE = 0
 
# LED CONFIG - Set GPIO Ports
# http://www.hobbytronics.co.uk/image/data/tutorial/raspberry-pi/gpio-pinout.jpg
RGB_RED   = 11  # GPIO 17
RGB_GREEN = 13  # GPIO 21
RGB_BLUE  = 15  # GPIO 22
RGB = [RGB_RED, RGB_GREEN, RGB_BLUE]
 
def led_setup():
  # Set up the wiring
  GPIO.setmode(GPIO.BOARD)
  # Setup Ports
  for val in RGB:
    GPIO.setup(val, GPIO.OUT)
 
def led_activate(colour):
  GPIO.output(colour, RGB_ENABLE)
 
def led_deactivate(colour):
  GPIO.output(colour, RGB_DISABLE)
 
def led_clear():
  for val in RGB:
    GPIO.output(val, RGB_DISABLE)
 
def main():
  led_setup()
  led_clear()

  led_activate(RGB_RED)
  time.sleep(5)
  led_deactivate(RGB_RED)
  time.sleep(5)

  led_activate(RGB_GREEN)
  time.sleep(5)
  led_deactivate(RGB_GREEN)
  time.sleep(5)

  led_activate(RGB_BLUE)
  time.sleep(5)
  led_deactivate(RGB_BLUE)
  time.sleep(5)

  led_clear()
  GPIO.cleanup()
  
main()
