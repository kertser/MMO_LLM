import math

import menuHandler as mH
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

        character_x = status.get('x')
        character_y = status.get('y')

        closest_spawn = None
        min_distance = float('inf')

        for spawn in spawns:
            spawn_x = spawn.get('x')
            spawn_y = spawn.get('y')
            distance = math.dist((character_x, character_y), (spawn_x, spawn_y))

            if distance < min_distance:
                min_distance = distance
                closest_spawn = spawn

        # Now `closest_spawn` contains the spawn with the shortest distance
        if closest_spawn:
            # Move to the closest spawn
            mH.handle_move(character_name, closest_spawn['x'], closest_spawn['y'])

            # Engage in battle with the specified monster type
            for _ in range(number_of_monsters):
                # Perform fight and get the result response
                response = mH.handle_fight(character_name)

                # Check the response status and return False if an error or cooldown status is found
                status = response.get("status")
                if status in {498, 497, 499, 598}:
                    return False

                # Check if the fight was lost
                data = response.get("data")
                if data and data['fight']['result'] == 'lost':
                    return False
        return True



BotActions.kill_bot('Sylphy','yellow_slime', 400)