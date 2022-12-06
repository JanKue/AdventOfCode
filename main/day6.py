import numpy as np


def main():

    file = open("../inputs/day6.txt")
    data = file.read()
    print(data)

    print("PART ONE")
    packet_marker = find_packet_marker(data)
    print(packet_marker)

    print("PART TWO")
    message_marker = find_message_marker(data)
    print(message_marker)


def find_packet_marker(string):
    for i in range(3, len(string)):
        if string[i-3:i].__contains__(string[i]):
            continue
        elif string[i-3:i-1].__contains__(string[i-1]):
            continue
        elif string[i-3] == string[i-2]:
            continue
        else:
            return i+1
    return 0


def find_message_marker(string):
    found_all = np.array(13 * [None])
    for i in range(13, len(string)):
        for j in range(13):
            found_all[j] = string[i-13:i-j].__contains__(string[i-j])
        if not found_all.any():
            return i+1
    return 0


if __name__ == "__main__":
    main()
