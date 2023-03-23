from collections import deque


def main():
    # hard-coded monkeys
    example_monkeys = [
        Monkey([79, 98], lambda old: old * 19, 23, 2, 3),
        Monkey([54, 65, 75, 74], lambda old: old + 6, 19, 2, 0),
        Monkey([79, 60, 97], lambda old: old * old, 13, 1, 3),
        Monkey([74], lambda old: old + 3, 17, 0, 1)
    ]
    monkeys = [
        Monkey([83, 88, 96, 79, 86, 88, 70], lambda old: old * 5, 11, 2, 3),
        Monkey([59, 63, 98, 85, 68, 72], lambda old: old * 11, 5, 4, 0),
        Monkey([90, 79, 97, 52, 90, 94, 71, 70], lambda old: old + 2, 19, 5, 6),
        Monkey([97, 55, 62], lambda old: old + 5, 13, 2, 6),
        Monkey([74, 54, 94, 76], lambda old: old * old, 7, 0, 3),
        Monkey([58], lambda old: old + 4, 17, 7, 1),
        Monkey([66, 63], lambda old: old + 6, 2, 7, 5),
        Monkey([56, 56, 90, 96, 68], lambda old: old + 7, 3, 4, 1)
    ]

    monkey_group = MonkeyGroup(monkeys)
    monkey_group.print_monkey_items()
    start_items = monkey_group.total_items()

    round_num = 10_000
    for i in range(round_num):
        monkey_group.do_round()

    print("Finished", round_num, "rounds")
    monkey_group.print_monkey_items()
    print("No items were lost:", start_items == monkey_group.total_items())
    print("Monkey business:", monkey_group.monkey_business())


class MonkeyGroup:
    def __init__(self, monkeys):
        self.monkeys = monkeys

    def do_round(self):
        for monkey in self.monkeys:
            throws = monkey.do_actions()
            for throw in throws:
                target = throw[0]
                item = throw[1]
                self.monkeys[target].items.append(item)

    def monkey_business(self):
        counts = sorted([monkey.inspection_count for monkey in self.monkeys])
        return counts[-1] * counts[-2]

    def total_items(self):
        lengths = [len(monkey.items) for monkey in self.monkeys]
        return sum(lengths)

    def print_monkey_items(self):
        for monkey in self.monkeys:
            print(monkey.items)


class Monkey:
    def __init__(self, starting_items: list, operation, divisor: int, throw_true: int, throw_false: int):
        starting_floats = [float(i) for i in starting_items]
        self.items = deque(starting_items)
        self.operation = operation
        self.divisor = divisor
        self.throw_true = throw_true
        self.throw_false = throw_false

        self.inspection_count = 0

    def do_actions(self):
        throws = []
        while len(self.items) > 0:
            item = self.items.popleft()
            item = self.inspect_item(item)
            target = self.throw_item(item)
            throw = [target, item]
            throws.append(throw)
        return throws

    def inspect_item(self, item):
        self.inspection_count += 1
        item = self.operation(item)  # item value changes based on operation
        item %= 9699690  # hard-coded divisor product, for example case: 96577
        # item //= 3  # item value divides by 3
        return item

    def throw_item(self, item):
        if item % self.divisor == 0:
            return self.throw_true
        else:
            return self.throw_false


if __name__ == "__main__":
    main()
