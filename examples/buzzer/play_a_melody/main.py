"""
This is an example code that uses the Buzzer class to play a melody.

Initializes a Buzzer object with the buzzer connected to pin 26.
Creates a tuple of frequency values for the melody.
Loops through each frequency in the tuple.
Calls the pitch_ms method of the Buzzer object to play the tone with the specified frequency for 400 milliseconds.
Pauses for 100 milliseconds between each tone.
Note: Make sure to import the required modules before running this code.
"""

import time
import buzzer

#Initialize the Buzzer object with the buzzer connected to pin 26
my_buzzer = buzzer.Buzzer(pin=26)

#Create a tuple of frequency values for the melody
tones = (262, 262, 392, 392, 440, 440, 392)

#Loop through each frequency in the tuple
for tone in tones:
    # Call the pitch_ms method of the Buzzer object to play the tone with the specified frequency for 400 milliseconds
    my_buzzer.pitch_ms(tone, 400)
    # Pause for 100 milliseconds between each tone
    time.sleep_ms(100)
