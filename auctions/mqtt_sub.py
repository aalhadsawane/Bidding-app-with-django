import sys

import paho.mqtt.client as paho


def message_handling(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")


client = paho.Client()
client.on_message = message_handling

if client.connect("127.0.0.1", 1883, 60) != 0:
    print("sub couldn't connect to the mqtt broker")
    sys.exit(1)

def sub_topic(topic):
    client.subscribe(topic)

client.subscribe("test_topic")

try:
    print("from mqtt sub, Press CTRL+C to exit...")
    client.loop_forever()
except Exception:
    print("Caught an Exception, something went wrong...")
finally:
    print("Disconnecting from the MQTT broker")
    client.disconnect()