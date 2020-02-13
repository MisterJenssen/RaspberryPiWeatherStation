#!/usr/bin/python

import wiringpi2
import time

wiringpi2.wiringPiSetupGpio()

pinRainGauge = 5

wiringpi2.pinMode(pinRainGauge, 0)

x = 0

while x==0:

	result = wiringpi2.digitalRead(pinRainGauge)

	print result

	time.sleep(1)
