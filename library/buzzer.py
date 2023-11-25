import machine
import time


class Buzzer:

    def __init__(self, pin: int) -> None:
        """
        Initializes the Buzzer class.

        Args:
            pin (int): The pin number where the buzzer is connected.
        """
        self.pwm = machine.PWM(machine.Pin(pin), freq=1, duty=0)

    def pitch_ms(self, freq: int, duration: int) -> None:
        """
        Generates a specific pitch and duration on the buzzer.

        Args:
            freq (int): The frequency of the pitch to be generated.
            duration (int): The duration of the pitch in milliseconds.
        """
        if freq == 0:
            self.pwm.duty(0)
        else:
            self.pwm.duty(512)
            self.pwm.freq(freq)
        time.sleep_ms(duration)
        self.pwm.duty(0)
