import time
import pyautogui

# deixe a tela do chrome a 90%.
# escolher no google imagens tamanho grande.
# salvar um arquivo na pasta onde deseja salvar.
# aperte na primeira imagem.
j = 1
k = 1
while k <= 200:

    pyautogui.sleep(3)
    pyautogui.moveTo(750,300)
    # x se move da esquerda para direita,y é se move de cima para baixo.
    # no x o canto esquerdo da tela é 0 e no y a parte de cima é 0.
    pyautogui.click(button='right')
    pyautogui.sleep(3)

    i = 1
    while i <=6:
        pyautogui.press("up")
        i += 1

    pyautogui.sleep(3)
    pyautogui.press('enter')
    pyautogui.sleep(2)
    pyautogui.hotkey('ctrl','tab')
    pyautogui.moveTo(500, 300)
    pyautogui.click(button='right')
    pyautogui.sleep(3)

    i=1
    while i <= 6:
        pyautogui.press("up")
        i += 1

    pyautogui.sleep(3)
    pyautogui.press('enter')
    pyautogui.press('left')

    if j % 2 == 0:
        pyautogui.write('a')
    else:
        pyautogui.write('b')
    j += 1

    pyautogui.press('enter')
    pyautogui.sleep(3)
    pyautogui.hotkey('ctrl','w')
    pyautogui.press('right')

    k += 1





