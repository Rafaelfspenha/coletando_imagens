import time
import pyautogui

# em chrome://settings/downloads,
# a opção "perguntar onde salvar o arquivo antes de fazer download" deve estar ativada.

# deixe a tela do chrome a 90%.
# feche todas as janelas do chrome.

j = 1
k = 1

opcao1 = input("Digite tema a pesquisar: ")

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.sleep(3)
pyautogui.press('enter')
pyautogui.sleep(3)
pyautogui.hotkey('alt','space','x') # maximizar janela do chrome
pyautogui.sleep(3)
pyautogui.press('esc')  # essa linha é para evitar erro!
pyautogui.moveTo(200,50)  # essa linha é para evitar erro!
pyautogui.click(button='left')  # essa linha é para evitar erro!
pyautogui.sleep(3)
pyautogui.write('https://images.google.com/')
pyautogui.sleep(3)
pyautogui.press('enter')
pyautogui.sleep(3)
pyautogui.write(opcao1)
pyautogui.sleep(3)
pyautogui.press('enter')
pyautogui.sleep(3)

i = 1
while i <= 16:
    pyautogui.press("tab")
    i += 1

pyautogui.sleep(3)
pyautogui.press('enter')
pyautogui.sleep(3)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.sleep(3)

i = 1
while i <= 4:
    pyautogui.press("up")
    i += 1

pyautogui.sleep(3)
pyautogui.press('enter')
pyautogui.sleep(6)
pyautogui.moveTo(50,300)
pyautogui.click(button='left')


while k <= 200: # quantidade de imagens a baixar

    pyautogui.sleep(6)
    pyautogui.moveTo(750,300)
    # x se move da esquerda para direita,y é se move de cima para baixo.
    # no x o canto esquerdo da tela é 0 e no y a parte de cima é 0.
    pyautogui.sleep(3)
    pyautogui.click(button='right')
    pyautogui.sleep(3)

    # na página do google maps, após clicar na foto
    i = 1
    while i <=6:
        pyautogui.press("up")
        i += 1

    pyautogui.sleep(3)
    pyautogui.press('enter')
    pyautogui.sleep(2)
    pyautogui.hotkey('ctrl','tab')

    # na próxima guia
    pyautogui.sleep(3)
    pyautogui.moveTo(500, 300)
    pyautogui.sleep(3)
    pyautogui.click(button='right')
    pyautogui.sleep(3)

    i=1
    while i <= 6:
        pyautogui.press("up")
        i += 1

    pyautogui.sleep(3)
    pyautogui.press('enter')
    pyautogui.sleep(3)
    pyautogui.press('left')
    pyautogui.sleep(3)

    if j % 2 == 0:
        pyautogui.write('a')
    else:
        pyautogui.write('b')
    j+=1

    pyautogui.sleep(3)
    pyautogui.press('enter')
    pyautogui.sleep(3)
    pyautogui.hotkey('ctrl','w')
    pyautogui.sleep(3)
    pyautogui.press('right')

    k += 1


