from pprint import pprint
data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        key = name, title
        data[key] = color, quest, comment

pprint(data)

print(data[('Arthur', 'Sir')][0])
print(data[('Arthur', 'King')][0])
