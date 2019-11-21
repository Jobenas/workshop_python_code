import paho.mqtt.client as mqtt
import numpy as np

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

    client.subscribe("buttonStatus")


def on_message(client, userdata, message):
    print(f"message received: {str(message.payload)}")
    print(f"topic: {message.topic}")
    print(f"message qos: {message.qos}")
    print(f"message retain flag: {message.retain}")

if __name__ == "__main__":

    broker = "iot.jobenas.com"
    port = 1883

    mqtt_client = mqtt.Client(f"python_client_{np.random.randint(10000, size=(1))[0]}")

    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(broker, port, 60)

    mqtt_client.loop_forever()


