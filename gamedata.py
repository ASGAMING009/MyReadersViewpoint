import time
import Stigma


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