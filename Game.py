import time
#Global variables
Inventory: list[str] = ["chocolate"]
Items: list[str] = ["phone"]
health = 100
coins = 0
stigma = "None"
companions: list[str] = []

def show_logo():
    print("""
   ╔══════════════════════════════════════════════════════════════╗
   ║                                                              ║
   ║       ███╗   ███╗██╗   ██╗██████╗ ███████╗ █████╗ ██████╗    ║
   ║       ████╗ ████║╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔══██╗   ║
   ║       ██╔████╔██║ ╚████╔╝ ██████╔╝███████╗███████║██║  ██║   ║
   ║       ██║╚██╔╝██║  ╚██╔╝  ██╔══██╗╚════██║██╔══██║██║  ██║   ║
   ║       ██║ ╚═╝ ██║   ██║   ██║  ██║███████║██║  ██║██████╔╝   ║
   ║       ╚═╝     ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝    ║
   ║                                                              ║
   ║                     MyReadersViewpoint                       ║
   ║                    [ An ORV Fan Game ]                       ║
   ║                                                              ║
   ║          📖✨  THE OMNISCIENT EYE IS WATCHING  ✨🚇          ║
   ║                                                              ║
   ╚══════════════════════════════════════════════════════════════╝
    """)
def start_menu():
    while True:
        show_logo()
        print("1. Start New Game")
        print("2. Check Stats")
        print("3. Exit")
        Start_choice: str= input("Please Choose One:")
        if Start_choice == "1":
            print("Starting A new game...")
            return
        elif Start_choice == "2":
            check_stats()
            input("Press enter to go back")
        elif Start_choice == "3":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid choice. Please try again.")
            start_menu()

def check_stats():
    print("\n=== SYSTEM STATUS ===")
    print(f"Health: {health}/100")
    print(f"Coins: {coins}")
    print(f"Stigma: {stigma}")
    print(f"Companions: {', '.join(companions) if companions else 'None'}")
    print("Inventory:")
    for item in Inventory:
        print("- " + item)
    print("=====================\n")
def prologue():
    print("Hello Fellow Reader")
    time.sleep(1)
    print("\nWelcome to the Game")
    time.sleep(1)
    name: str= input("\nWhat is your name? ")
    time.sleep(1)
    print("Hello " + name + "!" )
    time.sleep(1)
    age: str= input("\nHow old are you? ")
    time.sleep(1)
    print("Wow! " + age + " is a great age to play this game!")
    time.sleep(1)
    print("\nThis is a game where you will be given decisions to choose from and this will effect the game and its ending and the characters.")
    ready: str = input("Are you ready to play? (yes/no) ")
    if ready.lower() == "yes":
        time.sleep(1)
    print("Great! Let's get started.")
    if ready.lower() == "no":
            print("No worries! Come back when you're ready.")
    while ready.lower() != "yes":
        ready: str = input("are you ready now?")
    if ready.lower() == "yes":
        print("\nGreat You're Ready!")
        input("\nPress enter to continue...")
        time.sleep(1.5)
        print("\nchoose your first item from the list: ",Items)
        chosen_item: str = input("Type the item you want to choose: ")
        if chosen_item in Items:
            print("You have chosen: " + chosen_item)
            Inventory.append(chosen_item)
            time.sleep (1)
            print(chosen_item + " added to your inventory")
            time.sleep(1)
            for item in Inventory:
                print("- " + item)
    time.sleep(5)              
    print("\nYou have completed the first part of the game! Congratulations!")
    time.sleep(7)
def first_scenario():
    print("\nYou are currently in a metro going home from work...")
    time.sleep(5)
    print("\nYou're currently reading a novel, its called Omniscient Readers Viewpoint")
    time.sleep(5)
    print("\nWhile reading it you closed your eyes and wished for it to become reality....")
    time.sleep(5)
    print("\nA window pops up right in front of you and it says 'Do you wish to make the novel become a reality?'")
    user_input: str = input("yes or no?")
    while user_input.lower() != "yes":
        user_input: str = input("Window still asks 'yes' or 'no'? ")
    if user_input.lower() == "yes":
        print("\nYou have chosen to make the novel become a reality!")
        time.sleep(1)
        print("\n The metro stops and everyone is talking about why the metro stopped and you are confused as well")
        time.sleep(5)
        print("\nYou looked in to your phone and see a notfication that open in email with the following message: here is the link to the novel, hope this helpes you during the adventure: https://www.webtoons.com/en/action/omniscient-reader/list?title_no=2154")
