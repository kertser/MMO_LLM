import time

def move_character(client, character_name, x, y):
    endpoint = f"my/{character_name}/action/move"
    data = {"x": x, "y": y}
    response = client.post(endpoint, data)
    print(response)

def perform_fight(character_name):
    endpoint = f"my/{character_name}/action/fight"
    response = post(endpoint)

    if response is None:
        print("An error occurred during the fight.")
        return

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
            print(f"{character_name} is fighting a {data['monster']}...")
            print(f"The fight ended successfully. You have {data['fight']['result']}.")
            cooldown = data['cooldown']['total_seconds']
            time.sleep(cooldown)
            perform_fight(character_name)
            return cooldown
    return 0



def crafting(character_name, item_code, quantity):
    endpoint = f"my/{character_name}/action/crafting"
    data = {"code": item_code, "quantity": quantity}
    response = post(endpoint, data)
    print(response)


def gathering(character_name):
    endpoint = f"my/{character_name}/action/gathering"
    response = post(endpoint)

    if response is None:
        print("An error occurred during gathering.")
        return

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
            gathering(character_name)
            return cooldown
    return 0

def get_character_status(character_name):
    endpoint = f"my/{character_name}/status"
    return get(endpoint)

def unequip(character_name, slot):
    endpoint = f"my/{character_name}/action/unequip"
    data = {"slot": slot}
    response = post(endpoint, data)
    print(response)

def deposit_bank(character_name, code, quantity):
    endpoint = f"my/{character_name}/action/bank/deposit"
    data = {"code": code, "quantity": quantity}
    response = post(endpoint, data)
    print(response)


def deposit_gold(character_name, quantity):
    endpoint = f"my/{character_name}/action/bank/deposit/gold"
    data = {"quantity": quantity}
    response = post(endpoint, data)
    print(response)


def withdraw_bank(character_name, code, quantity):
    endpoint = f"my/{character_name}/action/bank/withdraw"
    data = {"code": code, "quantity": quantity}
    response = post(endpoint, data)
    print(response)


def withdraw_gold(character_name, quantity):
    endpoint = f"my/{character_name}/action/bank/withdraw/gold"
    data = {"quantity": quantity}
    response = post(endpoint, data)
    print(response)


def buy_ge(character_name, code, quantity, price):
    endpoint = f"my/{character_name}/action/ge/buy"
    data = {"code": code, "quantity": quantity, "price": price}
    response = post(endpoint, data)
    print(response)


def sell_ge(character_name, code, quantity, price):
    endpoint = f"my/{character_name}/action/ge/sell"
    data = {"code": code, "quantity": quantity, "price": price}
    response = post(endpoint, data)
    print(response)

def new_task(character_name):
    endpoint = f"my/{character_name}/action/task/new"
    response = post(endpoint)
    print(response)

def complete_task(character_name):
    endpoint = f"my/{character_name}/action/task/complete"
    response = post(endpoint)
    print(response)

def task_exchange(character_name):
    endpoint = f"my/{character_name}/action/task/exchange"
    response = post(endpoint)
    print(response)

def delete_item(character_name, code, quantity):
    endpoint = f"my/{character_name}/action/delete"
    data = {"code": code, "quantity": quantity}
    response = post(endpoint, data)
    print(response)






