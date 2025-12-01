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
        output_string = "Debug: BEF: " + str(current_num)
        curr_zero_count_round = 0

        if combo[TURN_DIRECTION] == TURN_DIAL_RIGHT:
            current_num = current_num + (int(combo[TURN_DISTANCE]) % (MAX_DIAL_NUM + 1))

            if current_num > MAX_DIAL_NUM:
                current_num = current_num - MAX_DIAL_NUM - 1
                curr_zero_count_round = curr_zero_count_round + 1

        if combo[TURN_DIRECTION] == TURN_DIAL_LEFT:
            current_num = current_num - (int(combo[TURN_DISTANCE]) % (MAX_DIAL_NUM + 1))

            if current_num < MIN_DIAL_NUM:
                current_num = current_num + MAX_DIAL_NUM + 1

                if (current_num + int(combo[TURN_DISTANCE]) != MAX_DIAL_NUM + 1):
                    curr_zero_count_round = curr_zero_count_round + 1

        total_rotations = math.floor(int(combo[TURN_DISTANCE]) / (MAX_DIAL_NUM + 1))

        if total_rotations > 0:
            curr_zero_count_round = curr_zero_count_round + total_rotations

            if current_num == 0 and combo[TURN_DIRECTION] == TURN_DIAL_LEFT:
                curr_zero_count_round = curr_zero_count_round + 1

        zero_count = zero_count + curr_zero_count_round

        output_string = output_string + ", DIR: " + str(combo[TURN_DIRECTION])
        output_string = output_string + ", DIS: " + str(combo[TURN_DISTANCE])
        output_string = output_string + ", AFT: " + str(current_num)
        output_string = output_string + ", ZER: " + str(curr_zero_count_round)
        output_string = output_string + ", TRO: " + str(total_rotations)
        
        print(output_string)

    print("Door password is the zero count: " + str(zero_count))
    print("Done!\n")
    sys.exit(GOOD_EXIT)

if __name__ == "__main__":
    main()