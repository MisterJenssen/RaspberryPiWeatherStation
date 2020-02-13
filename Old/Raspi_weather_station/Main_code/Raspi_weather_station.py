#!/usr/bin/python

# SOFTWARE
import sys
import Adafruit_BMP.BMP085 as BMP085
import Adafruit_DHT as DHT22

sensorBMP = BMP085.BMP085()
sensorDHT = DHT22.DHT22
pinDHT = 4

print 'BMP085:'
print 'Temp = {0:0.2f} *C'.format(sensorBMP.read_temperature())
print 'Pressure = {0:0.2f} Pa'.format(sensorBMP.read_pressure())
print 'Altitude = {0:0.2f} m'.format(sensorBMP.read_altitude())
print 'Sealevel Pressure = {0:0.2f} Pa'.format(sensorBMP.read_sealevel_pressure())
print ''
print 'DHT22:'
humidity, temperature = DHT22.read(sensorDHT, pinDHT)
print 'Temp = {0:0.2f} *C'.format(temperature) 
print 'Humidity = {0:0.2f} %'.format(humidity)