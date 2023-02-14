# Juan Carlos Gallardo Brambila
import time

import readchar
import os
import random
import keyboard

# Constants
POS_X = 0
POS_Y = 1
NUM_OF_MAP_OBJECTS = 10
# Variables in game
my_position = [14, 9]
tail = []
tail_length = 0
map_objects = []
end_game = False
obstacle_definition = """\
########   ########     #####
#                           #
#       ##          ##      #
        ##          ##       
        ##          ##       
        ##          ##       
        ##          ##       
#                           #
#                           #
#                           #
#                           #
#                           #
         ##          ##      
         ##          ##      
         ##          ##      
         ##          ##      
#                           #
#                           #
########   ########     #####\ """

# Generate obstacles on the map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = 29
MAP_HEIGHT = 19

while True:
    # Generate random objects on the map
    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_position = [random.randint(0, (MAP_WIDTH - 1)), random.randint(0, (MAP_HEIGHT - 1))]

        if new_position not in map_objects and new_position != my_position:
            if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
                map_objects.append(new_position)

    print("Score: {}".format(tail_length))
    # Draw Map
    print("-" + "--" * MAP_WIDTH + "-")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "
            object_in_cell = None
            tail_in_cell = None
            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = " *"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = " @"
                    tail_in_cell = tail_piece

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " +"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1

                if tail_in_cell:
                    end_game = True

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        print("|")

    if end_game:
        break

    print("-" + "--" * MAP_WIDTH + "-")
    # print(tail)
    # print(map_objects)
    # print("El tamaño de la cola es {}".format(tail_length))

    # Input of where to move, readchar == input()
    direction = readchar.readchar()

    new_position = None
    # Movement conditions
    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q":
        break

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position = new_position
        else:
            break

    os.system("cls")
os.system("cls")
print("\n\n       YOU DIED    ")
print("\n\n=========================")
print("     Final Score: {}     ".format(tail_length))
print("=========================\n\n")
input("")
