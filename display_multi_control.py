# Copyright (c) 2014 Adafruit Industries
# Author: Phil Howard, Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# DISPLAY - RASPI
# VCC   -> 3.3V
# GND   -> GND
# CS    -> GPIO8
# RESET -> GPIO27
# A0    -> GPIO25
# SDA   -> GPIO10
# SCK   -> GPIO11
# LED   -> GPIO24

# Display GPIOs (Each CS Pin needs an individual GPIO)
DISPLAY_1 = 16
DISPLAY_2 = 5
DISPLAY_3 = 19
DISPLAY_4 = 1
DISPLAY_5 = 12
DISPLAY_6 = 6
DISPLAY_7 = 26
DISPLAY_8 = 13

from PIL import Image
import RPi.GPIO as GPIO
import ST7735
import time
import sys

# Setup help CS Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(DISPLAY_1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(DISPLAY_2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(DISPLAY_3, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(DISPLAY_4, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(DISPLAY_5, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(DISPLAY_6, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(DISPLAY_7, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(DISPLAY_8, GPIO.OUT, initial=GPIO.HIGH)

# Create TFT LCD display class.
GPIO.output(DISPLAY_1, 0)
disp = ST7735.ST7735(
    port=0,
    cs=ST7735.BG_SPI_CS_BACK,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
    dc=25,
    backlight=24,
    spi_speed_hz=4000000,
    rst=27,
    invert=False
)
width = disp.width
height = disp.height
GPIO.output(DISPLAY_1, 1)

# Setup Display 2
GPIO.output(DISPLAY_2, 0)
disp._init()
GPIO.output(DISPLAY_2, 1)

#Setup Display 3
GPIO.output(DISPLAY_3, 0)
disp._init()
GPIO.output(DISPLAY_3, 1)

#Setup Display 4
GPIO.output(DISPLAY_4, 0)
disp._init()
GPIO.output(DISPLAY_4, 1)

#Setup Display 5
GPIO.output(DISPLAY_5, 0)
disp._init()
GPIO.output(DISPLAY_5, 1)

#Setup Display 6
GPIO.output(DISPLAY_6, 0)
disp._init()
GPIO.output(DISPLAY_6, 1)

#Setup Display 7
GPIO.output(DISPLAY_7, 0)
disp._init()
GPIO.output(DISPLAY_7, 1)

#Setup Display 8
GPIO.output(DISPLAY_8, 0)
disp._init()
GPIO.output(DISPLAY_8, 1)



# Load an image.
print('Loading gifs:')
image_1 = Image.open("gifs/de_Museum.gif")
image_2 = Image.open("gifs/de_Heizung.gif")
image_3 = Image.open("gifs/de_Museum.gif")
image_4 = Image.open("gifs/de_Heizung.gif")
image_5 = Image.open("gifs/de_Museum.gif")
image_6 = Image.open("gifs/de_Heizung.gif")
image_7 = Image.open("gifs/de_Museum.gif")
image_8 = Image.open("gifs/de_Heizung.gif")
image_1_frame = 0
image_2_frame = 0
image_3_frame = 0
image_4_frame = 0
image_5_frame = 0
image_6_frame = 0
image_7_frame = 0
image_8_frame = 0

print('Drawing gifs, press Ctrl+C to exit!')



while True:
    # Display 1
    try:
        image_1.seek(image_1_frame)

        GPIO.output(DISPLAY_1, 0)
        disp.display(image_1.resize((width, height)))
        GPIO.output(DISPLAY_1, 1)

        image_1_frame += 1

    except EOFError:
        image_1_frame = 0

    # Display 2
    try:
        image_2.seek(image_2_frame)

        GPIO.output(DISPLAY_2, 0)
        disp.display(image_2.resize((width, height)))
        GPIO.output(DISPLAY_2, 1)

        image_2_frame += 1

    except EOFError:
        image_2_frame = 0

    # Display 3
    try:
        image_3.seek(image_3_frame)

        GPIO.output(DISPLAY_3, 0)
        disp.display(image_3.resize((width, height)))
        GPIO.output(DISPLAY_3, 1)

        image_3_frame += 1

    except EOFError:
        image_3_frame = 0

    # Display 4
    try:
        image_4.seek(image_4_frame)

        GPIO.output(DISPLAY_4, 0)
        disp.display(image_4.resize((width, height)))
        GPIO.output(DISPLAY_4, 1)

        image_4_frame += 1

    except EOFError:
        image_4_frame = 0

    # Display 5
    try:
        image_5.seek(image_5_frame)

        GPIO.output(DISPLAY_5, 0)
        disp.display(image_5.resize((width, height)))
        GPIO.output(DISPLAY_5, 1)

        image_5_frame += 1

    except EOFError:
        image_5_frame = 0

    # Display 6
    try:
        image_6.seek(image_6_frame)

        GPIO.output(DISPLAY_6, 0)
        disp.display(image_6.resize((width, height)))
        GPIO.output(DISPLAY_6, 1)

        image_6_frame += 1

    except EOFError:
        image_6_frame = 0

    # Display 7
    try:
        image_7.seek(image_7_frame)

        GPIO.output(DISPLAY_7, 0)
        disp.display(image_7.resize((width, height)))
        GPIO.output(DISPLAY_7, 1)

        image_7_frame += 1

    except EOFError:
        image_7_frame = 0

    # Display 8
    try:
        image_8.seek(image_8_frame)

        GPIO.output(DISPLAY_8, 0)
        disp.display(image_8.resize((width, height)))
        GPIO.output(DISPLAY_8, 1)

        image_8_frame += 1

    except EOFError:
        image_8_frame = 0

    time.sleep(0.01)
