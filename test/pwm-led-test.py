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
  for pwm in rgb_pwm:
    pwm.stop()

def led_show_rgb(rgb_pwm, rgb_color):
  r = (rgb_color >> 16) & 0xFF
  g = (rgb_color >> 8) & 0xFF
  b = rgb_color & 0xFF
  
  rgb_pwm[0].ChangeDutyCycle(100 * r / 255)
  rgb_pwm[1].ChangeDutyCycle(100 * g / 255)
  rgb_pwm[2].ChangeDutyCycle(100 * b / 255)

def led_change_brightness(rgb_pwm, freq):
  for pwm in rgb_pwm:
    pwm.ChangeFrequency(freq)
 
def main():
  try:
    rgb_pwm = led_setup()

    white = 0xFFB4B4
    pink = 0xFF005A
    orange = 0xFF2300
    yellow = 0xFF5005
    green = 0x00FF00
    blue = 0x0000FF
    magenta = 0xFF00FF

    color_bands = [white, pink, orange, yellow, green, blue, magenta]
  
    for rgb_color in color_bands:
      led_show_rgb(rgb_pwm, rgb_color)
      # for freq in range(1,60):
      #   led_change_brightness(rgb_pwm, freq)
      #   time.sleep(.3)
      # for freq in range(60,1):
      #   led_change_brightness(rgb_pwm, freq)
      #   time.sleep(.3)
  
    led_cleanup(rgb_pwm)

  except Exception as ex:
    print ex
    GPIO.cleanup()
  
main()
