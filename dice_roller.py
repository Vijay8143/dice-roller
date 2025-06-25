import os
import random
import time
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def rolling_animation():
    animation = ["Rolling", "Rolling.", "Rolling..", "Rolling..."]
    for frame in animation:
        sys.stdout.write("\r" + frame)
        sys.stdout.flush()
        time.sleep(0.4)
    print("\n")

def roll_dice():
    while True:
        input("🎲 Press Enter to roll the dice (Ctrl+C to quit)...")
        clear_screen()
        rolling_animation()
        result = random.randint(1, 6)
        print(f"🎉 You rolled a {result}!\n")

if __name__ == "__main__":
    clear_screen()
    roll_dice()
