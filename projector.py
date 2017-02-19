#!/usr/bin/env python

import paho.mqtt.client as mqtt
import argparse

parser = argparse.ArgumentParser(description='Control and get status from projector')
parser.add_argument('-p', '--power', help="set power 1=on 0=off", type=int, default=1)
parser.add_argument('-v', '--volume', help="set volume +=up -=down")
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

# power on is the default
command = 1
if not args.power:
	command = 0

if args.volume:
	if args.volume=='+':
		command = 5
	elif args.volume=='-':
		command = 6
	else:
		print "Bad volume command, expecting + or -"

if command == 0:
	print "Turning off projector"
elif command == 1:
	print "Turning on projector"
elif command == 2:
	print "requesting projector state"
elif command == 3:
	print "Requesting filter time"
elif command == 4:
	print "Requesting projector errors"
elif command == 5:
	print "Turning volume up"
elif command == 6:
	print "Turning volume down"
else:
	print "Bad command"

ret = client.publish("/projectorControl_SOMEHASH", '{"command":'+str(command)+'}')

print "Publishe status = " + str(ret[0])

client.disconnect()
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#client.loop_forever()
