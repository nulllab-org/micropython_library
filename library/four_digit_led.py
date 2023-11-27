from i2c_device import I2cDevice
import struct


class FourDigitLed:
    DEFAULT_I2C_ADDRESS: int = 0x70
    HT16K33_CMD_BLINK: int = 0x80
    HT16K33_CMD_BRIGHTNESS: int = 0xE0
    HT16K33_BLINK_DISPLAY_ON: int = 0x01
    COLON_BUFFER_POSITION: int = 2
    DIGIT_NUMBER: int = 4

    NUMBER_TABLE = (
        0x3F,  # 0
        0x06,  # 1
        0x5B,  # 2
        0x4F,  # 3
        0x66,  # 4
        0x6D,  # 5
        0x7D,  # 6
        0x07,  # 7 
        0x7F,  # 8
        0x6F,  # 9
        0x77,  # A
        0x7C,  # b
        0x39,  # C
        0x5E,  # d
        0x79,  # e
        0x71,  # F
    )

    def __init__(self, i2c, i2c_address=DEFAULT_I2C_ADDRESS) -> None:
        self._i2c_device = I2cDevice(i2c_address=i2c_address, i2c=i2c)
        self._i2c_device.write_bytes(0x21)
        self.buffer = [0, 0, 0, 0, 0]
        self.clear()
        self.blink_rate(0)
        self.brightness(14)

    def blink_rate(self, blink_rate) -> None:
        self._i2c_device.write_bytes(FourDigitLed.HT16K33_CMD_BLINK |
                                     FourDigitLed.HT16K33_BLINK_DISPLAY_ON |
                                     (blink_rate << 1))

    def brightness(self, brightness: int) -> None:
        self._i2c_device.write_bytes(FourDigitLed.HT16K33_CMD_BRIGHTNESS |
                                     brightness)

    def clear(self) -> None:
        for i in range(len(self.buffer)):
            self.buffer[i] = 0x00
        self._show()

    def show_colon(self, show: bool) -> None:
        self.buffer[2] = show << 1
        self._i2c_device.write_bytes(0x04, struct.pack("<H", self.buffer[2]))

    def show_digit_number(self, position, number, dot: bool) -> None:
        if position >= FourDigitLed.COLON_BUFFER_POSITION:
            position += 1

        self.buffer[position] = FourDigitLed.NUMBER_TABLE[number] | (dot << 7)

        self._i2c_device.write_bytes(position << 1,
                                     struct.pack("<H", self.buffer[position]))

    def show_number(self, number, base=10, fractional_part_digits=2) -> None:
        if not isinstance(number, (int, float)):
            raise TypeError("number be of type int or float")

        if base != 10:
            fractional_part_digits = 0

        if isinstance(number, (int)):
            fractional_part_digits = 0

        numeric_digits = FourDigitLed.DIGIT_NUMBER
        # available digits on display

        is_negative: bool = False

        if number < 0:
            numeric_digits -= 1
            number = -number
            is_negative = True

        limit_value = 1
        for i in range(numeric_digits):
            limit_value *= base

        to_int_factor = 1.0
        for i in range(fractional_part_digits):
            to_int_factor *= base

        display_number = int(number * to_int_factor + 0.5)
        while display_number >= limit_value:
            fractional_part_digits -= 1
            to_int_factor /= base
            display_number = int(number * to_int_factor + 0.5)

        if to_int_factor < 1:
            self._show_error()
            return

        position = FourDigitLed.DIGIT_NUMBER

        index = 0
        while index <= fractional_part_digits or display_number > 0 or position == FourDigitLed.DIGIT_NUMBER:
            display_decimal = (fractional_part_digits != 0 and
                               index == fractional_part_digits)
            self.buffer[position] = FourDigitLed.NUMBER_TABLE[int(
                display_number % base)] | (display_decimal << 7)
            position -= 1
            if (position == FourDigitLed.COLON_BUFFER_POSITION):
                position -= 1
            display_number = int(display_number / base)
            index += 1

        if is_negative:
            self.buffer[position] = 0x40
            position -= 1

        while position >= 0:
            self.buffer[position] = 0x00
            position -= 1

        self._show()

    def _show_error(self):
        for i in range(len(self.buffer)):
            self.buffer[i] = 0x40
        self.buffer[FourDigitLed.COLON_BUFFER_POSITION] = 0x00
        self._show()

    def _show(self) -> None:
        data = bytearray([0x00])
        for i in range(len(self.buffer)):
            data += struct.pack("<H", self.buffer[i])
        self._i2c_device.write_bytes(data)
