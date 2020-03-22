# MicroPython MPU-9250 (MPU-6500 + AK8963) I2C driver

MPU-9250 is a System in Package (SiP) which combines two chips: MPU-6500 which contains 3-axis gyroscope and 3-axis accelerometer and an AK8963 which is a 3-axis digital compass.

## Usage

Simple test with never ending loop.

```python
import utime
from machine import I2C, Pin
from mpu9250 import MPU9250

i2c = I2C(scl=Pin(22), sda=Pin(21))
sensor = MPU9250(i2c)

print("MPU9250 id: " + hex(sensor.whoami))

while True:
    print(sensor.acceleration)
    print(sensor.gyro)
    print(sensor.magnetic)
    print(sensor.temperature)

    utime.sleep_ms(1000)
```

By default the library returns 3-tuple of X, Y, Z axis values for either acceleration, gyroscope and magnetometer ie compass. Default units are `m/s^2`, `rad/s`, `uT` and `°C`. It is possible to also get acceleration values in `g` and gyro values `deg/s`. See the example below. Note that both the MPU6500 and the AK8963 drivers are available as separate classes. MPU9250 is actually a composite of those two.

```python
import utime
from machine import I2C, Pin
from mpu9250 import MPU9250
from mpu6500 import MPU6500, SF_G, SF_DEG_S

i2c = I2C(scl=Pin(22), sda=Pin(21))
mpu6500 = MPU6500(i2c, accel_sf=SF_G, gyro_sf=SF_DEG_S)
sensor = MPU9250(i2c, mpu6500=mpu6500)

print("MPU9250 id: " + hex(sensor.whoami))

while True:
    print(sensor.acceleration)
    print(sensor.gyro)
    print(sensor.magnetic)
    print(sensor.temperature)

    utime.sleep_ms(1000)
```

More realistic example usage with timer. If you get `OSError: 26` or `i2c driver install error` after soft reboot do a hard reboot.

```python
import micropython
from machine import I2C, Pin, Timer
from mpu9250 import MPU9250

micropython.alloc_emergency_exception_buf(100)

i2c = I2C(scl=Pin(22), sda=Pin(21))
sensor = MPU9250(i2c)

def read_sensor(timer):
    print(sensor.acceleration)
    print(sensor.gyro)
    print(sensor.magnetic)
    print(sensor.temperature)

print("MPU9250 id: " + hex(sensor.whoami))

timer_0 = Timer(0)
timer_0.init(period=1000, mode=Timer.PERIODIC, callback=read_sensor)
```

## Magnetometer Calibration

For real life applications you should almost always [calibrate the magnetometer](https://appelsiini.net/2018/calibrate-magnetometer/). The AK8963 driver supports both hard and soft iron correction. Calibration function takes two parameters: `count` is the number of samples to collect and `delay` is the delay in millisecods between the samples.

With the default values of `256` and `200` calibration takes aproximately one minute. While calibration function is running the sensor should be rotated multiple times around each axis.

NOTE! If using MPU9250 you will first need to open the I2C bypass access to AK8963. This is not needed when using a standalone AK8963 sensor.

```python
from machine import I2C, Pin
from mpu9250 import MPU9250
from ak8963 import AK8963

i2c = I2C(scl=Pin(22), sda=Pin(21))

dummy = MPU9250(i2c) # this opens the bybass to access to the AK8963
ak8963 = AK8963(i2c)
offset, scale = ak8963.calibrate(count=256, delay=200)

sensor = MPU9250(i2c, ak8963=ak8963)
```

After finishing calibration the `calibrate()` method also returns tuples for both hard iron `offset` and soft iron `scale`. To avoid calibrating after each startup it would make sense to strore these values in NVRAM or config file and pass them to the AK8963 constructor. Below example only illustrates how to use the constructor.

```python
from machine import I2C, Pin
from mpu9250 import MPU9250
from ak8963 import AK8963

i2c = I2C(scl=Pin(22), sda=Pin(21))
dummy = MPU9250(i2c) # this opens the bybass to access to the AK8963

ak8963 = AK8963(
    i2c,
    offset=(-136.8931640625, -160.482421875, 59.02880859375),
    scale=(1.18437220840483, 0.923895823933424, 0.931707933618979)
)

sensor = MPU9250(i2c, ak8963=ak8963)
```

## Gyro Calibration

TODO

## License

The MIT License (MIT). Please see [License File](LICENSE.txt) for more information.