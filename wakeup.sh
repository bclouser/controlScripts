#!/usr/bin/env bash

LOG_FILE=wakeup.log

#Select the correct hdmi input
/home/maurice/controlScripts/hdmiSelector.py 2 | tee $LOG_FILE

# OK, turn on the projector
/home/maurice/controlScripts/projector.py -p 1 | tee $LOG_FILE

# OK, lets wait for 30 seconds for the projector to turn on
echo "Waiting for 60 seconds" | tee $LOG_FILE
sleep 60 | tee $LOG_FILE
 
# Annnnd, turn the volume up... slowly
echo "Turning the volume up... slowly" | tee $LOG_FILE
/home/maurice/controlScripts/projector.py -v + | tee $LOG_FILE
sleep 2
/home/maurice/controlScripts/projector.py -v + | tee $LOG_FILE
sleep 2
/home/maurice/controlScripts/projector.py -v + | tee $LOG_FILE
sleep 2
/home/maurice/controlScripts/projector.py -v + | tee $LOG_FILE
sleep 2
/home/maurice/controlScripts/projector.py -v + | tee $LOG_FILE
sleep 2
/home/maurice/controlScripts/projector.py -v + | tee $LOG_FILE




