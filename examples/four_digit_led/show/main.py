import four_digit_led
import machine
import time

four_digit_led = four_digit_led.FourDigitLed(i2c=machine.I2C(0, scl=22, sda=21))

four_digit_led.show_number(1234)
time.sleep(0.5)

four_digit_led.show_number(98.76)
time.sleep(0.5)

four_digit_led.show_number(-99)
time.sleep(0.5)

four_digit_led.clear()
four_digit_led.show_digit_number(0, 0, True)
time.sleep(0.5)

four_digit_led.show_digit_number(1, 1, False)
time.sleep(0.5)

four_digit_led.show_digit_number(2, 2, True)
time.sleep(0.5)

four_digit_led.show_digit_number(3, 3, False)
time.sleep(0.5)

four_digit_led.show_colon(True)
time.sleep(0.5)

four_digit_led.show_colon(False)
time.sleep(0.5)
