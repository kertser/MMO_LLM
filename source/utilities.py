"""
This is a collection of helper functions for interacting with the game's API.
These functions encapsulate common operations such as fetching tile information
"""
from connect import client
#! TODO: remove the page parameter from the list of arguments

# Representing the class of utility functions with static methods
class GameUtilities:
    @staticmethod
    def get_tiles_with_content(content_type=None, content_code=None, page=1, size=50):
        """
        Fetch all map tiles containing a specific content type and code.

        Args:
            content_type (str): The type of content to search for (e.g., "monster", "resource").
            content_code (str): The code of the content to search for.
            page (int): The page number to fetch.
            size (int): The number of results per page.

        Returns:
            #! TODO: Set your mind - List of Dicts, Dict of Lists of other shit of shit
            list: A list of map tiles containing the specified content.
        Example:
            get_tiles_with_content(content_type="monster", content_code="chicken")
        """
        endpoint = "/maps/"
        params = {
            "content_type": content_type,
            "content_code": content_code,
            "page": page,
            "size": size
        }

        response = client.get(endpoint, params=params)
        if response:
            return response["data"][0]
        return []

    @staticmethod
    def get_item_info(item_code=None, craft_material=None, craft_skill=None, max_level=None, min_level=None, page=1, size=50):
        """
        Get the information about a specific item or a list of items, filtered by parameters.

        Args:
            item_code (str): The code of the item to retrieve info for.
            craft_material (str): The material used in crafting.
            craft_skill (str): The skill required for crafting.
            max_level (int): The maximum item level.
            min_level (int): The minimum item level.
            page (int): The page number to fetch.
            size (int): The number of results per page.

        Returns:
            A dictionary containing item information if item_code is provided
        Example:
            get_item_info(item_code="wooden_stick")
        """
        if item_code:
            endpoint = f"/items/{item_code}"
            response = client.get(endpoint)
            if response:
                return response["data"][0]
            return {}
        else: # Full list of items
            endpoint = "/items"
            params = {
                "page": page, #TBD - remove?
                "size": size,
                "craft_material": craft_material,
                "craft_skill": craft_skill,
                "max_level": max_level,
                "min_level": min_level
            }
            # Remove None values from params
            # Filter empty values:
            params = {k: v for k, v in params.items() if v is not None}

            response = client.get(endpoint, params=params)
            if response:
                return response["data"][0]
        return {}

    def get_monster_info(monster_code=None, drop=None, max_level=None, min_level=None, page=1, size=50):
        """
        Fetch information about a specific monster or a list of monsters with tunable parameters.

        Args:
            monster_code (str): The code of the monster to retrieve info for.
            drop (str): The type of drop item.
            max_level (int): The maximum monster level.
            min_level (int): The minimum monster level.
            page (int): The page number to fetch.
            size (int): The number of results per page.

        Returns:
            #! TODO: fix - dict or list
            dict: A dictionary containing monster information if monster_code is provided,
                          otherwise a list of monsters.

        Example:
            #!TODO: Fix
            get_monster_info(...
        """
        if monster_code:
            endpoint = f"/monsters/{monster_code}"
            response = client.get(endpoint)
            if response:
                return response.get("data", {})
        else:
            endpoint = "/monsters"
            params = {
                "page": page,
                "size": size,
                "drop": drop,
                "max_level": max_level,
                "min_level": min_level
            }
            # Remove None values from params
            params = {k: v for k, v in params.items() if v is not None}

            response = client.get(endpoint, params=params)
            if response:
                return response["data"][0]
        return {}

    @staticmethod
    def get_resource_info(resource_code=None, drop=None, max_level=None, min_level=None, page=1, size=50):
        """
        Fetch information about a specific resource or a list of resources with tunable parameters.

        Args:
            resource_code (str): The code of the resource to retrieve info for.
            drop (str): The type of drop item.
            max_level (int): The maximum resource level.
            min_level (int): The minimum resource level.
            page (int): The page number to fetch.
            size (int): The number of results per page.

        Returns:
            dict or list: A dictionary containing resource information if resource_code is provided,
                          otherwise a list of resources.
        """
        if resource_code:
            endpoint = f"/resources/{resource_code}"
            response = client.get(endpoint)
            if response:
                return response["data"][0]
        else:
            endpoint = "/resources"
            params = {
                "page": page,
                "size": size,
                "drop": drop,
                "max_level": max_level,
                "min_level": min_level
            }
            # Remove None values from params
            params = {k: v for k, v in params.items() if v is not None}

            response = client.get(endpoint, params=params)
            if response:
                return response["data"][0]
        return {}

    @staticmethod
    def get_events(page=1, size=50):
        """
        Fetch a list of events with pagination. (remove pagination)
        This is about the events, currently happening on server

        Args:
            page (int): The page number to fetch.
            size (int): The number of results per page.

        Returns:
            list: A list of events.
        """
        endpoint = "/events"
        params = {
            "page": page,
            "size": size
        }

        response = client.get(endpoint, params=params)
        if response:
            return response["data"][0]
        return []

    @staticmethod
    def get_ge(page=1, size=50):
        """
        Fetch a list of grand exchange items
        (Free market between the players - items exchange list)

        Args:
            page (int): The page number to fetch.
            size (int): The number of results per page.

        Returns:
            list: A list of geographical entities.
        """
        endpoint = "/ge"
        params = {
            "page": page,
            "size": size
        }

        response = client.get(endpoint, params=params)
        if response:
            return response["data"][0]
        return {}



