import pyautogui
import time

time.sleep(5)

# pyautogui.press('[')

# while True:
# 	pyautogui.press('88')
# 	time.sleep(2)
# 	pass


# print(pyautogui.position())

# Point(x=959, y=711)
# 
# Point(x=967, y=496)

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

moveMouse(0, 215,"left")