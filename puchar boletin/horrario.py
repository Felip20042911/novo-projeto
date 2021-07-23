import pyautogui as py
import pyperclip
from time import sleep

py.PAUSE = 0.5
#abre o chrome
py.press('win')
py.write('chrome')
py.press('enter')

#entra no NSA
sleep(3.5)
pyperclip.copy('https://nsa.cps.sp.gov.br')
py.hotkey('ctrl', 'v')
py.press('enter')


#loga no meu NSA
sleep(3.7)
py.moveTo(x=803, y=357)
py.click()
py.write('010')

py.moveTo(x=659, y=376)
py.click()
py.write('200801')

py.moveTo(x=680, y=395)
py.click()
py.write('Felip2911')

#faz o reCaptcha
py.moveTo(x=606, y=437)
py.click()
sleep(3)
py.moveTo(x=778, y=481)
py.click()

#entra no horario
sleep(4)

py.moveTo(x=667, y=445)
py.click()

sleep(1.5)
py.moveTo(x=412, y=225)
py.click()
py.moveTo(x=419, y=270)
py.click()


#da um print

sleep(3)
py.hotkey('win', 'shift', 's')

py.moveTo(x=384, y=247)
py.mouseDown()
py.moveTo(x=1135, y=700)
py.mouseUp()

#salvar o print
sleep(2)
py.click()
sleep(2)
py.moveTo(x=903, y=82)
py.click()
sleep(0.5)
py.moveTo(x=1060, y=541)
py.click()


#fechando tudo
sleep(3)
py.moveTo(x=1012, y=47)
py.click()
sleep(2)
py.moveTo(x=1360, y=13)
py.click()
