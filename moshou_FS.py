import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

def normalAttack_fire():
	pyautogui.press('1')
	time.sleep(0.2)
	pyautogui.press('/')
	time.sleep(0.2)

	for x in range(1,10):
		pyautogui.press('2')
		time.sleep(1.7)
		pass

	pyautogui.press('.')
	time.sleep(2)
	pyautogui.press('/')
	time.sleep(0.5)
	pass