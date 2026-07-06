import time
import sys
import Scenario2
import gamedata
import json


def first_scenario():
    print("\nYou are currently in a metro going home from work...")
    time.sleep(3)
    print("You're currently reading a novel, its called Omniscient Readers Viewpoint")
    time.sleep(3)
    print("While reading it you closed your eyes and wished for it to become reality....")
    time.sleep(3)
    print("\nA window pops up right in front of you and it says 'Do you wish to make the novel become a reality?'")
    
    user_input: str = input("yes or no? ")
    while user_input.lower() != "yes":
        user_input = input("Window still asks 'yes' or 'no'? ")
        
    if user_input.lower() == "yes":
        print("\nYou have chosen to make the novel become a reality!")
        time.sleep(1)
        print("\nThe metro screeches to a sudden halt. Everyone starts murmuring, confused by the delay.")
        time.sleep(3)
        
        # --- NEW HINTS ADDED HERE ---
        print("\nYou look around the carriage. Sitting a few seats away is Yoo Sangah from your company's HR department, looking worried.")
        time.sleep(3)
        print("Near the doors, you notice a young boy crouching down. He is clutching a small, plastic insect collection box.")
        print("An eerie sense of deja vu washes over you...")
        time.sleep(4)
        # ----------------------------
        
        print("\nYou look into your phone and see a notification that opens an email with the following message:")
        print("'Here is the link to the novel, hope this helps you during the adventure: https://www.webtoons.com/en/action/omniscient-reader/list?title_no=2154'")
        time.sleep(3)

def dokkaebi_arrival():
    print("\nSparks of blue electricity suddenly crackle in the air. The metro lights flicker and die.")
    time.sleep(3)
    print("Out of thin air, a small, fluffy creature with a single horn floats down from the ceiling.")
    print("It looks like a cute mascot, but its eyes are completely cold.")
    time.sleep(3)
    
    print("\n[Dokkaebi] 'Ah, ah. Does the mic work? Humans, your free trial of life has ended.'")
    time.sleep(3)
    print("\nA man in a business suit yells, 'Is this a hidden camera show? I have a meeting to get to!'")
    time.sleep(3)
    print("The Dokkaebi sighs and snaps its fingers. The businessman's head suddenly explodes with a loud pop.")
    print("The train goes dead silent.")
    time.sleep(3)

    print("\nA glowing blue system window appears in front of your eyes:")
    time.sleep(2)
    print("\n=========================================")
    print("[MAIN SCENARIO #1 - PROOF OF VALUE]")
    print("Category: Main")
    print("Difficulty: F")
    print("Clear Condition: Kill one or more living organisms.")
    print("Time Limit: 30 minutes")
    print("Reward: 300 Coins")
    print("Penalty for Failure: Death")
    print("=========================================\n")
    time.sleep(4)

    print("Panic erupts. People are screaming. Some are eyeing each other suspiciously.")
    print("Because you read the novel, you know a secret: you don't have to kill a human to pass.")
    time.sleep(3)
    
    print("\nWhat do you do?")
    print("1. Search for the boy with the insect collection box.")
    print("2. Grab the item from your inventory and prepare to fight the man next to you.")
    print("3. Freeze in panic and do nothing.")

    action = input("\nEnter 1, 2, or 3: ")

    if action == "1":
        gamedata.coins += 300
        print("\nYou lunge for the insect box! You grab a grasshopper and crush it.")
        time.sleep(3)
        print("\n[You have killed a living organism.]")
        time.sleep(2)
        print("\n[You have cleared the First Scenario!]")
        print("\n[You have been rewarded with 300 coins.]") 
        print("Total Coins: " + str(gamedata.coins))
    elif action == "2":
        print("\nYou try to fight, but it's absolute chaos. You take a severe beating in the brawl.")
        time.sleep(3)
        gamedata.health -= 50
        print(f"*** You took 50 damage! Current Health: {gamedata.health}/100 ***")
        print("[Your health has drastically decreased.]")
        time.sleep(3)
        print("\nYou barely manage to survive as the time runs out...")
    else:
        print("\nYou stand perfectly still, paralyzed by fear. The 30-minute timer hits zero.")
        time.sleep(3)
        gamedata.health = 0
        print(f"*** Current Health: {gamedata.health}/100 ***")
        print("\n[Time is up. Penalty: Death.]")
        print("\n--- GAME OVER ---")
        sys.exit()

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
    time.sleep(5)

