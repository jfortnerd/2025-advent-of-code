### Day 2
import math

INPUT_FILE_PATH = "../data/"
INPUT_FILE_NAME = "day2.in"

DASH_CHAR = "-"
COMMA_CHAR = ","

START_INDEX = 0
END_INDEX = 1

LOG_OUTPUT = False 

METHOD_ONE = 1
METHOD_TWO = 2

def read_file_data():
    data = []

    with open(INPUT_FILE_PATH + INPUT_FILE_NAME, "r") as file:
        for line in file:
            data.append(line)

    return data 

def split_pair(range_string):
    pair = range_string.split(DASH_CHAR)
    return pair

def split_line(line_string):
    line_string = line_string.rstrip("\n")
    data = line_string.split(COMMA_CHAR)
    return data 

def retrieve_id_ranges(data):
    ranges = []

    for line in data:
        range_strings = split_line(line)

        for string in range_strings:
            # if not empty
            if string:
                ranges.append(split_pair(string))

    return ranges

def check_invalid_id(string_rep):

    # start from 1 to midpoint length, rounded down
    midpoint = math.floor(len(string_rep) / 2)
    for j in range(0, midpoint):
        substring = string_rep[0:j + 1]

        if (LOG_OUTPUT):
            debug_log = ("String rep: " + string_rep)
            debug_log = debug_log + (", Substring: " + str(substring))
            print(debug_log)

        # only check easily divisible substrings 
        if (len(string_rep) % len(substring) == 0):
            
            # replace all substrings
            check_string = string_rep.replace(substring, "")

            if len(check_string) == 0:
                return True

    return False 

def check_range_pt1(start, end):
    invalid_ids = []

    for i in range(int(start), int(end) + 1):

        # Only worth checking if # of digits is even
        string_rep = str(i)
        if (len(string_rep) % 2) == 0:
            midpoint = len(string_rep) / 2
            first_half = string_rep[0:int(midpoint)]
            second_half = string_rep[int(midpoint):]

            if (LOG_OUTPUT):
                debug_log = ("String rep: " + string_rep)
                debug_log = debug_log + (", First: " + str(first_half))
                debug_log = debug_log + (", Second: " + str(second_half))
                print(debug_log)

            if (str(first_half) == str(second_half)):
                invalid_ids.append(string_rep)

                if (LOG_OUTPUT):
                    print("Adding for string_rep: " + string_rep)

    return invalid_ids

def check_range_pt2(start, end):
    invalid_ids = []

    for i in range(int(start), int(end) + 1):

        string_rep = str(i)
        invalid_id = check_invalid_id(string_rep)

        if (invalid_id):
            invalid_ids.append(string_rep)

            if (LOG_OUTPUT):
                print("Adding for string rep: " + string_rep)

    return invalid_ids

def sum_invalid_ids(ranges, method):
    total_sum = 0

    for pair in ranges:
        start = pair[START_INDEX]
        end = pair[END_INDEX]

        if method == METHOD_ONE:
            invalid_ids = check_range_pt1(start, end)
        elif method == METHOD_TWO:
            invalid_ids = check_range_pt2(start, end)

        for invalid_id in invalid_ids:
            total_sum = total_sum + int(invalid_id)

    return total_sum

def main():

    # retrieve input file data
    data = read_file_data()

    # retrieve ID ranges 
    ranges = retrieve_id_ranges(data)

    # retrieve total invalid ID sum
    total_invalid_id_sum_pt1 = sum_invalid_ids(ranges, METHOD_ONE)
    total_invalid_id_sum_pt2 = sum_invalid_ids(ranges, METHOD_TWO)

    # print answer
    print("Part 1 - The sum of all the invalid IDs is: " + str(total_invalid_id_sum_pt1))
    print("Part 2 - The sum of all the invalid IDs is: " + str(total_invalid_id_sum_pt2))

if __name__ == "__main__":
    main()