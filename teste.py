import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)

kit.continuous_servo [0] .throttle = 1
kit.servo[1].angle = 180
