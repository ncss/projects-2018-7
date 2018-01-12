#! /bin/bash

DIR=/run/media/cbel8177/PYBFLASH

if [ -d $DIR ]; then
	cp -v ${1} $DIR/main.py
	sleep 5
	sync

	screen /dev/ttyACM0
else
	echo 'assuming microbit'

    python uflash.py ${1}
    screen /dev/ttyACM0
fi
