#!/usr/bin/python
import sys
import time
from astro_pi import AstroPi

X = [255, 0, 0]
O = [255, 255, 255]

question_mark = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

ap = AstroPi()

ap.set_pixels(question_mark)

ap.set_pixel(0, 0, 255, 0, 0)
ap.set_pixel(0, 7, 0, 255, 0)
ap.set_pixel(7, 0, 0, 0, 255)
ap.set_pixel(7, 7, 255, 0, 255)

while True:
    for r in [0, 90, 180, 270]:
        ap.set_rotation(r)
        time.sleep(.3)
