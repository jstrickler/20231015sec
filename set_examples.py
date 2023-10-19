
colors1 = ['red', 'purple', 'pink', 'orange', 'chartreuse', 'brown', 'pink', 'brown', 'blue']


c1 = set(colors1)
print(f"c1: {c1}")
c2 = set()
print(f"c2: {c2}")
c2.add('green')
c2.add('blue')
c2.add('red')
c2.add('orange')
c2.add('orange')
c2.add('pink')
print(f"c2: {c2}")

print("COMMON:", c1 & c2)  # intersection
print("NOT COMMON:", c1 ^ c2)  # xor
print("ALL:", c1 | c2)  # union
print("JUST c1:", c1 - c2)
print("Just c2:", c2 - c1)
print(f"(c1 - c2) | (c2 - c1): {(c1 - c2) | (c2 - c1)}")
