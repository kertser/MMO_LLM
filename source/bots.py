import math

import menuHandler as mH
from actions import GameActions as Ga
from utilities import GameUtilities as Gu

class BotActions:
    @staticmethod
    def kill_bot(character_name, monster_type, number_of_monsters):
        """
        :param character_name: controlled character
        :param monster_type: type of monster to slay
        :param number_of_monsters: the number of monsters to slay
        :return: successful or not
        """
        spawns = Gu.get_tiles_with_content("monster", monster_type)
        status = mH.handle_check_character_status(character_name)

        character_x = status['data']['x']
        character_y = status['data']['y']

        closest_spawn = None
        min_distance = float('inf')

        for spawn in spawns:
            spawn_x = spawn['x']
            spawn_y = spawn['y']
            distance = math.dist((character_x, character_y), (spawn_x, spawn_y))

            if distance < min_distance:
                min_distance = distance
                closest_spawn = spawn

        # Now `closest_spawn` contains the spawn with the shortest distance
        if closest_spawn:
            # Move to the closest spawn
            Ga.move_character(character_name, closest_spawn['x'], closest_spawn['y'])

            # Engage in battle with the specified monster type
            for _ in range(number_of_monsters):
                # Perform fight and get the result response
                print(f"{character_name} is fighting a {Gu.get_monster_info(monster_type)["name"]}...")
                if(mH.handle_fight(character_name) != True):
                    return False

        return True

    @staticmethod
    def gathering_bot(character_name, resource_type, number_of_resources):
        """
        Gathers the specified number of resources of a given type.

        :param character_name: controlled character
        :param resource_type: type of resource to gather
        :param number_of_resources: the number of resources to gather
        :return: True if successful, False otherwise
        """
        spawns = Gu.get_tiles_with_content("resource", resource_type)
        status = mH.handle_check_character_status(character_name)

        character_x = status['data']['x']
        character_y = status['data']['y']

        closest_spawn = None
        min_distance = float('inf')

        for spawn in spawns:
            spawn_x = spawn['x']
            spawn_y = spawn['y']
            distance = math.dist((character_x, character_y), (spawn_x, spawn_y))

            if distance < min_distance:
                min_distance = distance
                closest_spawn = spawn

        # Now `closest_spawn` contains the spawn with the shortest distance
        if closest_spawn:
            # Move to the closest spawn
            Ga.move_character(character_name, closest_spawn['x'], closest_spawn['y'])

            # Gather resources at the specified location
            gathered = 0
            while gathered < number_of_resources:
                # Perform gathering action and check if successful
                print(f"{character_name} is gathering {Gu.get_resource_info(resource_type)['name']}...")
                success = mH.handle_gathering(character_name)
                if success:
                    gathered += 1
                else:
                    print("Failed to gather resource. Moving to the next spot.")
                    #TODO: implement code that moves character to new spot

            return True

        print(f"No suitable resource spawn found for {resource_type}.")
        return False

    @staticmethod
    def equip_best_item(character_name, monster_code, allowed_item_codes=None):# Work in progress
        """
        Equips the best item for the character based on the monster's elemental resistances.

        :param character_name: The name of the controlled character.
        :param monster_code: The code of the monster.
        :param allowed_item_codes: A list of item codes that are allowed to be equipped.
                                   If None, use the character's current inventory.
        :return: True if an item was equipped, False otherwise.
        """
        # Get the character's inventory
        inventory = BotActions.get_inventory(character_name)

        # Get the monster's elemental resistances
        resistances = BotActions.get_monster_resistances(monster_code)

        # If allowed_item_codes is None, consider all items in the inventory
        if allowed_item_codes is None:
            allowed_item_codes = [item['code'] for item in inventory]

        # Filter inventory for allowed items
        allowed_items = [item for item in inventory if item['code'] in allowed_item_codes]

        # Find the best item to equip
        best_item = BotActions.find_best_item(allowed_items, resistances)

        # Equip the best item if found
        if best_item:
            Ga.equip_item(character_name, best_item['code'])
            print(f"{character_name} equipped {best_item['name']}.")
            return True

        print(f"No suitable item found to equip for {character_name}.")
        return False

    @staticmethod
    def get_inventory(character_name):
        """
        Retrieves the character's inventory.

        :param character_name: The name of the controlled character.
        :return: A list of items in the character's inventory.
        """
        status = mH.handle_check_character_status(character_name)
        return status['data']['inventory']

    @staticmethod
    def get_monster_resistances(monster_code):
        """
        Retrieves the monster's elemental resistances.

        :param monster_code: The code of the monster.
        :return: A dictionary containing the monster's elemental resistances.
        """
        monster_info = Gu.get_monster_info(monster_code)
        return {
            'fire': monster_info['res_fire'],
            'earth': monster_info['res_earth'],
            'water': monster_info['res_water'],
            'air': monster_info['res_air']
        }

    @staticmethod
    def calculate_effectiveness(item, resistances):
        """
        Calculates the effectiveness of an item against the monster's resistances.

        :param item: The item to evaluate.
        :param resistances: A dictionary of the monster's elemental resistances.
        :return: The effectiveness value of the item.
        """
        effectiveness = 0
        for effect in item.get('item', []).get('effects', []):
            print(effect)
            if effect['name'] == 'attack_fire':
                effectiveness += effect['value'] - resistances['fire']
            elif effect['name'] == 'attack_earth':
                effectiveness += effect['value'] - resistances['earth']
            elif effect['name'] == 'attack_water':
                effectiveness += effect['value'] - resistances['water']
            elif effect['name'] == 'attack_air':
                effectiveness += effect['value'] - resistances['air']
        return effectiveness

    @staticmethod
    def find_best_item(allowed_items, resistances):
        """
        Finds the best item to equip based on effectiveness against monster resistances.

        :param allowed_items: A list of items that can be equipped.
        :param resistances: A dictionary of the monster's elemental resistances.
        :return: The best item to equip, or None if no suitable item is found.
        """
        best_item = None
        best_effectiveness = -float('inf')

        for item in allowed_items:
            effectiveness = BotActions.calculate_effectiveness(item, resistances)
            if effectiveness > best_effectiveness:
                best_effectiveness = effectiveness
                best_item = item

        return best_item


#Example usages:
#Go to the weaponcrafting workshop
workshop = Gu.get_tiles_with_content('workshop', 'weaponcrafting')[0]
print(workshop)
Ga.move_character('Sylphy',workshop.get('x'), workshop.get('y'))
