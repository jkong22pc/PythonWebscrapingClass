import re

file = open('regex_sum_1668024.txt')
sum = 0
for line in file.readlines():
    for num in re.findall('[0-9]+', line):
        sum += int(num)
print(sum)
