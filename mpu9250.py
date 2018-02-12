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
from mpu6050 import MPU6050, ACCEL_FS_SEL_2G, GYRO_FS_SEL_250DPS
from ak8963 import AK8963

__version__ = "0.1.0-dev"

SF_G = 1
SF_M_S2 = 9.80665 # 1 g = 9.80665 m/s2 ie. standard gravity
SF_DEG_S = 1
SF_RAD_S = 57.295779578552 # 1 rad/s is 57.295779578552 deg/s

class MPU9250:
    """Class which provides interface to MPU9250 9-axis motion tracking device."""
    def __init__(
        self, i2c, address=0x68,
        accel_fs=ACCEL_FS_SEL_2G, accel_sf=SF_M_S2,
        gyro_fs=GYRO_FS_SEL_250DPS, gyro_sf=SF_RAD_S
    ):
        self.mpu6050 = MPU6050(
            i2c, address=0x68,
            accel_fs=accel_fs, accel_sf=accel_sf,
            gyro_fs=gyro_fs, gyro_sf=gyro_sf
        )
        self.ak8963 = AK8963(i2c)

    @property
    def acceleration(self):
        """
        Acceleration measured by the sensor. By default will return a
        3-tuple of X, Y, Z axis values in m/s^2 as floats. To get values in g
        pass `accel_fs=SF_G` parameter to the constructor.
        """
        return self.mpu6050.acceleration

    @property
    def gyro(self):
        """
        Gyro measured by the sensor. By default will return a 3-tuple of
        X, Y, Z axis values in rad/s as floats. To get values in deg/s pass
        `gyro_sf=SF_DEG_S` parameter to the constructor.
        """
        return self.mpu6050.gyro

    @property
    def magnetic(self):
        """
        X, Y, Z axis micro-Tesla (uT) as floats.
        """
        return self.ak8963.magnetic

    @property
    def whoami(self):
        return self.mpu6050.whoami

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        pass