
fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

nums = [800, 80, 1000, 32, -4, 255, -8, 400, 5, 5000]

rfruits = reversed(fruits)  # rfruits is an iterator 
print(f"rfruits: {rfruits}")
for fruit in rfruits:
    print(fruit)
print()

for i, fruit in enumerate(fruits):
    print(i, fruit)
print()
print(f"list(enumerate(fruit)): {list(enumerate(fruit))}")
print()

for i in range(10):
    print(i)
print()

#  range(stop)   range(start, stop)   range(start, stop, step)

print(f"range(1,11): {list(range(1,11))}")

for i in range(5):
    print("We love Python")
print()
