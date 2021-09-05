import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

feedTime = 0

def showTime( attackName, waitTime, feedTimes):
	while True:
		if attackName == 'fireAttack':
			fireAttack(waitTime)

		feedPet(feedTimes)
		pass
	pass

def feedPet(number):
	global feedTime
	if feedTime == number:
		pyautogui.press(';')
		time.sleep(20)
		feedTime = 0
		pass
	else:
		feedTime += 1
	pass

def fireAttack(waitTime, attacktime):
	pyautogui.hotkey('ctrl', '0')
	time.sleep(0.2)
	pyautogui.press('1')
	time.sleep(0.2)
	pyautogui.hotkey('ctrl', '1')
	time.sleep(attacktime)
	pyautogui.hotkey('ctrl', '2')
	time.sleep(9)
	pyautogui.hotkey('ctrl', '9')
	time.sleep(2)
	pyautogui.press('[')
	time.sleep(1)
	pyautogui.press(']')
	time.sleep(0.5)
	pyautogui.press('/')
	time.sleep(1)
	pyautogui.press('[')
	time.sleep(1)
	pyautogui.press(']')
	time.sleep(0.5)
	pyautogui.press('/')
	time.sleep(1)
	pyautogui.press('7')
	time.sleep(1)
	pyautogui.press('5')
	# time.sleep(0.2)
	# pyautogui.press('2')
	time.sleep(waitTime)
	# moveMouse_take(0, 300,"left")
	moveMouse_take_bopi(bopiTime = 2)
	# pyautogui.press('.')
	time.sleep(1)
	# pyautogui.press('/')
	# time.sleep(2)
	# pyautogui.press('.')
	# time.sleep(1)
	# pyautogui.press('8')
	# time.sleep(2)
	# pyautogui.press('-')
	# time.sleep(0.5)
	pass

def moveMouse_take(pointX, poitnY,buttonclick):
	pyautogui.move(pointX, poitnY)
	time.sleep(0.5)
	pyautogui.click(button=buttonclick)
	time.sleep(1)
	pyautogui.move(pointX, -poitnY)
	time.sleep(0.5)
	pyautogui.click(button=buttonclick)
	time.sleep(1)
	pass

def bopi_take(bopiTime):
	pyautogui.press('.')
	time.sleep(1)
	pyautogui.press('/')
	time.sleep(2)
	for x in range(0,bopiTime):
		time.sleep(2)
		pyautogui.press('.')
		time.sleep(1)
		pyautogui.press('8')
		time.sleep(2)
		pyautogui.press('-')
		time.sleep(0.5)
		pass
	pass

def moveMouse_take_bopi(bopiTime):
	moveMouse_take(0, 0,"left")
	for x in range(0,bopiTime):
		pyautogui.press('8')
		time.sleep(2)
		pass
	
	pyautogui.press('-')
	time.sleep(0.5)
	pass