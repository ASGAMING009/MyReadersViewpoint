import time
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
    print(f"Stigma: {stigma}")
    print(f"Companions: {', '.join(companions) if companions else 'None'}")
    print("Inventory:")
    for item in Inventory:
        print("- " + item)  
    print("=====================\n")
    time.sleep(3)
