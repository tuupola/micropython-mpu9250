# Changelog

All notable changes to this project will be documented in this file, in reverse chronological order by release.

## 0.2.0 - 2018-04-08
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