### Day 1

import sys

GOOD_EXIT = 0
BAD_EXIT = 1

MAX_DIAL_NUM = 99
MIN_DIAL_NUM = 0

INPUT_FILE = "day1.txt"
INPUT_FILE_PATH = "../data/"

TURN_DIAL_LEFT = "L"
TURN_DIAL_RIGHT = "R"

TURN_DIRECTION = 0
TURN_DISTANCE = 1

def read_input_file():
    data = []

    with open(INPUT_FILE_PATH + INPUT_FILE, "r") as file:
        for line in file:
            data.append(line.rstrip("\n"))

    return data

def retrieve_combos(data):
    combos = []

    for entry in data:
        turn_direction = entry[0]
        turn_distance = entry[1:]
        combos.append([turn_direction, turn_distance])

    return combos

def main():
    
    # prompt for starting input for safe
    dial_start = input("What's the starting number on the dial?\n")

    # check if dial start is valid input
    try:
        dial_start = int(dial_start)
    except ValueError:
        print("Input was not a valid integer. Exiting...\n")
        sys.exit(BAD_EXIT)

    if (dial_start > MAX_DIAL_NUM):
        print("Input cannot be more than " + str(MAX_DIAL_NUM) + ". Exiting...\n")
        sys.exit(BAD_EXIT)

    if (dial_start < MIN_DIAL_NUM):
        print("Input cannot be less than " + str(MIN_DIAL_NUM) + ". Exiting...\n")
        sys.exit(BAD_EXIT)

    # read input file data
    print("Reading input file data...")
    data = read_input_file()

    # retrieve combos
    combos = retrieve_combos(data)

    # crack safe
    current_num = dial_start
    zero_count = 0
    for combo in combos:
        print("Debug: Before = " + str(current_num))

        if combo[TURN_DIRECTION] == TURN_DIAL_RIGHT:
            current_num = current_num + (int(combo[TURN_DISTANCE]) % (MAX_DIAL_NUM + 1))

            if current_num > MAX_DIAL_NUM:
                current_num = current_num - MAX_DIAL_NUM - 1

        if combo[TURN_DIRECTION] == TURN_DIAL_LEFT:
            current_num = current_num - (int(combo[TURN_DISTANCE]) % (MAX_DIAL_NUM + 1))

            if current_num < MIN_DIAL_NUM:
                current_num = current_num + MAX_DIAL_NUM + 1

        print(", DIR: " + str(combo[TURN_DIRECTION]))
        print(", DIS: " + str(combo[TURN_DISTANCE]))
        print(", After: " + str(current_num))

        if current_num == 0:
            zero_count = zero_count + 1
        

    print("Door password is the zero count: " + str(zero_count))
    print("Done!\n")
    sys.exit(GOOD_EXIT)

if __name__ == "__main__":
    main()