def dokkaebi_arrival():
    global health, coins
    print("\nSparks of blue electricity suddenly crackle in the air. The metro lights flicker and die.")
    time.sleep(5)
    print("Out of thin air, a small, fluffy creature with a single horn floats down from the ceiling.")
    print("It looks like a cute mascot, but its eyes are completely cold.")
    time.sleep(5)
    
    print("\n[Dokkaebi] 'Ah, ah. Does the mic work? Humans, your free trial of life has ended.'")
    time.sleep(3)
    print("\nA man in a business suit yells, 'Is this a hidden camera show? I have a meeting to get to!'")
    time.sleep(5)
    print("The Dokkaebi sighs and snaps its fingers. The businessman's head suddenly explodes with a loud pop.")
    print("The train goes dead silent.")
    time.sleep(5)

    print("\nA glowing blue system window appears in front of your eyes:")
    time.sleep(3)
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
    time.sleep(5)
    
    print("\nWhat do you do?")
    print("1. Search for the boy with the insect collection box.")
    print("2. Grab the item from your inventory and prepare to fight the man next to you.")
    print("3. Freeze in panic and do nothing.")

    action = input("\nEnter 1, 2, or 3: ")

    if action == "1":
        coins += 300
        print("\nYou lunge for the insect box! You grab a grasshopper and crush it.")
        time.sleep(5)
        print("\n[You have killed a living organism.]")
        time.sleep(5)
        print("\n[You have cleared the First Scenario!]")
        print("\n[You have been rewarded with 300 coins.]") 
        print("Total Coins: " + str(coins))
    elif action == "2":
        print("\nYou try to fight, but it's absolute chaos. You take a severe beating in the brawl.")
        time.sleep(5)
        health -= 50
        print(f"*** You took 50 damage! Current Health: {health}/100 ***")
        print("[Your health has drastically decreased.]")
        time.sleep(5)
        print("\nYou barely manage to survive as the time runs out...")
    else:
        print("\nYou stand perfectly still, paralyzed by fear. The 30-minute timer hits zero.")
        time.sleep(5)
        health = 0
        print(f"*** Current Health: {health}/100 ***")
        print("\n[Time is up. Penalty: Death.]")
        print("\n--- GAME OVER ---")
        quit()
def sponsor_selection():
    global sponsor, stigma
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
        sponsor = "Prisoner of the Golden Headband"
        stigma = "[Lightning Transformation]" 
        print(f"\nYou have chosen {sponsor}!")
        time.sleep(2)
        print(f"The constellation looks upon you with a grin. They are thrilled by your choice and gift you the Stigma: [{stigma}]!")
    
    elif choice == "2":
        sponsor = "Demon-like Judge of Fire"
        stigma = "[Hellfire]"
        print(f"\nYou have chosen {sponsor}!")
        time.sleep(2)
        print(f"The constellation sheds tears of joy at your righteous heart. They happily bless you with the Stigma: [{stigma}]!")
    
    elif choice == "3":
        sponsor = "Secretive Plotter"
        stigma = "[Plotter's Insight]"
        print(f"\nYou have chosen {sponsor}!")
        time.sleep(2)
        print(f"The constellation chuckles in the dark. They find you highly amusing and grant you the Stigma: [{stigma}].")
    
    elif choice == "4":
        sponsor = "Abyssal Black Flame Dragon"
        stigma = "[Black Flame]"
        print(f"\nYou have chosen {sponsor}!")
        time.sleep(2)
        print(f"The constellation roars with dark excitement. They welcome your destructive spirit and bestow the Stigma: [{stigma}]!")
    
    else:
        print("\n[You have chosen not to select a sponsor.]")
        stigma = "None"
        time.sleep(3)
        print("You have read the story, so you know you can select a greater constellation later, or maybe become one yourself...")

def metro_aftermath():
    print("\n--- SCENE 5: THE AFTERMATH ---")
    time.sleep(2)
    print("The sponsor selection ends. The heavy pressure in the air lifts.")
    print("You look around the bloodied carriage. Only a few survived.")
    time.sleep(3)
    
    print("\nA young woman with brown hair approaches you nervously. It's Yoo Sangah from your office.")
    print("Behind her, a small boy is clutching a crushed insect box. His name is Lee Gilyoung.")
    
    companions.append("Yoo Sangah")
    companions.append("Lee Gilyoung")
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
            check_stats()
            
        elif action == "4":
            print("\nInventory:")
            for item in Inventory:
                print("- " + item)
            time.sleep(2)
            
        elif action == "5":
            print("\nYou decide it's time to face the ruined world outside.")
            time.sleep(2)
            # CHALLENGE 3: What command do you use here to escape this 'while True' loop 
            # so the code can move on to the next scene?
            return
        else:
            print("Invalid choice. Try again.")

start_menu()
prologue()
first_scenario()
dokkaebi_arrival()
check_stats()
sponsor_selection()
metro_aftermath()