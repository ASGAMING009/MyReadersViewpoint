import time
import sys
import Scenario1
import Scenario2
import gamedata
import json

def show_logo():
    print("""
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                                ║
    ║                  ███╗   ███╗██████╗ ██╗   ██╗                  ║
    ║                  ████╗ ████║██╔══██╗██║   ██║                  ║
    ║                  ██╔████╔██║██████╔╝██║   ██║                  ║
    ║                  ██║╚██╔╝██║██╔══██╗╚██╗ ██╔╝                  ║
    ║                  ██║ ╚═╝ ██║██║  ██║ ╚████╔╝                   ║
    ║                  ╚═╝     ╚═╝╚═╝  ╚═╝  ╚═══╝                    ║
    ║                                                                ║
    ║          [ M Y  R E A D E R ' S  V I E W P O I N T ]           ║
    ║                     - An ORV Fan Game -                        ║
    ║                                                                ║
    ║           📖✨ THE OMNISCIENT EYE IS WATCHING ✨🚇           ║
    ║                                                                ║
    ╚════════════════════════════════════════════════════════════════╝
    """)

def start_menu():
    while True:
        show_logo()
        print("1. Start New Game")
        print("2. Load Game")
        print("3. Check Stats")
        print("4. Exit")
        Start_choice = input("\nPlease Choose One: ")
        
        if Start_choice == "1":
            print("Starting a new game...")
            return
        elif Start_choice == "2":
            gamedata.load_game()
            return
        elif Start_choice == "3":
            gamedata.check_stats()
            input("Press enter to go back")
        elif Start_choice == "4":
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def check_stats():
    print("\n=== SYSTEM STATUS ===")
    print(f"Health: {gamedata.health}/100")
    print(f"Coins: {gamedata.coins}")
    print(f"Stigma: {gamedata.stigma}")
    print(f"Companions: {', '.join(gamedata.companions) if gamedata.companions else 'None'}")
    print("Inventory:")
    for item in gamedata.Inventory:
        print("- " + item)
    print("=====================\n")

def prologue():
    print("Hello Fellow Reader")
    time.sleep(1)
    print("\nWelcome to the Game")
    time.sleep(1)
    name: str = input("\nWhat is your name? ")
    time.sleep(1)
    print("Hello " + name + "!" )
    time.sleep(1)
    age: str = input("\nHow old are you? ")
    time.sleep(1)
    print("Wow! " + age + " is a great age to play this game!")
    time.sleep(1)
    print("\nThis is a game where you will be given decisions to choose from and this will effect the game and its ending and the characters.")
    
    ready: str = input("Are you ready to play? (yes/no) ")
    if ready.lower() == "no":
        print("No worries! Come back when you're ready.")
        while ready.lower() != "yes":
            ready = input("Are you ready now? ")
            
    if ready.lower() == "yes":
        print("\nGreat You're Ready!")
        input("\nPress enter to continue...")
        time.sleep(1.5)
        print(f"\nchoose your first item from the list: {gamedata.Items}")
        chosen_item: str = input("Type the item you want to choose: ")
        
        if chosen_item in gamedata.Items:
            print("You have chosen: " + chosen_item)
            gamedata.Inventory.append(chosen_item)
            time.sleep (1)
            print(chosen_item + " added to your inventory")
            time.sleep(1)
            for item in gamedata.Inventory:
                print("- " + item)
    time.sleep(3)              
    print("\nYou have completed the first part of the game! Congratulations!")
    time.sleep(3)





start_menu()


if gamedata.current_scene == "prologue":
    prologue()
    Scenario1.first_scenario()
    Scenario1.dokkaebi_arrival()
    Scenario1.check_stats()
    Scenario1.sponsor_selection()

gamedata.current_scene = "metro_aftermath"


if gamedata.current_scene == "metro_aftermath":
    Scenario1.metro_aftermath()
    
    gamedata.current_scene = "bridge"


if gamedata.current_scene == "bridge":
    Scenario2.bridge_crossing()