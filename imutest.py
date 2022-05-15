#!/usr/bin/python3
from math import degrees
from time import sleep
import RTIMU
SETTINGS_FILE = "/home/pi/dev/imutest/RTIMULib"
s = RTIMU.Settings(SETTINGS_FILE)
s.FusionType = 1
s.CompassCalValid = False

s.CompassCalEllipsoidOffset = (0, 0, 0)
s.CompassCalEllipsoidValid = True
s.MPU925xAccelFsr = 0  # +- 2g
s.MPU925xGyroFsr = 0  # +- 250 deg/s
# compass noise by rate 10=.043, 20=.033, 40=.024, 80=.017, 100=.015
rate = 100
s.MPU925xGyroAccelSampleRate = rate
s.MPU925xCompassSampleRate = rate

s.AccelCalValid = True  # will be updated later
s.AccelCalMin = (-1, -1, -1)
s.AccelCalMax = (1, 1, 1)

s.GyroBiasValid = False
s.GyroBias = (0, 0, 0)

s.KalmanRk, s.KalmanQ = .002, .001
s.IMUType = 0 # always autodetect imu
imu = RTIMU.RTIMU(s)
if (not imu.IMUInit()):
  print("IMU init failed")
  exit(1)
else:
  print("IMU init succeeded")
imu.setSlerpPower(0.02)
imu.setGyroEnable(True)
imu.setAccelEnable(True)
imu.setCompassEnable(True)
poll_interval = imu.IMUGetPollInterval()
while True:
  if imu.IMURead():
    data = imu.getIMUData()
    print(data)
    fusionPose = data["fusionPose"]
    global roll, pitch, yaw
    roll = degrees(fusionPose[0])
    pitch = degrees(fusionPose[1])
    yaw = degrees(fusionPose[2])
    print(str(roll) + "   " + str(pitch) + "   " + str(yaw))
    sleep(1)
