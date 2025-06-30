#!C:\Users\OWNER\AppData\Local\pypoetry\Cache\virtualenvs\yts-V7ypgcX4-py3.12\Scripts\python.exe
from yamcs.client import YamcsClient
import math
import time
import threading
from yts.sys.yamcs import Yamcs

# Function to generate sine wave-based numbers
def generate_sine_wave(start_angle, low, high, frequency=0.1, amplitude=20):
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

# Function to handle user input
def handle_user_input():
    while True:
        user_input = input("Enter a command (e.g., 'pause', 'speed <value>', 'exit'): ").strip().lower()
        
        if user_input == 'exit':
            print("Exiting the program.")
            global running
            running = False
            break
        elif user_input == 'pause':
            print("Paused. Press Enter to resume.")
            input()  # Wait for user to press Enter to resume
            print("Resumed.")
        elif user_input.startswith('speed'):
            try:
                # Extract speed value and adjust the frequency
                _, speed_value = user_input.split()
                new_speed = float(speed_value)
                global frequency
                frequency = new_speed
                print(f"Speed adjusted to {new_speed}.")
            except ValueError:
                print("Invalid speed value. Please enter a number after 'speed'.")
        else:
            print("Unknown command. Use 'pause', 'speed <value>', or 'exit'.")

# initalize yamcs
client = YamcsClient("localhost:8090")
processor = client.get_processor(instance='simulator', processor='realtime')
parameter = '/YSS/SIMULATOR/Rssi'

# Parameters for sine wave generation
start_angle = 0        # Starting angle for sine wave
low = -120             # Lower bound of the range
high = -80             # Upper bound of the range
amplitude = (high - low) / 2  # Half the difference between high and low to control the oscillation range
frequency = 0.1        # Frequency of the sine wave oscillation

# Create a generator for the sine wave
sine_generator = generate_sine_wave(start_angle, low, high, frequency, amplitude)

# Global flag to control the main loop
running = True

# Start the user input handling thread
input_thread = threading.Thread(target=handle_user_input, daemon=True)
input_thread.start()

# Continuously generate numbers based on the sine wave
try:
    while running:
        # Get the next value from the sine wave generator and print it
        Yamcs.send_tlm(processor, parameter, next(sine_generator))    
        # Optional: sleep for a brief moment to control output speed
        time.sleep(1)  # Adjust this for the speed of generation (in seconds)

except KeyboardInterrupt:
    print("\nStopped by user.")
    