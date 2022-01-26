#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import LED, time, math

x = 0
y = 0
width = 60
radius = 15
numLEDs = 4800
pixels = [ (0,0,0) ] * numLEDs
offset = 0
timer = 0

#time.sleep(2)
while True:
    for degree in range(360):
        offset+=0.0025
        degrees = math.radians(degree)
        radius = (degree+offset) % 30
        x = 40+math.floor(math.sin(degrees)*radius)
        y = 30+math.floor(math.cos(degrees)*radius)
        rainbow = LED.hsv2rgb(((degree+offset*6)*255/360) % 255,255,255)
        LED.draw_point(y,x,rainbow)#(degree % 255, 255, degree % 255))
        LED.draw_circle(30,40,math.sin(offset/20)*15+15,(0,0,0))
        #LED.set_brightness((math.sin(math.pi+offset/20)+1)/2+0.2)

    LED.draw()
        