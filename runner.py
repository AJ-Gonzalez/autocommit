#!/usr/bin/python3
from os import system as cmd
from random import randrange
from time import sleep
HOUR=3600
while True:
	sleep(randrange(3*HOUR,9*HOUR))
	try:
		cmd('./autocommit.py >> log.txt')
	except Exception:
		pass