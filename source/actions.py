import time
from connect import client  # Import the singleton client

class GameActions:
    """Class containing static methods for various game actions."""
    @staticmethod
    def move_character(character_name, x, y):
        """
        Move the character to a specified location.
        Args:
            character_name (str): The name of the character to move.
            x (int): The x-coordinate of the destination.
            y (int): The y-coordinate of the destination.
        Returns:
            dict: The response from the API.
        """
        endpoint = f"my/{character_name}/action/move"
        data = {"x": x, "y": y}
        response = client.post(endpoint, data)
        return response

    @staticmethod
    def perform_fight(character_name):
        """
        Engage the character in a fight.
        Args:
            character_name (str): The name of the character to perform the fight.
        Returns:
            int: The cooldown time in seconds, or 0 if an error occurs.
        """
        endpoint = f"my/{character_name}/action/fight"
        response = client.post(endpoint)

        if response is None:
            print("An error occurred during the fight.")
            return 0

        status = response.get("status")
        if status == 498:
            print("The character cannot be found on your account.")
        elif status == 497:
            print("Your character's inventory is full.")
        elif status == 499:
            print("Your character is in cooldown.")
        elif status == 598:
            print("No monster on this map.")
        else:
            data = response.get("data")
            if data:
                print(f"The fight ended successfully. You have {data['fight']['result']}.")
                cooldown = data['cooldown']['total_seconds']
                time.sleep(cooldown)
                return True
        return False

    @staticmethod
    def crafting(character_name, item_code, quantity):
        """
        Craft items using the specified character.
        Args:
            character_name (str): The name of the character to perform crafting.
            item_code (str): The code of the item to craft.
            quantity (int): The quantity of items to craft.

        Returns:
            dict: The response from the API.
        """
        endpoint = f"my/{character_name}/action/crafting"
        data = {"code": item_code, "quantity": quantity}
        response = client.post(endpoint, data)
        return response

    @staticmethod
    def gathering(character_name):
        """
        Gather resources using the specified character.
        Args:
            character_name (str): The name of the character to perform gathering.
        Returns:
            int: The cooldown time in seconds, or 0 if an error occurs.
        """
        endpoint = f"my/{character_name}/action/gathering"
        response = client.post(endpoint)

        if response is None:
            print("An error occurred during gathering.")
            return 0

        status = response.get("status")
        if status == 498:
            print("The character cannot be found on your account.")
        elif status == 497:
            print("Your character's inventory is full.")
        elif status == 499:
            print("Your character is in cooldown.")
        elif status == 493:
            print("The resource is too high-level for your character.")
        elif status == 598:
            print("No resource on this map.")
        else:
            data = response.get("data")
            if data:
                print("Your character successfully gathered the resource.")
                cooldown = data['cooldown']['total_seconds']
                time.sleep(cooldown)

        return response

    @staticmethod
    def get_character_status(character_name):
        """
        Retrieve the status of the specified character.
        Args:
            character_name (str): The name of the character.
        Returns:
            dict: The response from the API containing character status information.
        """
        endpoint = f"characters/{character_name}"
        return client.get(endpoint)

    @staticmethod
    def unequip(character_name, slot):
        """
        Unequip an item from a specified slot.
        Args:
            character_name (str): The name of the character.
            slot (str): The equipment slot to unequip.

        Returns:
            dict: The response from the API.
        """
        endpoint = f"my/{character_name}/action/unequip"
        data = {"slot": slot}
        response = client.post(endpoint, data)
        return response

    @staticmethod
    def deposit_bank(character_name, code, quantity):
        """
        Deposit an item into the character's bank.
        Args:
            character_name (str): The name of the character.
            code (str): The code of the item to deposit.
            quantity (int): The quantity of the item to deposit.

        Returns:
            dict: The response from the API.
        """
        endpoint = f"my/{character_name}/action/bank/deposit"
        data = {"code": code, "quantity": quantity}
        response = client.post(endpoint, data)
        return response

    @staticmethod
    def deposit_gold(character_name, quantity):
        """
        Deposit gold into the character's bank.
        Args:
            character_name (str): The name of the character.
            quantity (int): The quantity of gold to deposit.

        Returns:
            dict: The response from the API.
        """
        endpoint = f"my/{character_name}/action/bank/deposit/gold"
        data = {"quantity": quantity}
        response = client.post(endpoint, data)
        return response

    @staticmethod
    def withdraw_bank(character_name, code, quantity):
        """
        Withdraw an item from the character's bank.
        Args:
            character_name (str): The name of the character.
            code (str): The code of the item to withdraw.
            quantity (int): The quantity of the item to withdraw.

        Returns:
            dict: The response from the API.
        """
        endpoint = f"my/{character_name}/action/bank/withdraw"
        data = {"code": code, "quantity": quantity}
        response = client.post(endpoint, data)
        return response

    @staticmethod
    def withdraw_gold(character_name, quantity):
        """
        Withdraw gold from the character's bank.
        Args:
            character_name (str): The name of the character.
            quantity (int): The quantity of gold to withdraw.

        Returns:
            dict: The response from the API.
        """
        endpoint = f"my/{character_name}/action/bank/withdraw/gold"
        data = {"quantity": quantity}
        response = client.post(endpoint, data)
        return response

    @staticmethod
    def buy_ge(character_name, code, quantity, price):
        """
        Buy an item from the Grand Exchange.
        Args:
            character_name (str): The name of the character.
            code (str): The code of the item to buy.
            quantity (int): The quantity of the item to buy.
            price (int): The price per item.

        Returns:
            dict: The response from the API.
        """
        endpoint = f"my/{character_name}/action/ge/buy"
        data = {"code": code, "quantity": quantity, "price": price}
        response = client.post(endpoint, data)
        return response

    @staticmethod
    def sell_ge(character_name, code, quantity, price):
        """
        Sell an item on the Grand Exchange.
        Args:
            character_name (str): The name of the character.
            code (str): The code of the item to sell.
            quantity (int): The quantity of the item to sell.
            price (int): The price per item.
        Returns:
            dict: The response from the API.
        """
        endpoint = f"my/{character_name}/action/ge/sell"
        data = {"code": code, "quantity": quantity, "price": price}
        response = client.post(endpoint, data)
        return response

    @staticmethod
    def new_task(character_name):
        """
        Assign a new task to the character.
        Args:
            character_name (str): The name of the character.
        Returns:
            dict: The response from the API.
        """
        endpoint = f"my/{character_name}/action/task/new"
        response = client.post(endpoint)
        return response

    @staticmethod
    def complete_task(character_name):
        """
        Complete the current task assigned to the character.
        Args:
            character_name (str): The name of the character.
        Returns:
            dict: The response from the API.
        """
        endpoint = f"my/{character_name}/action/task/complete"
        response = client.post(endpoint)
        return response

    @staticmethod
    def task_exchange(character_name):
        """
        Exchange the current task for a new one.
        Args:
            character_name (str): The name of the character.
        Returns:
            dict: The response from the API.
        """
        endpoint = f"my/{character_name}/action/task/exchange"
        response = client.post(endpoint)
        return response

    @staticmethod
    def delete_item(character_name, code, quantity):
        """
        Delete an item from the character's inventory.
        Args:
            character_name (str): The name of the character.
            code (str): The code of the item to delete.
            quantity (int): The quantity of the item to delete.
        Returns:
            dict: The response from the API.
        """
        endpoint = f"my/{character_name}/action/delete"
        data = {"code": code, "quantity": quantity}
        response = client.post(endpoint, data)
        return response