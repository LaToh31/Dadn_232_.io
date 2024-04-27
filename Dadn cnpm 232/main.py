import numpy as np
import time

#import my module

from mqtt import MyMQTTClient
from uart import UARTCommunication


AIO_USERNAME = "La_Toh"
AIO_KEY = "aio_pQzL64KlIlSqeVd7UlJL969Z6uTE"
AIO_FEED_ID = ["led", "fan", "temp", "humi","lux","door"]


mqtt_client = MyMQTTClient(AIO_USERNAME, AIO_KEY, AIO_FEED_ID)
uart = UARTCommunication(baudrate=115200, timeout=1)


def myProcessData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    if splitData[0] == "TEMP":
        mqtt_client.publish_data("temp",splitData[1])
    elif splitData[0] == "HUMI":
        mqtt_client.publish_data("humi",splitData[1])
    elif splitData[0] == "LUX":
        mqtt_client.publish_data("lux",splitData[1])




def myProcessMess(feed_id, payload):
    if feed_id == "led":
        if payload == "0":
            uart.send_data(f"led:{payload}")
        elif payload == "1":
            uart.send_data(f"led:{payload}")
        elif payload == "2":
            uart.send_data(f"led:{payload}")
        elif payload == "3":
            uart.send_data(f"led:{payload}")
    elif feed_id == "fan":
        if payload == "0":
            uart.send_data(f"fan:{payload}")
        elif payload == "1":
            uart.send_data(f"fan:{payload}")
        elif payload == "2":
            uart.send_data(f"fan:{payload}")
        elif payload == "3":
            uart.send_data(f"fan:{payload}")
        elif payload == "4":
            uart.send_data(f"fan:{payload}")
    elif feed_id == "door":
        if payload == "0":
            uart.send_data(f"door:{payload}")
        elif payload == "1":
            uart.send_data(f"door:{payload}")        


def main():

    # serial init
    uart.processData = myProcessData
    mqtt_client.processMessage = myProcessMess
    #mqtt init
    mqtt_client.start()

    while True:
        uart.read_serial()
        time.sleep(1)
    
if __name__ == "__main__":
    main()


