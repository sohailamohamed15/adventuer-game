import time
import random
# using the list for random choice
weapon_list = [
               "knife",
               "gun",
               "AMW",
               "scar",
               "rocket"]
# the function printing the messages and make a duration between them


def print_pause(m):
    print(m)
    time.sleep(2)
# this string help us not t repating this sentences every time
fail = "i do not understand you!"


def intro():  # an intro to our game
    print_pause("You want to discover the outer space! \n")
    print_pause("Milky way galaxy is such a beautiful place. \n")
    print_pause("WARNING:there are alot of aliens on the planets! \n")
    print_pause("You are a cleaver HERO you will fight all the ALIENS.. \n")
# first the player choose if he want to sacrified and go to mars or stay safe


def reach_planets():
    print_pause("You find yourself in the space between the solar system!")
    print_pause("In front of you the 2 planets.")
    print_pause("Enter 1 to go to Mars")
    print_pause("Enter 2 to go to Earth")
    que = input("please enter 1 or 2! \n").lower()
    print_pause(que)
    if que == "1":
        mars()
    elif que == "2":
        earth()
    else:
        print_pause(fail)
        reach_planets()
# second if the player chooses mars he will find something strange


def mars():
    print_pause("Ok it was a hard choice \n")
    print_pause("Now there is a strange voice from this way \n")
    print_pause("CHOOSE yor decision dude!! \n")
    print_pause("a)you want to go back to earth. \n ")
    print_pause("b)you want to follow the sound \n")
    que = input("please enter a or b! \n").lower()
    print_pause(que)
    if que == "a":
        earth()
    elif que == "b":
        sound()
    else:
        print_pause(fail)
        mars()
# player chooses earth,go fishing or he will get bored and return to mars


def earth():
    print_pause("there is too much safe here,nice chioce \n")
    print_pause("Go fishing an good idea, you want to chill out! \n")
    print_pause("a)you want to go fishing \n")
    print_pause("b)you want to go to mars\n")
    que = input("please enter a or b! \n").lower()
    print_pause(que)
    if que == "a":
        go_fishing()
    elif que == "b":
        mars()
    else:
        print_pause(fail)
        earth()
# if the player follow the sound,will find the alien he can fight it or gofar


def sound():
    print_pause("You are so brave man! \n")
    print_pause("oh,It is an ALINE \n")
    print_pause("a)You want to fight the alien? \n")
    print_pause("b)you want to go to the earth. \n")
    que = input("please enter a or b! \n").lower()
    print_pause(que)
    if que == "a":
        fight()
    elif que == "b":
        earth()
    else:
        print_pause(fail)
        sound()
# if the player wants to fight the alien he can pick a weapon randomly


def fight():
    print_pause("Now you go to destroy the alien!!! \n")
    print_pause("pick up your weapon quickly.. \n")
    print_pause("then , you have caught a"+random.choice(weapon_list)+"! \n")
    print_pause("you achive your goal and be a strong HERO! \n")
    again()
# if the player become chooses to stay on earth,go fising he achive anything


def go_fishing():
    print_pause("MMM.a good idea but its too much boring! \n")
    print_pause("you become bored and sad.. \n")
    print_pause("you donot achive your goal and you become depreseed\n")
    again()
# this function that give the player the chance to replay


def again():
    que = input("Do you want to play again ? (y/n) \n").lower()
    print_pause(que)
    if que == "y":
        play_the_game()
    elif que == "n":
        print_pause("Nice , hope you enjoy!")
    else:
        print_pause(fail)
        again()


def play_the_game():  # this function starts the game
    intro()
    reach_planets()
play_the_game()
