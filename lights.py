#!/usr/bin/env python

import paho.mqtt.client as mqtt
import argparse
import sys

parser = argparse.ArgumentParser(description='Control lights')
parser.add_argument('lightNum', help="Number of light to control", type=int, default=1)
parser.add_argument('-p', '--power', help="set power 0=off, 1=on, 2=toggle", type=int, default=1)
parser.add_argument('-b', '--brightness', help="set brightness level 0-100", type=int, default=1)
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

if args.power:
	if args.power == 0:
		control_str="off"
	elif args.power == 1:
		control_str="on"
	elif args.power == 2:
		control_str="toggle"
	else:
		print "unknown power option specified"
		sys.exit()

print "Setting light"+str(args.lightNum)+" "+control_str 
ret = client.publish("/bensRoom/light1", "{\"command\":\""+control_str+"\"}")
ret = client.publish("/bensRoom/light2", "{\"command\":\""+control_str+"\"}")
ret = client.publish("/bensRoom/light3", "{\"command\":\""+control_str+"\"}")
ret = client.publish("/bensRoom/light4", "{\"command\":\""+control_str+"\"}")

print "Publishe status = " + str(ret[0])

client.disconnect()
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#client.loop_forever()
