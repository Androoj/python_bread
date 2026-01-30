file = open('nums.txt')
file_lines = list(map(lambda row: row.strip(), file))
print(
    sum(
        list(
            map(
                lambda el: int(el),
                filter(lambda el: el.isdigit(), file_lines)
            ))))
file.close()