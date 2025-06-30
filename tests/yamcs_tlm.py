from yamcs.client import YamcsClient
from yts.sys.yamcs import Yamcs

client = YamcsClient("localhost:8090")
processor = client.get_processor("simulator", "realtime")
Yamcs.get_tlm(processor, 'YSS/SIMULATOR/Rssi')