file = open('numbers.txt')
print(sum(map(lambda row: int(row), file)))
file.close()