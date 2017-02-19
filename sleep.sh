#!/usr/bin/env bash

LOG_FILE=sleep.log

# Turn the volume down
echo "Turning the volume down" | tee $LOG_FILE
/home/maurice/controlScripts/projector.py -v - | tee $LOG_FILE
sleep 1
/home/maurice/controlScripts/projector.py -v - | tee $LOG_FILE
sleep 1
/home/maurice/controlScripts/projector.py -v - | tee $LOG_FILE
sleep 1
/home/maurice/controlScripts/projector.py -v - | tee $LOG_FILE
sleep 1
/home/maurice/controlScripts/projector.py -v - | tee $LOG_FILE
sleep 1
/home/maurice/controlScripts/projector.py -v - | tee $LOG_FILE
sleep 1

# Finally, turn off the projector
/home/maurice/controlScripts/projector.py -p 0 | tee $LOG_FILE

# Also, lets change back our hdmi input
/home/maurice/controlScripts/hdmiSelector.py 1 | tee $LOG_FILE

