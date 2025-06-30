import math
import time
import threading
import requests
from typing import Literal

class Demo:
    def __init__(self, c2: Literal['OPEN-NCT', "YAMCS"]):
        self.c2 = c2
        self.running = False
        self.frequency = None
    
    def start_tlm(self):
        # Parameters for sine wave generation
        start_angle = 0        # Starting angle for sine wave
        low = -120             # Lower bound of the range
        high = -80             # Upper bound of the range
        amplitude = (high - low) / 2  # Half the difference between high and low to control the oscillation range
        self.frequency = 0.1        # Frequency of the sine wave oscillation

        # Create a generator for the sine wave
        sine_generator = self._generate_sine_wave(start_angle, low, high, self.frequency, amplitude)
        
        # Global flag to control the main loop
        self.running = True

        if self.c2 == 'OPEN-MCT':
            # The URL of the Node.js server (replace with your server's IP if not running locally)
            url = 'http://localhost:7070'

            # # Start the user input handling thread
            # input_thread = threading.Thread(target=handle_user_input, daemon=True)
            # input_thread.start()
            while self.running:
                # Get the next value from the sine wave generator and print it
                response = requests.post(url, data=str(next(sine_generator)))
                # Optional: sleep for a brief moment to control output speed
                time.sleep(1)  # Adjust this for the speed of generation (in seconds)


    def change_agc(self, new_frequency: float):
        # global frequency
        self.frequency = new_frequency


    @staticmethod
    def _generate_sine_wave(
        start_angle, 
        low, 
        high, 
        frequency=0.1, 
        amplitude=20
        ):
        angle = start_angle
        
        while True:
            # Calculate the sine value
            sine_value = math.sin(angle)
            
            # Scale the sine value to fit within the specified range
            scaled_value = low + (sine_value * amplitude)
            
            # Yield the scaled value
            yield round(scaled_value, 2)
            
            # Update the angle to simulate continuous oscillation
            angle += frequency
