import re

handle = open('./regex_sum_354529.txt')
numbers = list()
sum_result = 0
for line in handle:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if not len(numbers) != 0: continue
    for num in numbers:
        sum_result = sum_result + int(num)
print(sum_result)

