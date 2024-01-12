def create_room(room_width, room_height):
    return [(col, row) for row in range(room_height) for col in range(room_width)]


def generate_room(room, room_width, room_height):
    for cell in room:
        if cell[0] in (0, room_width - 1) and cell[1] in (
            0,
            room_height - 1,
        ):
            print("-", end="")
        elif cell[0] in (0, room_width - 1):
            print("|", end="")
        elif cell[1] in (0, room_height - 1):
            print("-", end="")
        else:
            print(".", end="")
        if cell[0] == room_width - 1:
            print("", end="\n")


def create_player():
    pass


FIRST_ROOM_WIDTH = 30
FIRST_ROOM_HEIGHT = 6
FIRST_ROOM = create_room(FIRST_ROOM_WIDTH, FIRST_ROOM_HEIGHT)

generate_room(FIRST_ROOM, FIRST_ROOM_WIDTH, FIRST_ROOM_HEIGHT)
