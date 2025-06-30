from time import sleep

from yamcs.client import YamcsClient, ProcessorClient

class Yamcs:
    @staticmethod
    def get_tlm(processor: ProcessorClient, parameter: str):
        """Shows how to poll values from the subscription."""
        return processor.get_parameter_value(parameter)
    
    @staticmethod
    def send_tlm(processor: ProcessorClient, parameter: str, value: str | float | int):
        """Shows how to poll values from the subscription."""
        processor.set_parameter_value(parameter, value)  
        return True





