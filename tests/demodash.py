from yts.demos.agc_monitor import Demo
import threading


dem = Demo('OPEN-MCT')

input_thread = threading.Thread(target=dem.start_tlm, daemon=True)
input_thread.start()
print('started')
