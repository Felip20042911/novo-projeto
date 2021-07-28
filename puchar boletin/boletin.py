import pyautogui as pyGUI
import pyperclip
from time import sleep

pyGUI.PAUSE = 0.5
#abre o chrome
pyGUI.press('win')
pyGUI.write('chrome')
pyGUI.press('enter')

#entra no NSA
sleep(3.5)
pyperclip.copy('https://nsa.cps.sp.gov.br')
pyGUI.hotkey('ctrl', 'v')
pyGUI.press('enter')


#loga no meu NSA
sleep(3.7)
pyGUI.moveTo(x=803, y=357)
pyGUI.click()
pyGUI.write('010')

pyGUI.moveTo(x=659, y=376)
pyGUI.click()
pyGUI.write('200801')

pyGUI.moveTo(x=680, y=395)
pyGUI.click()
pyGUI.write('Felip2911')

#faz o reCaptcha
pyGUI.moveTo(x=606, y=437)
pyGUI.click()
sleep(3)
pyGUI.moveTo(x=778, y=481)
pyGUI.click()

#entra no boletin
sleep(4)
pyGUI.moveTo(x=670, y=449)
pyGUI.click()
sleep(2)
pyGUI.moveTo(x=458, y=223)
pyGUI.click()

#da um print

sleep(3)
pyGUI.hotkey('win', 'shift', 's')

pyGUI.moveTo(x=371, y=341)
pyGUI.mouseDown()
pyGUI.moveTo(x=1135, y=700)
pyGUI.mouseUp()

#salvar o print
sleep(2)
pyGUI.click()
sleep(2)
pyGUI.moveTo(x=903, y=82)
pyGUI.click()
pyGUI.moveTo(x=1027, y=536)
pyGUI.click()

#fechando tudo
sleep(3)
pyGUI.moveTo(x=1012, y=47)
pyGUI.click()
sleep(2)
pyGUI.moveTo(x=1360, y=13)
pyGUI.click()
