# Changelog

All notable changes to this project will be documented in this file, in reverse chronological order by release.

## [0.3.0](https://github.com/tuupola/micropython-mpu9250/compare/0.2.1...0.3.0) - 2020-03-22
### Added

- Support for internal temperature sensor ([#1](https://github.com/tuupola/micropython-mpu9250/issues/1), [#9](https://github.com/tuupola/micropython-mpu9250/pull/9), [#18](https://github.com/tuupola/micropython-mpu9250/pull/18))
- Support for gyro calibration ([#5](https://github.com/tuupola/micropython-mpu9250/issues/5), [#10](https://github.com/tuupola/micropython-mpu9250/pull/10))

### Fixed
- Support for standalone MPU6500 sensors ([#15](https://github.com/tuupola/micropython-mpu9250/issues/15), [#16](https://github.com/tuupola/micropython-mpu9250/pull/16))

### Changed

- Move I2C bypass initialisation from MPU6500 to MPU9250 ([#17](https://github.com/tuupola/micropython-mpu9250/issues/17))

## [0.2.1](https://github.com/tuupola/micropython-mpu9250/compare/0.2.0...0.2.1) - 2019-02-07
### Fixed
- Gyro degrees to radians conversion ([#8](https://github.com/tuupola/micropython-mpu9250/pull/8)).

## [0.2.0](https://github.com/tuupola/micropython-mpu9250/compare/0.1.0...0.2.0)- 2018-04-08
### Added
- Support for magnetometer factory sensitivity adjustement values `ASAX`, `ASAY` and `ASAZ`.
- Support for setting magnetometer offset and scale calibration values.
    ```
    ak8963 = AK8963(
        i2c,
        offset=(-136.8931640625, -160.482421875, 59.02880859375),
        scale=(1.18437220840483, 0.923895823933424, 0.931707933618979)
    )
    ```
- Method for retrieving the magnetometer offset and scale calibration values.
    ```
    ak8963 = AK8963(i2c)
    offset, scale = ak8963.calibrate(count=256, delay=200)
    ```

## 0.1.0 - 2018-02-17

Initial working release.