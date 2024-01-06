import pyautogui
from time import sleep
from random import randint, uniform


# Go to Falador west bank
# To begin stand in front of the 3rd bank teller from the left, point camera north
# Zoom camera completely out and press up on arrows to move camera up all the way


sleep(3)
x, y = pyautogui.position()


def move_and_click(x_cor, y_cor):
    """Basic framework for a mouse movement with random intervals between
    mouse movement and clicks. Takes input for x and y coordinates"""
    pyautogui.moveTo(x_cor, y_cor)
    sleep(uniform(.5, 1.3))
    pyautogui.click()


def wait_cut():
    """Function to move the move around and right click on screen at random times, and to wait
    while chopping."""
    sleep(randint(7, 9))
    pyautogui.moveTo(randint(200, 900), randint(200, 600))
    pyautogui.rightClick()


def chopping_wood():
    """Function for clicking on spot to resume chopping upon level or tree is chopped down
    and waiting while chopping, cycles 3 times"""
    for _ in range(3):
        move_and_click(randint(908, 912), randint(518, 522))  # check tree
        wait_cut()
        sleep(randint(10, 15))


# Main loop
while True:
    # Go to Tree
    move_and_click(randint(648, 652), randint(258, 264))
    sleep(randint(20, 30))

    # Main chopping function
    chopping_wood()

    # Go to bank
    move_and_click(1830, 155)
    sleep(randint(5,7))
    move_and_click(960, 570)
    sleep(randint(1, 3))
    move_and_click(1015, 823)
    sleep(randint(3, 5))
    move_and_click(655, 250)
    sleep(randint(1, 3))
    move_and_click(1055, 70)
    sleep(randint(1,3))
