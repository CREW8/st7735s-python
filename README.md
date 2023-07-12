# Python ST7735s

Python library to control multiple ST7735s TFT LCD display. Allows to display individual Gif's on each display.
Designed specifically to work with ST7735s based 128x160 pixel TFT SPI displays. (Specifically the 1.8" SPI LCD).

⚠️ This is a Hobby Project and not a production ready Library ⚠️

## Installing

### Python 3

Make sure you have the following dependencies:

````
sudo apt update
sudo apt install python3-rpi.gpio python3-spidev python3-pip python3-pil python3-numpy
````

Install this library by cloning the files from this repo.
See example of usage in the examples folder.


# Licensing & History

This library is a modification of a modification of code originally written by Tony DiCola for Adafruit Industries, and modified to work with the ST7735 by Clement Skau.

It has been modified by Pimoroni to include support for their 160x80 SPI LCD breakout, and hopefully also generalised enough so that it will support other ST7735-powered displays.

It has been further modified by CREW8 to control multiple ST7735s based 128x160 pixel TFT SPI displays.

## Modifications include:

* PIL/Pillow has been removed from the underlying display driver to separate concerns- you should create your own PIL image and display it using `display(image)`
* `width`, `height`, `rotation`, `invert`, `offset_left` and `offset_top` parameters can be passed into `__init__` for alternate displays
* `Adafruit_GPIO` has been replaced with `RPi.GPIO` and `spidev` to closely align with our other software (IE: Raspberry Pi only)
* Test fixtures have been added to keep this library stable
* ST7735s Support
* Multi-Display-Support

## Known Issues:

* Gif animations are pretty slow


Modified from 'Adafruit Python ILI9341' written by Tony DiCola for Adafruit Industries written by Clement Skau.

MIT license, all text above must be included in any redistribution
