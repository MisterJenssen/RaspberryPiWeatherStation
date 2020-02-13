#!/usr/bin/python

import wiringpi2
import time

wiringpi2.wiringPiSetupGpio()

pinAnemometer = 9

wiringpi2.pinMode(pinAnemometer, 0)

x = 0

while x==0:

	result = wiringpi2.digitalRead(pinAnemometer)

	print result

	time.sleep(0.1)
