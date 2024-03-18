from operator import add
from colorama import Fore as color
import keyboard, os, sys


def verify_os():
    if sys.platform == "win32" or sys.platform == "cygwin":
        erasecmd = "cls"
    else:
        erasecmd = "clear"
    return erasecmd


def erase_screen():
    clearcmd = verify_os()
    os.system(clearcmd)


def clear_screen():
    print("\033[H", end="")


def controls(control):
    global direction, player
    if control.event_type == keyboard.KEY_DOWN:
        if control.name == "w":
            direction = DIRECTIONS["up"]
            move_player()
        elif control.name == "a":
            direction = DIRECTIONS["left"]
            move_player()
        elif control.name == "s":
            direction = DIRECTIONS["down"]
            move_player()
        elif control.name == "d":
            direction = DIRECTIONS["right"]
            move_player()


def create_player():
    global player
    x, y = FIRST_ROOM_WIDTH // 8, FIRST_ROOM_HEIGHT // 2
    player = (x, y)


def create_enemy():
    global enemy
    x, y = FIRST_ROOM_WIDTH - 4, FIRST_ROOM_HEIGHT // 2
    enemy = (x, y)


def move_player():
    global player, turn_passed, turns_counter
    new_position = tuple(map(add, player, direction))

    if not wall_collision(new_position) and new_position != enemy:
        player = new_position
        turn_passed = True
        turns_counter += 1


def move_enemy():
    global enemy, turn_passed, movement_cooldown
    if turn_passed:
        distanceX, distanceY = enemy_distance()

        x_direction = distanceX // abs(distanceX) if distanceX != 0 else 0
        y_direction = distanceY // abs(distanceY) if distanceY != 0 else 0

        new_position = tuple(map(add, enemy, (x_direction, y_direction)))

        if (
            not wall_collision(new_position)
            and new_position != player
            and not movement_cooldown
        ):
            enemy = new_position
            turn_passed = False
            movement_cooldown = True


def enemy_distance():
    xEnemy, yEnemy = enemy
    xPlayer, yPlayer = player

    distanceX, distanceY = xPlayer - xEnemy, yPlayer - yEnemy

    return distanceX, distanceY


def cooldown():
    global movement_cooldown, turns_counter
    if movement_cooldown:
        if turns_counter >= 2:
            turns_counter = 0
            movement_cooldown = False


def create_room(room_width, room_height):
    return [(col, row) for row in range(room_height) for col in range(room_width)]


def display_room(room, room_width, room_height):
    for row in range(room_height):
        for col in range(room_width):
            cell = (col, row)
            if cell[0] in (0, room_width - 1) and cell[1] in (0, room_height - 1):
                print("-", end="")
            elif cell[0] in (0, room_width - 1):
                print("|", end="")
            elif cell[1] in (0, room_height - 1):
                print("-", end="")
            elif cell == player:
                print("@", end="")
            elif cell == enemy:
                print("e", end="")
            else:
                print(".", end="")
        print("")


def wall_collision(position):
    x, y = position
    return x in (0, FIRST_ROOM_WIDTH - 1) or y in (0, FIRST_ROOM_HEIGHT - 1)


keyboard.hook(controls)

FIRST_ROOM_WIDTH = 30
FIRST_ROOM_HEIGHT = 7
FIRST_ROOM = create_room(FIRST_ROOM_WIDTH, FIRST_ROOM_HEIGHT)

DIRECTIONS = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}
direction = None

turn_passed = False
movement_cooldown = False
turns_counter = 0

create_player()
create_enemy()

erase_screen()

while True:
    clear_screen()
    display_room(FIRST_ROOM, FIRST_ROOM_WIDTH, FIRST_ROOM_HEIGHT)
    move_enemy()
    cooldown()
