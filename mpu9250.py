#
# This file is part of MicroPython MPU9250 driver
# Copyright (c) 2018 Mika Tuupola
#
# Licensed under the MIT license:
#   http://www.opensource.org/licenses/mit-license.php
#
# Project home:
#   https://github.com/tuupola/micropython-mpu9250
#

"""
MicroPython I2C driver for MPU9250 9-axis motion tracking device
"""

import ustruct # pylint: disable=import-error
from machine import I2C, Pin # pylint: disable=import-error
from micropython import const # pylint: disable=import-error

_WHO_AM_I = const(0x75)

SF_G = 0.001 # 1 mg = 0.001 g
SF_SI = 0.00980665 # 1 mg = 0.00980665 m/s2

class MPU9250:
    """Class which provides interface to MPU9250 9-axis motion tracking device."""
    def __init__(self, i2c=None, address=0x68, sf=SF_SI):
        if i2c is None:
            self.i2c = I2C(scl=Pin(22), sda=Pin(21))
        else:
            self.i2c = i2c

        self.address = address

        if 0x71 != self.whoami:
            raise RuntimeError("MPU9250 not found in I2C bus.")

    @property
    def acceleration(self):
        """
        Acceleration measured by the sensor. By default will return a
        3-tuple of X, Y, Z axis acceleration values in m/s^2 as floats. Will
        return values in g if constructor was provided `sf=SF_G` parameter.
        """
        # # so = self._so
        # # sf = self._sf

        # # x = self._register_word(_OUT_X_L) * so * sf
        # # y = self._register_word(_OUT_Y_L) * so * sf
        # # z = self._register_word(_OUT_Z_L) * so * sf
        # return (x, y, z)
        pass

    @property
    def gyro(self):
        """
        x, y, z radians per second as floats
        """
        pass

    @property
    def orientation(self):
        """
        x, y, z degrees as floats
        """
        pass

    @property
    def whoami(self):
        """ Value of the whoami register. """
        return self._register_char(_WHO_AM_I)

    def _register_word(self, register, value=None):
        if value is None:
            data = self.i2c.readfrom_mem(self.address, register, 2)
            return ustruct.unpack("<h", data)[0]
        data = ustruct.pack("<h", value)
        return self.i2c.writeto_mem(self.address, register, data)

    def _register_char(self, register, value=None):
        if value is None:
            return self.i2c.readfrom_mem(self.address, register, 1)[0]
        data = ustruct.pack("<b", value)
        return self.i2c.writeto_mem(self.address, register, data)
