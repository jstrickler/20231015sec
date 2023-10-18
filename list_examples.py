list1 = list()  # create one list object from list class
vegetables = list()

months = ["Jan", "Feb", "Mar"] # ...


cities = list()
print(f"cities: {cities}")

cities.append('Tokyo')
print(f"cities: {cities}")

cities.append("Durham")
cities.append('Chicago')
print(f"cities: {cities}")
cities.insert(0, 'Topeka')
cities.insert(3, "Pittsburgh")
print(f"cities: {cities}")

more_cities = ['Miami', 'Dallas', 'Portland', 'Los Angeles']
cities.extend(more_cities)
print(f"cities: {cities}")

#  LIST.append(obj)   LIST.insert(pos, obj)   LIST.extend(iterable)

del cities[5]
print(f"cities: {cities}")
print(f"cities.index('Durham'): {cities.index('Durham')}")

cities.remove('Durham')

print(f"cities: {cities}")

city = cities.pop()   # remove and return last element
print(f"city: {city}")
print(f"cities: {cities}")

city = cities.pop(2)
print(f"city: {city}")
print(f"cities: {cities}")

#  del LIST[pos]    LIST.remove(value)    x = LIST.pop()    x = LIST.pop(pos)

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"fruits[0]: {fruits[0]}")
print(f"fruits[14]: {fruits[14]}")
print(f"len(fruits): {len(fruits)}")
print(f"fruits[21]: {fruits[21]}")
print(f"fruits[len(fruits)-1]: {fruits[len(fruits)-1]}")
print(f"fruits[-1]: {fruits[-1]}")

b_fruits = [f for f in fruits if f.startswith('b')]
print(f"b_fruits: {b_fruits}")

#  [ EXPR for VAR in ITERABLE if CONDITION]
print(f"fruits[0:5]: {fruits[0:5]}")
print(f"fruits[8:12]: {fruits[8:12]}")

#   [start:sentinel]   [:sentinel]  [start:]   
s = "Securities and Exchange Commission"
print(f"s[15:23]: {s[15:23]}")
print(f"s[24:]: {s[24:]}")
print(f"s[-7:]: {s[-7:]}")
print()

for fruit in fruits:
    print(fruit)
print()

for car in 'BMW', 'Audi', 'Lamborghini':
    print(f"My {car} goes fast")
print()

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
]

for person in people:
    print(person)
print()

for first_name, last_name, *product, dob in people:
    print(first_name, last_name, product)
    if product ==  ['BASIC']:
        break
print()

a = 'foot'
b = 'ball'
sport = a + b
print(f"sport: {sport}")
print()

j = [1, 2, 3]
k = [4, 5, 6]
m = j + k
print(f"m: {m}")

print('-' * 60)

flags = [False] * 10
print(f"flags: {flags}")
print()

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(min(fruits), max(fruits), sorted(fruits))
print('-' * 60)

nums = [800, 80, 1000, 32, -4, 255, -8, 400, 5, 5000]

print(min(nums), max(nums), sorted(nums))

fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

print(f"sorted(fruits): {sorted(fruits)}\n")

print(f"sorted(fruits, key=str.lower): {sorted(fruits, key=str.lower)}\n")

print(f"sum(nums): {sum(nums)}")




















