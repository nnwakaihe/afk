import pyautogui as pag
import random
import time

def main():
    # Time variables
    startup_delay = 5
    position_check_timer = 120
    movement_timer = 60

    time.sleep(startup_delay)      #wait 10 sec before starting
    print("Booting Up...")
    current_position = pag.position()

    active = False  # Initialize active here

    while True:
        last_position = pag.position()
        time.sleep(position_check_timer)  #Check position every ... sec
        current_position = pag.position()
        if last_position == current_position:
            active = True
            print("Turning ON")

        while active == True:
            if pag.position() != current_position:  #If mouse moved manually
                print("Turning OFF")
                active = False
                break

            x = random.randint(100,150)
            y = random.randint(100,150)
            pag.moveTo(x,y,0.5)
            pag.keyDown('f13')
            pag.keyUp('f13')
            current_position = pag.position()
            time.sleep(movement_timer) #Move every ... sec

if __name__ == "__main__":
    main()

# #Run the following command in the terminal to create executable:
# pyinstaller --name afk main.py
