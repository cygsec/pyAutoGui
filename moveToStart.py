import pyautogui
start = pyautogui.locateCenterOnScreen('start.png') #If the file is not a png file it will not work
print(start)
pyautogui.moveTo(start) #Moves the mouse to the coordinates of the image
