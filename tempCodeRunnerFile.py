import time
Inventory: list[str] = ["chocolate"]
Items: list[str] = ["phone"]
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
    time.sleep(10)
def first_scenario():
    print("\nYou are currently in a metro going home from work...")
    time.sleep(5)
    print("\nYou're currently reading a novel, its called Omniscient Readers Viewpoint")
    time.sleep(5)
    print("\nYou are currently reading the novel and you are enjoying it very much")
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

