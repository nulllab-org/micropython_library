"""
This is a class for controlling an 8x8 LED matrix display.

The class provides methods for setting the brightness, showing custom LED patterns, displaying numbers and strings
on the display, clearing the display, and updating the display to show the content of the buffer.

The class uses an SPI object for communication with the display, and requires the chip select (CS) pin of the display
to be specified during initialization. The methods of this class must be called in the appropriate order to set up
the display and show the desired content.

Note: Make sure to import the required modules before using this class.
"""

import machine
from micropython import const
import framebuf
import time

_NOOP = const(0)
_DIGIT0 = const(1)
_DECODEMODE = const(9)
_INTENSITY = const(10)
_SCANLIMIT = const(11)
_SHUTDOWN = const(12)
_DISPLAYTEST = const(15)


class MatrixLed8x8:
    """
    Initializes the MatrixLed8x8 class with the specified SPI object and chip select (CS) pin.

    Args:
        spi: The SPI object used for communication with the MatrixLed8x8 display.
        cs: The chip select (CS) pin of the display.
    """

    def __init__(self, spi, cs) -> None:
        self.spi = spi
        self.cs = machine.Pin(cs, machine.Pin.OUT)
        self.cs(1)
        self.buffer = bytearray(8)
        self.frame_buffer = framebuf.FrameBuffer(self.buffer, 8, 8,
                                                 framebuf.MONO_HLSB)
        for command, data in (
            (_SHUTDOWN, 0),
            (_DISPLAYTEST, 0),
            (_SCANLIMIT, 7),
            (_DECODEMODE, 0),
            (_SHUTDOWN, 1),
        ):
            self._write(command, data)

    def brightness(self, value):
        """
        Sets the brightness of the MatrixLed8x8 display.

        Args:
            value: The brightness value. Must be an integer between 0 and 15 (inclusive).
        
        Raises:
            ValueError: If the brightness value is out of range.
        """
        if not 0 <= value <= 15:
            raise ValueError("Brightness out of range")
        self._write(_INTENSITY, value)

    def show_leds(self, pixels):
        """
        Shows a custom pattern of LEDs on the MatrixLed8x8 display.

        Args:
            pixels: A 2D list of pixel values. Each pixel value should be 0 (off) or 1 (on).

        Raises:
            ValueError: If the pixels array is not a valid size.
        """
        if len(pixels) != 8 or any(len(row) != 8 for row in pixels):
            raise ValueError("Invalid pixels array size")
        self.frame_buffer.fill(0)
        for y in range(0, len(pixels)):
            for x in range(0, len(pixels[y])):
                self.frame_buffer.pixel(x, y, pixels[y][x])
        self._show()

    def show_number(self, number: int):
        """
        Shows a number on the MatrixLed8x8 display.

        Args:
            number: The number to display.
        """
        self.show_string(str(number))

    def show_string(self, string: str):
        """
        Shows a string on the MatrixLed8x8 display.

        Args:
            string: The string to display.
        """
        if (len(string) == 1):
            self.frame_buffer.fill(0)
            self.frame_buffer.text(string, 0, 0)
            self._show()
        else:
            buffer = bytearray(8 * len(string))
            fb = framebuf.FrameBuffer(buffer, 8 * len(string), 8,
                                      framebuf.MONO_HLSB)
            fb.text(string, 0, 0)

            for step in range((len(string)) * 8 + 1):
                self.frame_buffer.fill(0)
                self.frame_buffer.blit(fb, -step, 0)
                self._show()

    def clear(self):
        """
        Clears the MatrixLed8x8 display.
        """
        self.frame_buffer.fill(0)
        self._show()

    def _write(self, command, data):
        """
        Sends a command and data to the MatrixLed8x8 display.

        Args:
            command: The command to send.
            data: The data to send.
        """
        self.cs(0)
        self.spi.write(bytearray([command, data]))
        self.cs(1)

    def _show(self):
        """
        Updates the display to show the content of the frame buffer.
        """
        for y in range(8):
            self.cs(0)
            self.spi.write(bytearray([_DIGIT0 + y, self.buffer[y]]))
            self.cs(1)
        time.sleep_ms(100)
