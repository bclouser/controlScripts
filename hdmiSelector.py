#!/usr/bin/env python
import paho.mqtt.client as mqtt
import argparse

parser = argparse.ArgumentParser(description='Control hdmi selector')
parser.add_argument('input_num', help="set the currently selected hdmi input 1-4", type=int)
args = parser.parse_args()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.199", 1883, 60)

print "Setting hdmi"+str(args.input_num)+" as the current input"
hdmiSelectString = "{\"command\":\"hdmi"+str(args.input_num)+"\"}"
print hdmiSelectString
ret = client.publish("/bensRoom/hdmiSelector1", hdmiSelectString)

print "Publishe status = " + str(ret[0])

client.disconnect()
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#client.loop_forever()
