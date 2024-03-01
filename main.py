from operator import add
import keyboard
from os import system


def clear_screen():
    system("\033[H")


def create_player():
    global player
    x, y = FIRST_ROOM_WIDTH // 8, FIRST_ROOM_HEIGHT // 2
    player = (x, y)


def check_collision(position):
    x, y = position
    return x in (0, FIRST_ROOM_WIDTH - 1) or y in (0, FIRST_ROOM_HEIGHT - 1)


def move_player():
    global player
    new_position = tuple(map(add, player, direction))

    if not check_collision(new_position):
        player = new_position


def controls(e):
    global direction, player
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == "w":
            direction = DIRECTIONS["up"]
            move_player()
        elif e.name == "a":
            direction = DIRECTIONS["left"]
            move_player()
        elif e.name == "s":
            direction = DIRECTIONS["down"]
            move_player()
        elif e.name == "d":
            direction = DIRECTIONS["right"]
            move_player()


def create_room(room_width, room_height):
    return [(col, row) for row in range(room_height) for col in range(room_width)]


def display_room(room, room_width, room_height):
    clear_screen()
    for cell in room:
        if cell[0] in (0, room_width - 1) and cell[1] in (
            0,
            room_height - 1,
        ):
            print("-", end="")
        elif cell == player:
            print("@", end="")
        elif cell[0] in (0, room_width - 1):
            print("|", end="")
        elif cell[1] in (0, room_height - 1):
            print("-", end="")
        else:
            print(".", end="")
        if cell[0] == room_width - 1:
            print("")


keyboard.hook(controls)

FIRST_ROOM_WIDTH = 30
FIRST_ROOM_HEIGHT = 6
FIRST_ROOM = create_room(FIRST_ROOM_WIDTH, FIRST_ROOM_HEIGHT)

DIRECTIONS = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}
direction = None

create_player()

while True:
    display_room(FIRST_ROOM, FIRST_ROOM_WIDTH, FIRST_ROOM_HEIGHT)
