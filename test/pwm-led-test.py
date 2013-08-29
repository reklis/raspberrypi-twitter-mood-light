#!/usr/bin/python

import time
import RPi.GPIO as GPIO

# Common Cathode RGB-LEDs
RGB_ENABLE = 1
RGB_DISABLE = 0
 
# LED CONFIG - Set GPIO Ports
# http://www.hobbytronics.co.uk/image/data/tutorial/raspberry-pi/gpio-pinout.jpg

RED_PIN   = 11  # GPIO 17
GREEN_PIN = 13  # GPIO 21
BLUE_PIN  = 15  # GPIO 22
LED_PINS = [RED_PIN, GREEN_PIN, BLUE_PIN]

# global pwm handles
PWM_FREQUENCY = 60 # update frequency in Hz
 
def led_setup():
  # Set up the wiring
  GPIO.setmode(GPIO.BOARD)

  # Setup pins 
  GPIO.setup(RED_PIN, GPIO.OUT)
  GPIO.setup(GREEN_PIN, GPIO.OUT)
  GPIO.setup(BLUE_PIN, GPIO.OUT)

  # initialize the pulse handles
  RED_PWM = GPIO.PWM(RED_PIN, PWM_FREQUENCY)
  GREEN_PWM = GPIO.PWM(GREEN_PIN, PWM_FREQUENCY)
  BLUE_PWM = GPIO.PWM(BLUE_PIN, PWM_FREQUENCY)
  
  # start pulse width at a duty cycle of 0 (off)
  RED_PWM.start(0)
  GREEN_PWM.start(0)
  BLUE_PWM.start(0)

  return [RED_PWM, GREEN_PWM, BLUE_PWM]
 
def led_cleanup(rgb_pwm):
  rgb_pwm[0].stop()
  rgb_pwm[1].stop()
  rgb_pwm[2].stop()

def led_show_rgb(rgb_pwm, rgb_color):
  r = (rgb_color >> 16) & 0xFF
  g = (rgb_color >> 8) & 0xFF
  b = rgb_color & 0xFF
  
  rgb_pwm[0].ChangeDutyCycle(100 * r / 255)
  rgb_pwm[1].ChangeDutyCycle(100 * g / 255)
  rgb_pwm[2].ChangeDutyCycle(100 * b / 255)
 
def main():
  try:
    rgb_pwm = led_setup()


    red = 0xFF0000 
    orange = 0xFF7F00 
    yellow = 0xFFFF00 
    green = 0x00FF00 
    blue = 0x0000FF 
    indigo = 0x4B0082 
    violet = 0x8F00FF 

    color_bands = [red, orange, yellow, green, blue, indigo, violet]
  
    for rgb_color in color_bands:
      led_show_rgb(rgb_pwm, rgb_color)
      time.sleep(3)
  
    led_cleanup(rgb_pwm)

  except Exception as ex:
    print ex
    GPIO.cleanup()
  
main()
