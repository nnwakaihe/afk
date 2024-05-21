import pyautogui as pag
import random
import time

def main():
    time.sleep(5)      #wait 10 sec before starting
    current_position = pag.position()

    active = False  # Initialize active here

    while True:
        last_position = pag.position()
        time.sleep(60)  #Check position every ... sec
        current_position = pag.position()
        if last_position == current_position:
            active = True
            print("Turning ON")

        while active == True:
            if pag.position() != current_position:  #If mouse moved manually
                print("Turning OFF")
                active = False
                break

            x = random.randint(600,700)
            y = random.randint(200,600)
            pag.moveTo(x,y,0.5)
            pag.keyDown('up')
            pag.keyUp('up')
            current_position = pag.position()
            time.sleep(2) #Move every ... sec

if __name__ == "__main__":
    main()

# #Run the following command in the terminal to create executable:
# pyinstaller --name afk main.py
