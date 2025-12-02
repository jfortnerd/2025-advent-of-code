### Day 1

import sys
import math

GOOD_EXIT = 0
BAD_EXIT = 1

MAX_DIAL_NUM = 99
MIN_DIAL_NUM = 0

INPUT_FILE = "day1.in"
INPUT_FILE_PATH = "../data/"

OUTPUT_LOG = "day1.out"

TURN_DIAL_LEFT = "L"
TURN_DIAL_RIGHT = "R"

TURN_DIRECTION = 0
TURN_DISTANCE = 1

LOG_OUTPUT = False 

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
    zero_count = 0
    exact_zero_count = 0 
    for combo in combos:

        distance_remaining = combo[TURN_DISTANCE]
        full_turns = 0
        partial_zeroes_encountered = 0

        # check full turns
        if int(distance_remaining) > (MAX_DIAL_NUM + 1):
            full_turns = math.floor(int(combo[TURN_DISTANCE]) / (MAX_DIAL_NUM + 1))
            distance_remaining = (int(combo[TURN_DISTANCE]) % (MAX_DIAL_NUM + 1))

        # check if turning the dial right
        if combo[TURN_DIRECTION] == TURN_DIAL_RIGHT:

            # check partial turn (when turning dial right)
            dial_current = int(dial_start) + int(distance_remaining)

            if (dial_current > MAX_DIAL_NUM):
                partial_zeroes_encountered = partial_zeroes_encountered + 1 
                dial_current = dial_current - MAX_DIAL_NUM - 1

                if (dial_current == 100):
                    dial_current = 0

        # check if turning the dial left
        elif combo[TURN_DIRECTION] == TURN_DIAL_LEFT:

            # check partial turn (when turning dial right)
            dial_current = int(dial_start) - int(distance_remaining)

            if (dial_current <= 0):
                dial_current = (MAX_DIAL_NUM + 1) + dial_current

                if (dial_current == 100):
                    dial_current = 0

                if (dial_start != 0):
                    partial_zeroes_encountered = partial_zeroes_encountered + 1


        # calculate zero counts
        if dial_current == 0:
            exact_zero_count = exact_zero_count + 1

        zero_count = zero_count + full_turns
        zero_count = zero_count + partial_zeroes_encountered

        # reset dial_start
        dial_start = dial_current

        # log output --- if turned on
        if (LOG_OUTPUT):
            output_string = "BEFORE: " + str(dial_start)
            output_string = output_string + ", DIRECT: " + str(combo[TURN_DIRECTION])
            output_string = output_string + ", DISTAN: " + str(combo[TURN_DISTANCE])
            output_string = output_string + ", CURREN: " + str(dial_current)
            output_string = output_string + ", PARTTR: " + str(partial_zeroes_encountered)
            output_string = output_string + ", FULLTR: " + str(full_turns)
            output_string = output_string + ", RTOTAL: " + str(zero_count)
            print(output_string)


    # print solutions
    print("Part 1 --- Door password is: " + str(exact_zero_count))
    print("Part 2 --- Door password is: " + str(zero_count))

    # good exit
    print("Done!\n")
    sys.exit(GOOD_EXIT)

if __name__ == "__main__":
    main()