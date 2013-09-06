## raspberrypi-twitter-mood-light

A mood light for twitter indented to be run on the raspberry pi


### Dependencies

- [Tweepy](https://github.com/tweepy/tweepy)
- [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)

### Minimum Installation

- Install Tweepy and RPi with pip
- Clone this repo
- Go get your own keys from http://dev.twitter.com and put them in the config.py
- sudo ./stream.py

[If you need help setting up wifi read this](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/setting-up-wifi-with-occidentalis)

### boot launch

If you want the program to start automatically, you'll need to compile the C launcher, setuid and schedule it
    
    # install the start script
    # might want to double check the paths in here
    sudo cp init.d/moodlight /etc/init.d/moodlight

    # add it as the last thing to run
    sudo update-rc.d moodlight defaults 99
 
    # reboot 
    sudo shutdown -r now

Note: Be aware streaming from twitter and analyzing tweets does use a lot of CPU and network.  If you've added it to startup, be patient as it will likely cause subsequent ssh connections to be very slowm, you'll want to stop the script to do any remote administative work.  It seems to run at around 30-40% cpu depending on tweet volume, and it may be best to do [a bit of light overclocking](http://lifehacker.com/5944867/overclock-a-raspberry-pi-without-voiding-your-warranty).


### Shopping List

You have a couple of options for the wiring.
I chose the cheap route and went with a lower power common cathode RGB LED.
It works fine and is bright enough, but if you have the money, you'd probably get better results with a few transistors and using the 5V rail.
I've included schematics and parts lists for each.

##### Standard Raspberry Pi setup

If you are reading this, you probably already have most of this

- [Raspberry Pi](http://amzn.com/B009SQQF9C)
- [SD Card](http://amzn.com/B003VNKNEG)
- [RPi Case](http://www.adafruit.com/products/1326)
- [USB Micro Cable](http://www.adafruit.com/products/592)
- [5V 1A USB power supply](http://www.adafruit.com/products/501)
- [Mini Wifi module](http://www.adafruit.com/products/814)

NB: if you have an extra iPhone or iPad charger laying around, check the rating, it will work just fine if it says 5V 1A and you can save some money. Also if you've got some extra cash, there are better cases that allow headroom for the jumper cables.  This one is cheap and will require some dremeling.

##### Common Cathode Schematic (cheaper, less work)

![common cathode](/schematic/common-cathode-rgbled.png "Using a common cathode RGB LED drawing all power from the GPIO pins")

##### Common Cathode Parts List

- [Breadboard - Mini Modular](https://www.sparkfun.com/products/11662)
- [Jumper Wires Premium 6" M/M Pack of 10](https://www.sparkfun.com/products/8431)
- [Jumper Wires Premium 6" M/F Pack of 10](https://www.sparkfun.com/products/9140)
- [RGB Clear Common Cathode red 2, blue 3.2, green 3.2](https://www.sparkfun.com/products/105)
- [Resistor Kit - 1/4W](https://www.sparkfun.com/products/10969)
- [Acrylic Container](http://amzn.com/B000NE80GO)

##### Common Anode Schematic (brighter, more powerful)

![common anode](/schematic/common-anode-rgbled.png "Using a common cathode RGB LED drawing all power from the GPIO pins")

##### Common Anode Parts List

Instead of the above RGB LED you'll need this:

- [Common Anode RGB LED](http://www.jameco.com/webapp/wcs/stores/servlet/Product_10001_10001_2128500_-1)

And additionally, you'll need these:

- [NPN Bipolar Transistors PN2222](http://www.adafruit.com/products/756)

All the math on the schematic is using a Beta value of 75 based on the datasheet for those transistors.
If you use a different transistor, you'll need to adjust the resistor ohms to match.

##### Tools needed

- [A Dremel](http://amzn.com/B003TU0XFU)
- [Dremel Accessories](http://amzn.com/B002L3RUWA)
- [Robot Sheep Fur](http://amzn.com/B001SBI38G)
- [Finger Lacerators](http://amzn.com/B00006L38W)
- [Unicorn Breakfast Cereal](http://amzn.com/B00004WCCL)

### Hardware Assembly

Note the LED_PIN settings from the config.py

    LED_PINS = {
      'red': 11,      # GPIO 17
      'green': 13,    # GPIO 21
      'blue': 15      # GPIO 22
    }

Follow the schematics, you can use this picture as a guide:

![gpio pinout](http://www.hobbytronics.co.uk/image/data/tutorial/raspberry-pi/gpio-pinout.jpg "Raspberry Pi GPIO Pinout")

This isn't [J5](http://www.johnny-five.com/images/sc2/misc/j5_and_toronto.jpg) we are assembling here, it's just three wires and a route back to ground, but still, probably a good idea to double check everything.

These test scripts might be helpful if you are having trouble:

    test/rgb-led-test.py   # cycle through RED/OFF/GREEN/OFF/BLUE/OFF and terminate
    test/pwm-led-test.py   # cycle through some color bands, then prompt for a hex value

When testing PWM you can enter values at the prompt like so `0xFF00FF` and it will parse them as `0xRRGGBB` values [just like css](http://www.w3schools.com/cssref/css_colorsfull.asp).  This is good for finding the right colors for your config as each LED is different.  No RGB LED will produce web colors that match the codes you'll find, you will need to adjust them to match what you see.  Feel free to update `config.py` with your own color codes for things.

Once you get things the way you want them, there is a bit of jiggery pokery we need to do to get it to look more like a lamp and less like [one of those clear phones from the 80s](http://1.bp.blogspot.com/_HoZcnRbEDDA/THVV-zRm7JI/AAAAAAAABck/DxwUA1oUicY/s400/clearphone.jpg).

- Frost the acrylic
- Hide the wifi and power leds
- Dremel the pi case for the jumper wires
- Dremel out a hole for power cable
- Affix the mini breadboard to the top of the case
- Build and install the lampshade

You'll notice the jumper cables do not fit if you try to close that case.  You can use a different case or dremel holes in the top.  Your choice.

To hide the wifi and power leds on the RPi so they do not interfere with the mood light, you'll want to cover them up with a bit of electrical tape.

To build the lampshade, [follow these instructions and make a basic origami balloon](http://en.origami-club.com/fun/balloon/ballon/balloon.gif) and shove it right on top of the LED.  Works decently well with a 2 inch square piece of paper.

To frost the acrylic, scrub both the inside and outside of the container with some steel wool.  It takes a while, give it a good two minutes on each plane, trust me it's worth it to get a nice soft glow.  You don't need the top.

Once that's done, dremel or drill a tiny hole in the back corner for the power cable, and place gently on top of the RPi, it should fit nicely on a diagnanol.
