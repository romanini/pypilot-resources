# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the FXOS8700 accelerometer and magnetometer.
# Will print the acceleration and magnetometer values every second.
import time
import board
import adafruit_fxos8700
import math


# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_fxos8700.FXOS8700(i2c)
# Optionally create the sensor with a different accelerometer range (the
# default is 2G, but you can use 4G or 8G values):
# sensor = adafruit_fxos8700.FXOS8700(i2c, accel_range=adafruit_fxos8700.ACCEL_RANGE_4G)
# sensor = adafruit_fxos8700.FXOS8700(i2c, accel_range=adafruit_fxos8700.ACCEL_RANGE_8G)
def magnetic_to_heading(x,y,z):
    if x == 0:
        if y < 0:
            return 90.0
        else:
            return 0.0
    else:
        headingRad = math.atan2(y, z)

        # Correct for reversed heading
        if (headingRad < 0):
            headingRad += 2 * math.pi

        # Check for wrap and compensate
        if (headingRad > 2 * math.pi):
            headingRad -= 2 * math.pi

        # Convert to degrees from radians
        headingDeg = headingRad * 180 / math.pi
        return headingDeg

# Main loop will read the acceleration and magnetometer values every second
# and print them out.
while True:
    # Read acceleration & magnetometer.
    accel_x, accel_y, accel_z = sensor.accelerometer
    mag_x, mag_y, mag_z = sensor.magnetometer
    # Print values.
    print(
        "Acceleration (m/s^2): ({0:0.3f}, {1:0.3f}, {2:0.3f})".format(
            accel_x, accel_y, accel_z
        )
    )
    print(
        "Magnetometer (uTesla): ({0:0.3f}, {1:0.3f}, {2:0.3f}) Heading: {3:0.3f}".format(
            mag_x, mag_y, mag_z, magnetic_to_heading(mag_x * 0.15258789063, mag_y * 0.15258789063, mag_z * 0.15258789063)
        )
    )
    # Delay for a second.
    time.sleep(1.0)

