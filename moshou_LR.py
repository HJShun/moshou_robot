import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

feedTime = 0

def showTime( attackName, waitTime, feedTimes):
	while True:
		
		if attackName == 'normalAttack':
			normalAttack()
		elif attackName == 'walkAttack':
			walkAttack()
		elif attackName == 'fireAttack':
			fireAttack(waitTime)

		feedPet(feedTimes)
		pass
	pass

def normalAttack():
	pyautogui.press('1')
	time.sleep(0.2)
	pyautogui.press('/')
	time.sleep(0.2)
	pyautogui.press('4')
	time.sleep(1)
	pyautogui.press('3')
	time.sleep(1)
	# pyautogui.press('7')
	time.sleep(17)
	pyautogui.press('.')
	time.sleep(1)
	pyautogui.press('/')
	time.sleep(2)
	pyautogui.press('.')
	time.sleep(1)
	pyautogui.press('/')
	time.sleep(2)
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

def walkAttack():
	pyautogui.press('1')
	time.sleep(0.2)
	pyautogui.press('/')
	time.sleep(3)
	# pyautogui.press('0')
	# time.sleep(0.2)
	pyautogui.press('4')
	time.sleep(1)
	pyautogui.press('3')
	time.sleep(1)
	# pyautogui.press('5')
	# time.sleep(1)
	# pyautogui.press('8')
	# time.sleep(1)
	pyautogui.press('7')
	time.sleep(30)
	pyautogui.press('.')
	time.sleep(1)
	pyautogui.press('/')
	time.sleep(2)
	pyautogui.press('.')
	time.sleep(1)
	pyautogui.press('/')
	time.sleep(2)
	pass

def fireAttack(waitTime):
	pyautogui.hotkey('ctrl', '0')
	time.sleep(0.2)
	pyautogui.press('1')
	time.sleep(0.2)
	pyautogui.hotkey('ctrl', '1')
	time.sleep(10)
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
	moveMouse(0, 300,"left")
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

def moveMouse(pointX, poitnY,buttonclick):
	pyautogui.move(pointX, poitnY)
	time.sleep(0.5)
	pyautogui.click(button=buttonclick)
	time.sleep(1)
	pyautogui.move(pointX, -poitnY)
	time.sleep(0.5)
	pyautogui.click(button=buttonclick)
	time.sleep(1)
	pass