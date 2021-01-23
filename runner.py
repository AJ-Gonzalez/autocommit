#!/usr/bin/python3
from os import system as cmd
from random import randrange
from time import sleep
while True:
	sleep(randrange(10,30))
	try:
		cmd('./autocommit.py >> log.txt')
	except Exception:
		pass