"""
This is an example code that uses the Servo class to control a servo motor.

Initializes the Servo object with the servo connected to pin 32.
Enters an infinite loop that repeats the following steps:
Sets the angle of the servo to 90 degrees.
Pauses for 1 second.
Sets the angle of the servo to 0 degrees.
Pauses for 1 second.
Sets the angle of the servo to 180 degrees.
Pauses for 1 second.
Note: Make sure to import the required modules before running this code.
"""

import servo
import time

#Initialize the Servo object with the servo connected to pin 32
servo = servo.Servo(pin=32)

while True:
    servo.set_angle(90)  # Set the angle of the servo to 90 degrees
    time.sleep(1)  # Pause for 1 second
    servo.set_angle(0)  # Set the angle of the servo to 0 degrees
    time.sleep(1)  # Pause for 1 second
    servo.set_angle(180)  # Set the angle of the servo to 180 degrees
    time.sleep(1)  # Pause for 1 second
