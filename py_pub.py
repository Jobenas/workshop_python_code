import paho.mqtt.client as paho
import numpy as np

broker = "iot.jobenas.com"
port = 1883

def on_publish(client, userdata, result):
    print("data published")


if __name__ == "__main__":
    client_name = f"python_client_{np.random.randint(10000, size=(1))[0]}"
    mqttClient = paho.Client(client_name)
    mqttClient.on_publish = on_publish
    mqttClient.connect(broker, port)
    ret = mqttClient.publish("buttonStatus", "OFF")