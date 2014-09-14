#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	PillenBareAPI Protokoll:
	- 6 Status Bits (0-63) und 10 Value Bits (0-1023) ?
"""

import serial
import RPi.GPIO as GPIO

__author__ = "(c) Gruppe 'Die intelligente Pillenbox' 2014"
__version__ = 1.0

global servo1, servo2, servo3
servo1 = None
servo2 = None
servo3 = None

global servo1_angle, servo2_angle, servo3_angle
servo1_angle = None
servo2_angle = None
servo3_angle = None

class PillenBareAPI(object):
	con = None
	servo1, servo2, servo3 = None
	
	def __init__(self, port, baudrate):
		con = serial.Serial(port, baudrate)
		
		GPIO.setmode(GPIO.BCM)
		
		# LEDs
		for i in (14, 15, 18):
			GPIO.setup(i, GPIO.OUT)
		
		# Servos
		for i in (16, 20, 21):
			GPIO.setup(i, GPIO.OUT)
			
		servo1 = GPIO.PWM(16, 50)
		servo2 = GPIO.PWM(20, 50)
		servo3 = GPIO.PWM(21, 50)
		servo1.start(5)
		servo2.start(5)
		servo3.start(5)
		self.setServoWinkel(servo1, 90)
		self.setServoWinkel(servo2, 90)
		self.setServoWinkel(servo3, 90)
	
	def __str__(self):
		return "Pillen Bare API an Port: " + self.con.port + " und der Baudrate " + self.con.baudrate
	
	def __sendData(self, data):
		senddata = ""
		if ((isinstance(data, list)) or (isinstance(data, tuple))):
			for i in data:
				if (i == 0):
					_i = chr(48)
					senddata += _i
				elif (i == 1):
					_i = chr(49)
					senddata += _i
				else:
					raise Exception("Ein Part von data ist keine Null oder Eins")
			self.con.write(senddata)
		else:
			raise Exception("data ist keine Liste oder ein Tupel")
	
	@staticobject
	def connect(self, port, baudrate):
		return PillenAPI(port, baudrate)
	
	def setServoWinkel(self, servo, angle):
		if (isinstance(servo, GPIO.PWM)):
			if (servo == servo1):
				servo1_angle = angle
			elif (servo == servo2):
				servo2_angle = angle
			elif (servo == servo3):
				servo3_angle = angle
			else:
				raise Exception("Der Winkel des Servos konnte leider nicht gesetzt werden!")
		freq = float(angle)/10.0 + 2.5
		servo.ChangeDutyCycle(freq)
	
	def getServoWinkel(self, servo): #in den Doku gucken
		if (isinstance(servo, GPIO.PWM)):
			if (servo == servo1):
				return servo1_angle
			elif (servo == servo2):
				return servo2_angle
			elif (servo == servo3):
				return servo3_angle
			else:
				raise Exception("Der Winkel konnte nicht ausgegeben werden!")
	
	def setLED(self, led, status):
		_led = None
		
		if (led not in [1, 2, 3]):
			raise Exception("Die LED ist nicht in der Liste der verbauten LEDs!")
		elif (led == 1):
			_led = 14
		elif (led == 2):
			_led = 15
		elif (led == 3):
			_led = 18
		
		if (isinstance(status, bool)):
			GPIO.output(_led, status)
		else:
			raise Exception("Der Status ist nicht True oder False!")
	
	def getLichtsensor(self, number):
		value = None
		
		if (number == 1):
			self.__sendData([0, 0])
			value = self.con.readline() #noch nicht funktionstüchtig, in Arduino Serial Monitor schon, aber bitte mit Zeilenumbrüchen
		elif (number == 2):
			self.__sendData([0, 1])
			value = self.con.readline() #noch nicht funktionstüchtig, in Arduino Serial Monitor schon, aber bitte mit Zeilenumbrüchen
		elif (number == 3):
			self.__sendData([1, 0])
			vaule = self.con.readline() #noch nicht funktionstüchtig, in Arduino Serial Monitor schon, aber bitte mit Zeilenumbrüchen
		else:
			raise Exception("number ist nicht eine Zahl von 1-3")
		
		return value
	
	def wirfPilleRaus(self, seite): # noch ändern weil man nicht wegen den Servos weiss
		if (seite == "l"):
			self.setServoWinkel(servo1, 180) # kein Plan
		elif (seite == "r"):
			self.setServoWinkel(servo2, 180) # kein Plan
		else:
			raise Exception("Fehler mit dem anzusteuernden Servo!")
