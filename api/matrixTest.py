import requests
from flask import request
import traceback
from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS


import re
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
import Adafruit_CharLCD as LCD
from multiprocessing import Process

    # # API USING BINARY NUMBER

def matrix(msg, cascaded=1, block_orientation=90, rotate=0):
    
    # create matrix device
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=cascaded or 1, block_orientation=block_orientation, rotate=rotate or 0)
    # debugging purpose
    print("[-] Matrix initialized")

    # print hello world on the matrix display
    # debugging purpose
    print("[-] Printing: %s" % msg)
    show_message(device, msg, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)

    
    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    # Example using a character LCD backpack.

    # Define LCD column and row size for 16x2 LCD.
def lcdAction(x):
        lcd_columns = 16
        lcd_rows    = 2


        # Initialize the LCD using the pins
        lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)


        try:
            # Turn backlight on
            lcd.set_backlight(0)

            # Print a two line message
            lcd.message(x)

        except KeyboardInterrupt:
            # Turn the screen off
            lcd.clear()
            lcd.set_backlight(1)
            

if __name__=='__main__':
    try:
        matrix("Hello")
    except KeyboardInterrupt:
        pass

