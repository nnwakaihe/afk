import pyautogui as pag
import random
import time

def main():
    current_position = pag.position()

    while True:
        if pag.position() != current_position:
            break

        x = random.randint(600,700)
        y = random.randint(200,600)
        pag.moveTo(x,y,0.5)
        #time.sleep(120)
        current_position = pag.position()
        time.sleep(2)

if __name__ == "__main__":
    main()