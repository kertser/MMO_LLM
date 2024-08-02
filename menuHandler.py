from bots import *
from actions import GameActions as Ga
import json

def print_title():
    print(r"""
         /$$                               /$$ /$$               /$$$$$$  /$$                                                /$$                                /$$$$$$                        /$$                         /$$ /$$                    
        | $$                              |__/| $/              /$$__  $$| $$                                               | $$                               /$$__  $$                      | $$                        | $$| $$                    
        | $$       /$$   /$$ /$$$$$$/$$$$  /$$|_//$$$$$$$      | $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$  /$$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ | $$| $$  /$$$$$$   /$$$$$$ 
        | $$      | $$  | $$| $$_  $$_  $$| $$  /$$_____/      | $$      | $$__  $$ |____  $$ /$$__  $$|____  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$      | $$       /$$__  $$| $$__  $$|_  $$_/   /$$__  $$ /$$__  $$| $$| $$ /$$__  $$ /$$__  $$
        | $$      | $$  | $$| $$ \ $$ \ $$| $$ |  $$$$$$       | $$      | $$  \ $$  /$$$$$$$| $$  \__/ /$$$$$$$| $$        | $$    | $$$$$$$$| $$  \__/      | $$      | $$  \ $$| $$  \ $$  | $$    | $$  \__/| $$  \ $$| $$| $$| $$$$$$$$| $$  \__/
        | $$      | $$  | $$| $$ | $$ | $$| $$  \____  $$      | $$    $$| $$  | $$ /$$__  $$| $$      /$$__  $$| $$        | $$ /$$| $$_____/| $$            | $$    $$| $$  | $$| $$  | $$  | $$ /$$| $$      | $$  | $$| $$| $$| $$_____/| $$      
        | $$$$$$$$|  $$$$$$/| $$ | $$ | $$| $$  /$$$$$$$/      |  $$$$$$/| $$  | $$|  $$$$$$$| $$     |  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$$| $$            |  $$$$$$/|  $$$$$$/| $$  | $$  |  $$$$/| $$      |  $$$$$$/| $$| $$|  $$$$$$$| $$      
        |________/ \______/ |__/ |__/ |__/|__/ |_______/        \______/ |__/  |__/ \_______/|__/      \_______/ \_______/   \___/   \_______/|__/             \______/  \______/ |__/  |__/   \___/  |__/       \______/ |__/|__/ \_______/|__/   
        """)

def print_menu():
    """Print the available actions."""

    print("What would you like to do?")
    print("1. Move Character    |   2. Perform Fight Loop      |   3. Crafting")
    print("4. Gathering         |   5. Check Character Status  |   6. Unequip")
    print("7. Deposit Bank Item |   8. Deposit Gold            |   9. Withdraw Bank Item")
    print("10. Withdraw Gold    |   11. Buy GE                 |   12. Sell GE")
    print("13. New Task         |   14. Complete Task          |   15. Task Exchange")
    print("16. Delete Item      |   17. Activate Bot           |   18. Exit\n")
def get_int_input(prompt):
    """Get integer input from the user."""
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_int_input(prompt)

def get_string_input(prompt):
    """Get string input from the user."""
    return input(prompt).strip()

def handle_move(character_name):
    """Handle movement input and call the move_character function."""
    x = get_int_input("Enter new x coordinate: ")
    y = get_int_input("Enter new y coordinate: ")
    return Ga.move_character(character_name, x, y)

def handle_fight(character_name):
    """Call the perform_fight function."""
    return Ga.perform_fight(character_name)

def handle_crafting(character_name):
    """Handle crafting input and call the crafting function."""
    item_code = get_string_input("Enter item code: ")
    quantity = get_int_input("Enter quantity: ")
    return Ga.crafting(character_name, item_code, quantity)

def handle_gathering(character_name):
    """Call the gathering function."""
    return Ga.gathering(character_name)

def handle_unequip(character_name):
    """Handle unequip input and call the unequip function."""
    slot = get_string_input("Enter the slot to unequip (e.g., weapon): ")
    return Ga.unequip(character_name, slot)

def handle_deposit_bank(character_name):
    """Handle deposit bank input and call the deposit_bank function."""
    code = get_string_input("Enter item code: ")
    quantity = get_int_input("Enter quantity: ")
    return Ga.deposit_bank(character_name, code, quantity)

def handle_deposit_gold(character_name):
    """Handle deposit gold input and call the deposit_gold function."""
    quantity = get_int_input("Enter quantity: ")
    return Ga.deposit_gold(character_name, quantity)

def handle_withdraw_bank(character_name):
    """Handle withdraw bank input and call the withdraw_bank function."""
    code = get_string_input("Enter item code: ")
    quantity = get_int_input("Enter quantity: ")
    return Ga.withdraw_bank(character_name, code, quantity)

def handle_withdraw_gold(character_name):
    """Handle withdraw gold input and call the withdraw_gold function."""
    quantity = get_int_input("Enter quantity: ")
    return Ga.withdraw_gold(character_name, quantity)

def handle_buy_ge(character_name):
    """Handle buy GE input and call the buy_ge function."""
    code = get_string_input("Enter item code: ")
    quantity = get_int_input("Enter quantity: ")
    price = get_int_input("Enter price: ")
    return Ga.buy_ge(character_name, code, quantity, price)

def handle_sell_ge(character_name):
    """Handle sell GE input and call the sell_ge function."""
    code = get_string_input("Enter item code: ")
    quantity = get_int_input("Enter quantity: ")
    price = get_int_input("Enter price: ")
    return Ga.sell_ge(character_name, code, quantity, price)

def handle_new_task(character_name):
    """Call the new_task function."""
    return Ga.new_task(character_name)

def handle_complete_task(character_name):
    """Call the complete_task function."""
    return Ga.complete_task(character_name)

def handle_task_exchange(character_name):
    """Call the task_exchange function."""
    return Ga.task_exchange(character_name)

def handle_delete_item(character_name):
    """Handle delete item input and call the delete_item function."""
    code = get_string_input("Enter item code: ")
    quantity = get_int_input("Enter quantity: ")
    return Ga.delete_item(character_name, code, quantity)

def handle_check_character_status(character_name):
    """Handle character status check input and call the get_character_status function."""
    status = Ga.get_character_status(character_name)
    print(json.dumps(status, indent=2))
    return status


def activate_bot(character_name):
    print("Select a bot to activate:")
    print("1. Mob Slayer Bot    |   2. Ore Mining Mob")
    # Add more bots as needed
    bot_option = int(input("Enter the bot number: "))

    if bot_option == 1:
        number_of_mobs = int(input("Enter the number of mobs to kill: "))
        kill_bot(character_name, number_of_mobs)

    elif bot_option == 2:
        number_of_resources = int(input("Enter the number of resources to mine: "))
        mine_bot(character_name, number_of_resources)
    else:
        print("Invalid bot selection.")
