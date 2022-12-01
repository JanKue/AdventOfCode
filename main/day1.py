file = open("../inputs/day1.txt")

text = file.read()
lines = text.split('\n\n')

numbers = [[int(n) for n in line.split()] for line in lines]

print(numbers)

totals = [sum(nums) for nums in numbers]
totals.sort(reverse=True)

print(totals)

maximum = totals[0]

print(maximum)

top_three_sum = sum(totals[:3])

print(top_three_sum)
