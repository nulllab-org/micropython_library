import matrix_led_8x8
import machine
import time

# Initialize SPI with the appropriate pins
spi = machine.SPI(1, sck=25, mosi=2)

# Initialize MatrixLed8x8 with the SPI object and chip select (CS) pin
matrix_led = matrix_led_8x8.MatrixLed8x8(spi=spi, cs=26)

# Set the brightness of the display
matrix_led.brightness(1)

# Define a custom LED pattern
leds = [
    [0, 1, 1, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

# Show the custom LED pattern on the display
matrix_led.show_leds(leds)
time.sleep(1)

# Show a number on the display
matrix_led.show_number(1)
time.sleep(1)

# Show a larger number on the display
matrix_led.show_number(9876)
time.sleep(1)

# Show a single character on the display
matrix_led.show_string("a")
time.sleep(1)

# Show a string on the display
matrix_led.show_string("hello")
time.sleep(1)

# Clear the display
matrix_led.clear()
