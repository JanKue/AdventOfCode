def calculate_move_score(move_pair):

    # normalize move values to 1=rock, 2=paper, 3=scissors
    opponent_move = ord(move_pair[0]) - 64
    player_move = ord(move_pair[1]) - 87

    # outcome: -1=draw, 0=opponent wins, 1=player wins
    outcome = (opponent_move - player_move) % 3 - 1

    if outcome == -1:
        outcome = 3
    elif outcome == 1:
        outcome = 6

    return player_move + outcome


def calculate_strategy_score(strategy_pair):
    # move values: 0=rock, 1=paper, 2=scissors
    opponent_move = ord(strategy_pair[0]) - 65
    # outcome values: 0=opponent wins, 1=draw, 2=player wins
    outcome = ord(strategy_pair[1]) - 88

    outcome_score = 3 * outcome

    # shifted outcome: 1=opponent wins, 0=draw, -1=player wins
    outcome_shifted = -(outcome - 1)
    # picking the correct move (values as above)
    player_move = (opponent_move - outcome_shifted) % 3
    player_score = player_move + 1

    return outcome_score + player_score


# parsing data
file = open("../inputs/day2.txt")

lines = file.read().split('\n')
moves = [line.split(' ') for line in lines[:-1]]

print(lines)
print(moves)

print("PART ONE")
scores = [calculate_move_score(move_pair) for move_pair in moves]

print(scores)
print(sum(scores))

print("PART TWO")
scores = [calculate_strategy_score(strategy_pair) for strategy_pair in moves]

print(scores)
print(sum(scores))
