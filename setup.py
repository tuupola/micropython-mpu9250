import sys
sys.path.pop(0)
from setuptools import setup

setup(
    name="micropython-mpu9250",
    py_modules=["mpu9250", "mpu6500", "ak8963"],
    version="0.2.0",
    description="MicroPython I2C driver for MPU9250 9-axis motion tracking device",
    long_description="MPU-9250 is a System in Package (SiP) which combines two chips: MPU-6500 which contains 3-axis gyroscope and 3-axis accelerometer and an AK8963 which is a 3-axis digital compass.",
    keywords="accelerometer, gyro, magnetometer, micropython i2c",
    url="https://github.com/tuupola/micropython-mpu9250",
    author="Mika Tuupola",
    author_email="tuupola@appelsiini.net",
    maintainer="Mika Tuupola",
    maintainer_email="tuupola@appelsiini.net",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: MIT License",
    ],
)