def sponsor_selection():
    print("\n--- SCENE 4: SPONSOR SELECTION ---")
    time.sleep(2)
    print("\nThe blood in the train car hasn't even dried yet.")
    print("Suddenly, the air in the train car becomes incredibly heavy.")
    time.sleep(3)
    
    print("\n[The Sponsor Selection will now begin.]")
    time.sleep(2)
    print("\nA constellation is a god-like being that watches this broadcast.")
    print("Choosing a sponsor gives you their powers (Stigmas), but you become their puppet.")
    time.sleep(4)

    print("\nFour stars are shining brightly towards you:")
    print("1. [Prisoner of the Golden Headband] (Great Sun Wukong - High Attack)")
    print("2. [Demon-like Judge of Fire] (Archangel Uriel - Fire & Justice)")
    print("3. [Secretive Plotter] (Unknown - Strategy & Mystery)")
    print("4. [Abyssal Black Flame Dragon] (Chuunibyou Dragon - Pure Destruction)")
    print("5. [Skip Sponsor Selection] (No Sponsor - No Powers)")

    choice: str = input("\nEnter 1, 2, 3, 4, or 5: ")
    if choice == "1":
        gamedata.sponsor = "Prisoner of the Golden Headband"
        gamedata.stigma = "[Lightning Transformation]" 
        print(f"\nYou have chosen {gamedata.sponsor}!")
        time.sleep(2)
        print(f"The constellation looks upon you with a grin. They are thrilled by your choice and gift you the Stigma: {gamedata.stigma}!")
    
    elif choice == "2":
        gamedata.sponsor = "Demon-like Judge of Fire"
        gamedata.stigma = "[Hellfire]"
        print(f"\nYou have chosen {gamedata.sponsor}!")
        time.sleep(2)
        print(f"The constellation sheds tears of joy at your righteous heart. They happily bless you with the Stigma: {gamedata.stigma}!")
    
    elif choice == "3":
        gamedata.sponsor = "Secretive Plotter"
        gamedata.stigma = "[Plotter's Insight]"
        print(f"\nYou have chosen {gamedata.sponsor}!")
        time.sleep(2)
        print(f"The constellation chuckles in the dark. They find you highly amusing and grant you the Stigma: {gamedata.stigma}.")
    
    elif choice == "4":
        gamedata.sponsor = "Abyssal Black Flame Dragon"
        gamedata.stigma = "[Black Flame]"
        print(f"\nYou have chosen {gamedata.sponsor}!")
        time.sleep(2)
        print(f"The constellation roars with dark excitement. They welcome your destructive spirit and bestow the Stigma: {gamedata.stigma}!")
    
    else:
        print("\n[You have chosen not to select a sponsor.]")
        gamedata.stigma = "None"
        time.sleep(3)
        print("You have read the story, so you know you can select a greater constellation later, or maybe become one yourself...")

def metro_aftermath():
    print("\n--- SCENE 5: THE AFTERMATH ---")
    time.sleep(2)
    print("The sponsor selection ends. The heavy pressure in the air lifts.")
    print("You look around the bloodied carriage. Only a few survived.")
    time.sleep(3)
    
    print("\nA young woman with brown hair approaches you nervously. It's Yoo Sangah.")
    print("Behind her, the small boy is clutching the crushed insect box. His name is Lee Gilyoung.")
    
    gamedata.companions.append("Yoo Sangah")
    gamedata.companions.append("Lee Gilyoung")
    time.sleep(3)
    
    print("\n[Yoo Sangah and Lee Gilyoung have joined your party!]")
    time.sleep(2)

    while True:
        print("\nWhat would you like to do before the doors open?")
        print("1. Talk to Yoo Sangah")
        print("2. Talk to Lee Gilyoung")
        print("3. Check Stats")
        print("4. Check Inventory")
        print("5. Force the metro doors open and leave")
        
        action = input("\nChoose an action (1-5): ")
        
        if action == "1":
            print("\nYoo Sangah: 'I... I don't understand what's happening. Did you really know this would happen?'")
            time.sleep(2)
            print("You reassure her that as long as she sticks with you, she will survive.")
        
        elif action == "2":
            print("\nLee Gilyoung looks up at you silently. He seems completely unfazed by the blood.")
            time.sleep(2)
            print("He quietly hands you half of a candy bar. You pat his head.")
            
        elif action == "3":
            gamedata.check_stats()
            
        elif action == "4":
            print("\nInventory:")
            for item in gamedata.Inventory:
                print("- " + item)
            time.sleep(2)
            
        elif action == "5":
            print("\nYou decide it's time to face the ruined world outside.")
            time.sleep(2)
            break
        else:
            print("Invalid choice. Try again.")

