import re


def main():
    # parsing data
    file = open("../inputs/2023/day02.txt")
    lines = file.read().splitlines()
    print(lines)

    possible_game_sum = 0
    total_games_power = 0
    for i in range(len(lines)):
        game_max_red, game_max_green, game_max_blue = game_max_rgb(lines[i])
        if game_max_red <= 12 and game_max_green <= 13 and game_max_blue <= 14:
            possible_game_sum += i+1
        total_games_power += game_max_red * game_max_green * game_max_blue

    print("Part 1:", possible_game_sum)
    print("Part 2:", total_games_power)


def set_rgb(test_set):
    pattern = re.compile(r"(\d+) red|(\d+) green|(\d+) blue")
    matches = pattern.findall(test_set)
    rgb = [''.join(x) for x in zip(*matches)]
    return rgb


def game_max_rgb(game):
    sets = game.split(';')
    set_rgb_results = [set_rgb(test_set) for test_set in sets]
    red_max, green_max, blue_max = 0, 0, 0
    for result in set_rgb_results:
        red_max = max(int('0'+result[0]), red_max)
        green_max = max(int('0'+result[1]), green_max)
        blue_max = max(int('0'+result[2]), blue_max)
    return red_max, green_max, blue_max


if __name__ == '__main__':
    main()