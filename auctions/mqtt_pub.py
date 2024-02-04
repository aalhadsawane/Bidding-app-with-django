import sys

import paho.mqtt.client as paho

client = paho.Client()

if client.connect("127.0.0.1", 1883, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)

def pub_msg(topic, content):
    client.publish(topic, content)

client.publish("test_topic", "Hi, paho mqtt client works fine!", 0)
client.disconnect()