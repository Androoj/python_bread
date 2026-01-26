"""
В переменной florida_hurricane_dates хранится список дат (тип date), в которые произошел ураган во Флориде с 1950 по 2017 год.

Дополните приведенный ниже код, чтобы он вывел самую раннюю дату из списка florida_hurricane_dates в трех различных форматах:

в стандарте ISO (YYYY-MM-DD)
в типичном для России стиле (DD.MM.YYYY)
в типичном для Америки стиле (MM/DD/YYYY)
"""
import locale
from datetime import date

florida_hurricane_dates = [date(2014, 9, 24), date(2008, 12, 13)]

# присваиваем самую раннюю дату урагана в переменную first_date
first_date = min(florida_hurricane_dates)

# конвертируем дату в ISO и RU формат
iso = 'Дата первого урагана в ISO формате: ' + first_date.strftime('%A')
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%A')
locale.setlocale(locale.LC_ALL, 'us_US.UTF-8')
us = 'Дата первого урагана в US формате: ' + first_date.strftime('%A')

print(iso)
print(ru)
print(us)
