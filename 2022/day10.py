def main():

    file = open("inputs/day10.txt")
    lines = file.read().splitlines()

    signal_values = parse_signal_values(lines)
    print(signal_values)

    print("PART ONE")
    print(signal_strengths(signal_values))

    print("PART TWO")
    image = draw_image(signal_values)
    for row in image:
        print(str(row))


def draw_image(signal_values):
    raw_image = 240*['.']
    for i in range(240):
        if abs(signal_values[i] - i % 40) <= 1:
            raw_image[i] = '#'

    image_string = "".join(raw_image)
    render_image = [image_string[i:i+40] for i in range(0, 201, 40)]
    return render_image


def parse_signal_values(instructions):
    values = [1]
    i = 0
    for instruction in instructions:
        if instruction == "noop":
            values.append(values[i])
            i += 1
        if instruction[:4] == "addx":
            values.append(values[i])
            i += 1
            _, number = instruction.split()
            values.append(values[i] + int(number))
            i += 1
    return values


def signal_strengths(values):
    cycles = [20, 60, 100, 140, 180, 220]
    value_sum = 0
    for c in cycles:
        value_sum += c * values[c-1]
    return value_sum


if __name__ == "__main__":
    main()
