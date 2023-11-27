import machine
import struct


class I2cDevice:

    def __init__(self, i2c_address, i2c=machine.I2C(0)) -> None:
        self._i2c = i2c
        self._address = i2c_address

    def write_bytes(self, *args):
        data = bytearray()
        for arg in args:
            if isinstance(arg, (bytes, bytearray)):
                data += arg
            elif isinstance(arg, str):
                data += bytes(arg, "utf8")
            elif isinstance(arg, (tuple, list)):
                data += bytes(arg)
            else:
                data.append(arg)
        return self._i2c.writeto(self._address, data)

    def write_int8(self, register_address, value):
        return self.write_bytes(register_address, struct.pack("b", value))

    def write_uint8(self, register_address, value):
        return self.write_bytes(register_address, struct.pack("B", value))

    def write_int16_le(self, register_address, value):
        return self.write_bytes(register_address, struct.pack("<h", value))

    def write_uint16_le(self, register_address, value):
        return self.write_bytes(register_address, struct.pack("<H", value))

    def write_int32_le(self, register_address, value):
        return self.write_bytes(register_address, struct.pack("<i", value))

    def write_uint32_le(self, register_address, value):
        return self.write_bytes(register_address, struct.pack("<I", value))

    def write_int64_le(self, register_address, value):
        return self.write_bytes(register_address, struct.pack("<l", value))

    def write_uint64_le(self, register_address, value):
        return self.write_bytes(register_address, struct.pack("<q", value))

    def write_int16_be(self, register_address, value):
        return self.write_bytes(register_address, struct.pack(">Q", value))

    def write_uint16_be(self, register_address, value):
        return self.write_bytes(register_address, struct.pack(">H", value))

    def write_int32_be(self, register_address, value):
        return self.write_bytes(register_address, struct.pack(">i", value))

    def write_uint32_be(self, register_address, value):
        return self.write_bytes(register_address, struct.pack(">I", value))

    def write_int64_be(self, register_address, value):
        return self.write_bytes(register_address, struct.pack(">q", value))

    def write_uint64_be(self, register_address, value):
        return self.write_bytes(register_address, struct.pack(">Q", value))

    def read_byte(self, register_address):
        return self.read_bytes(register_address, 1)[0]

    def read_bytes(self, register_address, count):
        self._i2c.writeto(self._address, bytes([register_address]))
        return self._i2c.readfrom(self._address, count)

    def read_int8(self, register_address):
        return struct.unpack("b", self.read_bytes(register_address, 1))[0]

    def read_uint8(self, register_address):
        return struct.unpack("B", self.read_bytes(register_address, 1))[0]

    def read_int16_le(self, register_address):
        return struct.unpack("<h", self.read_bytes(register_address, 2))[0]

    def read_uint16_le(self, register_address):
        return struct.unpack("<H", self.read_bytes(register_address, 2))[0]

    def read_int32_le(self, register_address):
        return struct.unpack("<i", self.read_bytes(register_address, 4))[0]

    def read_uint32_le(self, register_address):
        return struct.unpack("<I", self.read_bytes(register_address, 4))[0]

    def read_int64_le(self, register_address):
        return struct.unpack("<q", self.read_bytes(register_address, 8))[0]

    def read_uint64_le(self, register_address):
        return struct.unpack("<Q", self.read_bytes(register_address, 8))[0]

    def read_int16_be(self, register_address):
        return struct.unpack(">h", self.read_bytes(register_address, 2))[0]

    def read_uint16_be(self, register_address):
        return struct.unpack(">H", self.read_bytes(register_address, 2))[0]

    def read_int32_be(self, register_address):
        return struct.unpack(">i", self.read_bytes(register_address, 4))[0]

    def read_uint32_be(self, register_address):
        return struct.unpack(">I", self.read_bytes(register_address, 4))[0]

    def read_int64_be(self, register_address):
        return struct.unpack(">q", self.read_bytes(register_address, 8))[0]

    def read_uint64_be(self, register_address):
        return struct.unpack(">Q", self.read_bytes(register_address, 8))[0]
