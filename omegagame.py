#!/usr/bin/python

from evdev import InputDevice, categorize, ecodes, KeyEvent
from OmegaExpansion import oledExp
from asyncore import file_dispatcher, loop
import random

# playfield dimensions
ROWS = 8
COLS = 21

# initial player position
x = 0
y = 1

#initial enemy position
enemyX = -1
enemyY = -1

hit = True
score = 0

class InputDeviceDispatcher(file_dispatcher):
	def __init__(self, device):
		self.device = device
		self.movX = 0
		self.movY = 0
		self.start = False
		self.select = False
		file_dispatcher.__init__(self, device)

	def getStart(self):
		return self.start

	def getMovX(self):
		return self.movX
		
	def getMovY(self):
		return self.movY
		
	def recv(self, ign=None):
		return self.device.read()

	def handle_read(self):
			
		for event in self.recv():
			if event.type == ecodes.EV_ABS:
				if event.code == 1:
					if event.value == 0:
						#print("UP")
						self.movY=-1
					if event.value == 255:
						#print("DOWN")
						self.movY=1
					if event.value == 128:
						#print("CENTER Y")
						self.movY = 0
				if event.code == 0:
					if event.value == 0:
						#print("LEFT")
						self.movX=-1
					if event.value == 255:
						#print("RIGHT")
						self.movX=1
					if event.value == 128:
						#print("CENTER X")
						self.movX = 0
				#print self.movX, self.movY
			if event.type == ecodes.EV_KEY:
				if event.code == 295:
					if event.value == 1:
						print("START PRESSED")
						self.start = True
					if event.value == 0:
						print("START RELEASED")
				if event.code == 294:
					if event.value == 1:
						print("SELECT PRESSED")
					if event.value == 0:
						print("SELECT RELEASED")
				if event.code == 289:
					if event.value == 1:
						print("B PRESSED")
					if event.value == 0:
						print("B RELEASED")
				if event.code == 288:
					if event.value == 1:
						print("A PRESSED")
					if event.value == 0:
						print("A RELEASED")
				if event.code == 290:
					if event.value == 1:
						print("X PRESSED")
					if event.value == 0:
						print("X RELEASED")
				if event.code == 291:
					if event.value == 1:
						print("Y PRESSED")
					if event.value == 0:
						print("Y RELEASED")				
				if event.code == 293:
					if event.value == 1:
						print("R PRESSED")
					if event.value == 0:
						print("R RELEASED")				
				if event.code == 292:
					if event.value == 1:
						print("L PRESSED")
					if event.value == 0:
						print("L RELEASED")	

def player():
	global x 
	global y

	loop(timeout=1, count=250)
	movementX = i.getMovX()
	movementY = i.getMovY()
	prevX = x
	prevY = y
	isMoving = False
	if movementX>0 and x<COLS-1:
		isMoving=True
		x += 1
	if movementX<0 and x>0:
		isMoving=True
		x -= 1
	if movementY>0 and y<ROWS-1:
		isMoving=True
		y += 1
	if movementY<0 and y>1:
		isMoving=True
		y -= 1
	if isMoving:
		oledExp.setCursor(prevY, prevX)
		oledExp.writeChar(' ')

	oledExp.setCursor(y, x)
	oledExp.writeChar('@')

def enemy():
	global hit
	global x
	global y
	global enemyX
	global enemyY
	global score
	if hit == True:
		hit = False
		enemyX = int(random.uniform(1, 20))
		enemyY = int(random.uniform(1, 7))
		oledExp.setCursor(enemyY, enemyX)
		oledExp.writeChar('*')
		
	# basic collision detection
	if x == enemyX and y == enemyY:
		hit = True
		score += 1
		writeScore(score)

def writeScore(score):
	oledExp.setCursor(0, 0)
	oledExp.write("score: %d" % score)

def mainLoop():
	writeScore(0)
	while True:		
		player()
		enemy()		
		


def intro():
	oledExp.setCursor(2, 6)
	oledExp.write("T  H  E")
	oledExp.setCursor(4, 0)
	oledExp.write(" O M E G A - G A M E ")
	start = False
	while start == False:
		loop(timeout=1, count=2000)
		if i.getStart() == True:
			start = True
			oledExp.clear()
		oledExp.setCursor(6, 4)
		oledExp.write(" P R E S S  S T A R T ")
		oledExp.setCursor(6, 4)
		oledExp.write("                      ") 

def initScreen():
	oledExp.driverInit()
	oledExp.setTextColumns()

###################### MAIN ##############################	
	
gamepad = InputDevice('/dev/input/event0')
i = InputDeviceDispatcher(gamepad)
initScreen()

# play intro
intro()

# run main game loop
mainLoop()
