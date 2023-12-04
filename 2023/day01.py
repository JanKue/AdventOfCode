import re

def main():
    # parsing data
    file = open("./inputs/day01.txt")
    lines = file.read().splitlines()
    print(lines)

    pattern = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))")
    matches = [pattern.findall(line) for line in lines]

    numwords = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    numbers = []
    for match in matches:
        first = match[0] if match[0].isdigit() else numwords[match[0]]
        last = match[-1] if match[-1].isdigit() else numwords[match[-1]]
        numbers.append(int(first + last))

    print(numbers)
    print(sum(numbers))

if __name__ == '__main__':
    main()