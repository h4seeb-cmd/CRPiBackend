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


def lcdOn(x):
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
            