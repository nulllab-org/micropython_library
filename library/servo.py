import machine


class Servo(object):
    """
    Initializes the Servo class.

    Args:
        pin (int): The pin number to which the servo is connected.
    
    Returns:
        None
    """

    def __init__(self, pin: int) -> None:
        self.pwm = machine.PWM(machine.Pin(pin), freq=50, duty=0)

    """
    Sets the angle of the servo.
    
    Args:
        angle (int): The angle to which the servo should be set, ranging from 0 to 180 degrees.
    
    Returns:
        None
    """

    def set_angle(self, angle):
        self.pwm.duty(int(((angle) / 90 + 0.5) / 20 * 1023))
