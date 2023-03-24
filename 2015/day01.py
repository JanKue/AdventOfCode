def main():

    file = open("inputs/day01.txt")
    text = file.read()

    floor = 0
    position = 0
    basement = 0
    for char in text:
        position += 1
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if basement == 0 and floor < 0:
            basement = position

    print(floor)
    print(basement)


if __name__ == '__main__':
    main()
