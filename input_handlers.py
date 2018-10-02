# Python Imports
import libtcodpy as libtcod

# Package Imports
from game_states import GameStates

def handle_keys(key, game_state):
    if game_state == GameStates.PLAYER_TURN:
        return handle_player_turn_keys(key)
    elif game_state == GameStates.PLAYER_DEAD:
        return handle_player_dead_keys(key)
    elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        return handle_inventory_keys(key)

    return {}

def handle_player_turn_keys(key):
    key_char = chr(key.c)
    #Movement keys
    if key.vk == libtcod.KEY_UP or key_char == 'w':
        return {'move': (0, -1)}
    if key.vk == libtcod.KEY_DOWN or key_char == 's':
        return {'move': (0, 1)}
    if key.vk == libtcod.KEY_LEFT or key_char == 'a':
        return {'move': (-1, 0)}
    if key.vk == libtcod.KEY_RIGHT or key_char == 'd':
        return {'move': (1, 0)}

    if key_char == 'q':
        return {'move':(-1, -1)}
    if key_char == 'e':
        return {'move':(1, -1)}
    if key_char == 'z':
        return {'move':(-1, 1)}
    if key_char == 'c':
        return {'move':(1, 1)}

    if key_char == 'x':
        return {'pickup': True}

    elif key_char == 'i':
        return {'show_inventory': True}

    elif key_char == 'r':
        return {'drop_inventory': True}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Set fullscreen
        return {'fullscreen': True}

    elif key.vk == libtcod.KEY_ESCAPE:
        #Exit the game
        return {'exit': True}

    #Nothing was pressed
    return {}

def handle_player_dead_keys(key):
    key_char = chr(key.c)
    if key_char == 'i':
        return {'show_inventory': True}
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Set fullscreen
        return {'fullscreen': True}

    elif key.vk == libtcod.KEY_ESCAPE:
        #Exit the game
        return {'exit': True}

    #Nothing was pressed
    return {}

def handle_inventory_keys(key):
    index = key.c - ord('a')

    if index >= 0:
        return {'inventory_index': index}
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Set fullscreen
        return {'fullscreen': True}

    elif key.vk == libtcod.KEY_ESCAPE:
        #Exit the game
        return {'exit': True}

    #Nothing was pressed
    return {}
