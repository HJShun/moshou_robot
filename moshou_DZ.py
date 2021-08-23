import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

def normalAttack():
	pyautogui.press('1')
	time.sleep(0.5)
	pyautogui.press('/')
	time.sleep(0.5)
	pyautogui.press('2')
	time.sleep(0.5)
	pyautogui.leftClick()
	time.sleep(0.2)
	pass