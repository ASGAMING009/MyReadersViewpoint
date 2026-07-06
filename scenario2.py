import time
import sys
import gamedata
import Stigma

def bridge_crossing():
    print("\n" + "="*50)
    print("--- SCENE 6: THE HAN RIVER BRIDGE ---")
    print("="*50 + "\n")
    time.sleep(2)
    
    print("With a heavy groan, the metro doors finally slide open.")
    print("You step out onto the tracks of the Dongho Bridge. The cold night wind hits your face.")
    time.sleep(3)
    
    print("\nYoo Sangah gasps behind you. 'Oh my god... Seoul... it's...'\n")
    time.sleep(2)
    
    print("The city you knew is gone. Plumes of black smoke rise from skyscrapers.")
    print("Military helicopters fall from the red sky, engulfed in flames.")
    print("The world has truly come to an end.")
    time.sleep(4)
    
    print("\nSuddenly, the entire bridge shakes violently!")
    time.sleep(2)
    print("You look down at the dark Han River below. A massive shadow is moving under the water.")
    print("With a deafening roar, a colossal sea monster  an Ichthyosaur  bursts from the surface!")
    print("Its massive jaws snap shut in the air, narrowly missing the bridge before crashing back down.")
    time.sleep(5)
    
    print("\nSparks fly in the air. The Dokkaebi floats above the panicked survivors.")
    print("[Dokkaebi] 'Hahaha! Isn't the view great? Now, let's not waste time.'")
    time.sleep(3)
    
    print("\n=========================================")
    print("[SUB SCENARIO - ESCAPE]")
    print("Category: Sub")
    print("Difficulty: D")
    print("Clear Condition: Cross the broken section of the bridge and reach the safe zone.")
    print("Time Limit: 20 minutes")
    print("Reward: 200 Coins")
    print("Penalty for Failure: Eaten by the Ichthyosaur")
    print("=========================================\n")
    time.sleep(4)
    
    print("You look ahead. About 50 meters away, a massive chunk of the bridge is completely missing.")
    print("Below the gap, the Ichthyosaur is swimming in circles, waiting for anyone to fall.")
    time.sleep(3)
    
    print("\nA group of thugs from the next train car notice the gap.")
    print("Their leader points at Yoo Sangah and Lee Gilyoung.")
    print("Thug Leader: 'Hey you! Throw the woman and the kid in! If the monster eats them, we can jump across while it's distracted!'")
    time.sleep(4)
    
    print("\nYoo Sangah steps back in fear. Lee Gilyoung grabs the edge of your shirt.")
    print("The Constellations are watching you closely. What do you do?")
    time.sleep(2)

    
    print(f"\n1. [Unleash Stigma {gamedata.stigma}] - Use the power your Constellation gave you to fight the thugs.")
    print("2. [Ruthless Survival] - Push the Thug Leader into the river to distract the monster.")
    print("3. [Deus Ex Machina] - Stand your ground and wait for the Constellations to create a bridge of light.")
    
    choice = input("\nEnter 1, 2, or 3: ")
    
    if choice == "1":
        print("\nYou step in front of your companions, your eyes glowing with the power of your Constellation.")
        time.sleep(3)
        
       
        print("\n" + "="*40)
        gamedata.stigma.use()  
        print("="*40 + "\n")
        time.sleep(4)
        
        if gamedata.stigma.name == "None":
            print("Wait... you don't have a Stigma! Absolutely nothing happens!")
            time.sleep(3)
            print("The thugs laugh at your dramatic pose.")
            print("The Thug Leader walks over and shoves you off the broken bridge.")
            time.sleep(3)
            print("The Ichthyosaur opens its massive jaws...")
            print("\n--- GAME OVER ---")
            sys.exit()
            
        else:
            print("The raw power slams into the thugs, throwing them backward.")
            print("The Constellations in your channel cheer at the brilliant display of power!")
            time.sleep(4)
            print("While the thugs are down, a glowing bridge of light—a Deus Ex Machina—suddenly materializes across the gap!")     
    elif choice == "2":
        print("\nYou don't hesitate. You grab the Thug Leader by the collar and hurl him off the edge!")
        time.sleep(3)
        print("He screams as he falls. The Ichthyosaur leaps from the water and swallows him whole.")
        print("Some Constellations are disturbed by your ruthlessness, but others toss you coins in amusement.")
        time.sleep(4)
        print("While the monster is distracted, you notice a thin, glowing bridge of light forming across the gap.")
        
    elif choice == "3":
        print("\nYou stare down the thugs, completely unbothered. You know the rules of this world.")
        time.sleep(3)
        print("You look up at the sky and smirk.")
        print("[The Constellation 'Secretive Plotter' is impressed by your composure.]")
        print("[A Constellation has sponsored a 'Deus Ex Machina' - Bridge of Light!]")
        time.sleep(4)
        print("A radiant bridge made of pure energy shoots across the gap, blinding the thugs.")
        
    else:
        print("\nYou hesitate. In this ruined world, hesitation is death.")
        time.sleep(3)
        print("The bridge crumbles beneath your feet. You fall into the dark waters below.")
        print("The Ichthyosaur opens its massive jaws...")
        time.sleep(2)
        print("\n--- GAME OVER ---")
        sys.exit()

    time.sleep(3)
    print("\nYou grab Yoo Sangah and Lee Gilyoung, sprinting across the bridge of light.")
    print("You reach the other side just as the light shatters into a million pieces.")
    time.sleep(3)
    print("\n[You have cleared the Sub Scenario!]")
    print("[You have been rewarded with 200 coins.]")
    time.sleep(2)
    gamedata.current_scene = "Scenario3"
    
    save_opt = input("\n[System: Would you like to save your game? (yes/no)]: ")
    if save_opt.lower() == "yes":
        gamedata.save_game()
    time.sleep(2)
    print("\nWelcome to the ruined world, Reader.")
    # End of scenario 2