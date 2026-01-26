from datetime import datetime

DATETIME_FORMAT = '%d.%m.%Y; %H:%M'

with open('diary.txt', 'r', encoding='utf-8') as file:
    result = file.read().split('\n\n')

result = sorted(
    result,
    key=lambda x: datetime.strptime(x[:17], DATETIME_FORMAT)
)

print('\n\n'.join(result))
