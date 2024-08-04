import time
from actions import *
import sys
import time


def kill_bot(character_name, number_of_monsters):
    defeated_monsters = 0

    while(defeated_monsters < number_of_monsters):
        cooldown = perform_fight(character_name)
        if (cooldown != 0):
            defeated_monsters += 1


        # Update the progress bar
        progress = defeated_monsters / number_of_monsters
        bar_length = 40  # Length of the progress bar in characters
        block = int(bar_length * progress)
        progress_bar = "#" * block + "-" * (bar_length - block)
        sys.stdout.write(f"\rProgress: [{progress_bar}] {defeated_monsters}/{number_of_monsters} chickens defeated")
        sys.stdout.flush()

        # Add a delay between actions to simulate realistic gameplay
        time.sleep(5)  # Adjust the delay as needed
    print('Hunting complete!')

def mine_bot(character_name, number_of_resources):
    resources_mined = 0

    while (resources_mined < number_of_resources):

        cooldown = gathering(character_name)
        if(cooldown != 0):
            resources_mined += 1

        # Update the progress bar
        progress = resources_mined / number_of_resources
        bar_length = 40  # Length of the progress bar in characters
        block = int(bar_length * progress)
        progress_bar = "#" * block + "-" * (bar_length - block)
        sys.stdout.write(f"\rProgress: [{progress_bar}] {resources_mined}/{number_of_resources} resources mined")
        sys.stdout.flush()

        # Add a delay between actions to simulate realistic gameplay
        time.sleep(cooldown)  # Adjust the delay as needed
    print("\nMining complete!")