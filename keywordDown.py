import pyautogui
import time
import moshou_DZ
import moshou_FS
import moshou_LR

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5


time.sleep(5)

moshou_LR.showTime('fireAttack', waitTime = 11, feedTimes = 30)

