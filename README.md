# Omniscient Reader's Viewpoint - Terminal RPG 🚇✨

A text-based Role Playing Game built in Python, inspired by the hit web novel/manhwa *Omniscient Reader's Viewpoint* (ORV). 

Survive the apocalypse, choose your Constellation sponsor, and wield powerful Stigmas in this interactive narrative adventure.

## 🌟 Features
* **Interactive Storyline:** Make critical choices that determine your survival in the First Scenario and beyond.
* **Dynamic Sponsor System:** Choose a Constellation (like the *Demon-like Judge of Fire* or *Secretive Plotter*) to receive unique, dynamically-loaded powers.
* **Object-Oriented Combat:** Wield custom Stigma classes that change the narrative flavor of your battles.
* **Persistent Save System:** Built-in JSON save/load functionality with a "Story Director" that tracks your exact chapter and scene progress.
* **Companion System:** Recruit familiar faces from the novel like Yoo Sangah and Lee Gilyoung.

## 📂 Project Structure
This game uses a modular, multi-file architecture:
* `game.py` - The main game loop, story director, and initial scenarios.
* `Scenario2.py` - Subsequent chapters (e.g., The Bridge Crossing).
* `gamedata.py` - The central Data Vault handling inventory, stats, and the JSON save/load logic.
* `Stigma.py` - The OOP blueprint and registry for Constellation powers.

## 🚀 How to Play

**Prerequisites:** Make sure you have [Python 3.x](https://www.python.org/downloads/) installed.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ASGAMING009/MyReadersViewpoint.git](https://github.com/ASGAMING009/MyReadersViewpoint.git)
Navigate to the project folder:

'''bash 
cd MyReadersViewpoint
Run the game:

'''bash
python game.py


💾 Saving and Loading
To save your progress, wait until you reach a safe "Hub Area" (like the Metro Aftermath) and select the Save Game option from the menu. Your progress will be written to orv_save.json.

To load, simply launch game.py and select Load Game from the main menu. The Story Director will instantly teleport you back to your exact scene with all your Stigmas and items intact.

“There are three ways to survive in a ruined world. Now, I have forgotten a few, but one thing is certain: the fact that you who are reading this now will survive.”# Omniscient Reader's Viewpoint - Terminal RPG 🚇✨
