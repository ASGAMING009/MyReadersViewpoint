import time
import Stigma
import json



def save_game():
    save_data = {
        "Inventory": Inventory,
        "Items": Items,
        "health": health,
        "coins": coins,
        "sponsor": sponsor,
        "stigma": stigma.name if isinstance(stigma, Stigma.Stigma) else stigma,
        "companions": companions,
        "current_scene": current_scene
    }
    with open("savegame.json", "w") as file:
        json.dump(save_data, file)
    
    print("\n[System: Game Progress Saved Successfully!]")
    time.sleep(2)





def load_game():
    global Inventory, Items, health, coins, sponsor, stigma, companions, current_scene
    try:
        with open("savegame.json", "r") as file:
            save_data = json.load(file)
        Inventory = save_data["Inventory"]
        Items = save_data["Items"]
        companions = save_data["companions"]
        health = save_data["health"]
        coins = save_data["coins"]
        sponsor = save_data["sponsor"]
        current_scene = save_data["current_scene"]
        saved_stigma = save_data["stigma"]
        if saved_stigma == "Lightning Transformation":
            stigma = Stigma.Wukong_power
        elif saved_stigma == "Hellfire":
            stigma = Stigma.Uriel_power
        elif saved_stigma == "[Plotter's Insight]":
            stigma = Stigma.Plotter_power
        elif saved_stigma == "Black Flame":
            stigma = Stigma.Abyssal_power
        else:
            stigma = Stigma.No_power
            
        print("\n[System: Game Loaded Successfully!]")
        time.sleep(2)
    except FileNotFoundError:
        print("\n[System: No saved game found.]")
        time.sleep(2)



#My Variables
Inventory: list[str] = ["chocolate"]
Items: list[str] = ["phone"]
health = 100
coins = 0
sponsor = "None"
stigma = "None"
companions: list[str] = []



def check_stats():
    print("\n=== SYSTEM STATUS ===")
    print(f"Health: {health}/100")  
    print(f"Coins: {coins}") 
    print(f"Sponsor: {sponsor}")
    print(f"Stigma: {stigma}")
    print(f"Companions: {', '.join(companions) if companions else 'None'}")
    time.sleep(3)



stigma = Stigma.No_power