import config
import menuHandler as mH
import connect
from utilities import GameUtilities as Gu

def main():

    # Connect to API:
    client = connect.APIClient()

    # Print the title to CLI
    mH.print_title()

    # Get
    character_name = config.character_list[0]

    # Define characted actions:
    actions = {
        1: mH.handle_move, 2: mH.handle_fight, 3: mH.handle_crafting,
        4: mH.handle_gathering, 5: mH.handle_check_character_status, 6: mH.handle_unequip,
        7: mH.handle_deposit_bank, 8: mH.handle_deposit_gold, 9: mH.handle_withdraw_bank,
        10: mH.handle_withdraw_gold, 11: mH.handle_buy_ge, 12: mH.handle_sell_ge,
        13: mH.handle_new_task, 14: mH.handle_complete_task, 15: mH.handle_task_exchange,
        16: mH.handle_delete_item, 17: mH.activate_bot
    }


    choice = 0 # default value
    while (choice != 18):
        mH.print_menu() # Pop the list of menu titles
        # get the user choice
        choice = mH.get_int_input("Enter the number of your choice: ")

        # Choose the proper action, relevant by choice:
        if choice in actions.keys():
            actions[choice](character_name)
        elif choice == 18:
            print("Exiting the program.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()