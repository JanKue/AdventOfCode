def main():

    file = open("inputs/day02.txt")
    lines = file.read().splitlines()

    lines = [line.split('x') for line in lines]
    lines = [(int(line[0]), int(line[1]), int(line[2])) for line in lines]
    paper = [0] * len(lines)
    ribbon = [0] * len(lines)
    i = 0

    for a, b, c in lines:
        sides = sorted((a, b, c))
        paper[i] = 2*a*b + 2*b*c + 2*a*c + sides[0] * sides[1]
        ribbon[i] = a*b*c + 2*sides[0] + 2*sides[1]
        i += 1

    print(lines)
    print(sum(paper))
    print(sum(ribbon))


if __name__ == '__main__':
    main()
