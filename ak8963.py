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
MicroPython I2C driver for AK8963 magnetometer
"""

import ustruct # pylint: disable=import-error
from machine import I2C, Pin # pylint: disable=import-error
from micropython import const # pylint: disable=import-error

_WIA = const(0x00)
_HXL = const(0x03)
_HXH = const(0x04)
_HYL = const(0x05)
_HYH = const(0x06)
_HZL = const(0x07)
_HZH = const(0x08)

class AK8963:
    """Class which provides interface to AK8963 magnetometer."""
    def __init__(self, i2c, address=0x0c):
        self.i2c = i2c
        self.address = address

        if 0x48 != self.whoami:
            raise RuntimeError("AK8963 not found in I2C bus.")

    @property
    def orientation(self):
        """
        x, y, z degrees as floats
        """
        return (0.0, 0.0, 0.0)

    @property
    def whoami(self):
        """ Value of the whoami register. """
        return self._register_char(_WIA)

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
