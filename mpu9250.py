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
from mpu6050 import MPU6050, SF_SI, ACCEL_FS_SEL_2G
from ak8963 import AK8963

SF_G = 1
SF_SI = 9.80665 # 1 g = 9.80665 m/s2 ie. standard gravity

class MPU9250:
    """Class which provides interface to MPU9250 9-axis motion tracking device."""
    def __init__(self, i2c, address=0x68, accel_fs=ACCEL_FS_SEL_2G, sf=SF_SI):
        self.mpu6050 = MPU6050(i2c)
        self.ak8963 = AK8963(i2c)

    @property
    def acceleration(self):
        """
        Acceleration measured by the sensor. By default will return a
        3-tuple of X, Y, Z axis acceleration values in m/s^2 as floats. Will
        return values in g if constructor was provided `sf=SF_G` parameter.
        """
        return self.mpu6050.acceleration

    @property
    def gyro(self):
        """
        X, Y, Z axis radians per second as floats.
        """
        return self.mpu6050.gyro

    @property
    def orientation(self):
        """
        X, Y, Z axis degrees as floats.
        """
        return self.ak8963.orientation

    @property
    def whoami(self):
        return self.mpu6050.whoami
