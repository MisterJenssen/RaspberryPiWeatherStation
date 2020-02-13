from gpiozero import Button

rain_sensor = Button(5)
rain_count = 0

def switched():
    global rain_count
    rain_count = rain_count + 1
    print("Times switched:" + str(rain_count))

while True:
    rain_sensor.when_pressed = switched