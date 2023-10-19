from pprint import pprint

d1 = dict()   #  empty
d2 = {'file': 'wombat.txt', 'repeat': 0, 'animal': 'wombat'}
d3 = {}

#  () [] {}
airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

airports['DCA'] = 'Washington'
airports['BWI'] = 'Baltimore'
# .....

airports['BWI'] = 'Washington'
print(f"len(airports): {len(airports)}")

names = {}
names['John'] = 14
names['Eugene'] = 9
names['Michael'] = 42

colors = ['a', 'b', 'c']

# names[colors] = 5

print(f"airports: {airports}")
print()

pprint(airports)
print()

del airports['EWR']   # del DICT[key]
pprint(airports)
print()

print(f"airports['RDU']: {airports['RDU']}")
print(f"airports['YYZ']: {airports['YYZ']}")
# print(f"airports['HOU']: {airports['HOU']}")
print(f"airports.get('HOU'): {airports.get('HOU')}")
print(f"airports.get('LHR'): {airports.get('LHR')}")
print(f"airports.get('HOU', 'TOO HUMID'): {airports.get('HOU', 'TOO HUMID')}")
print()

# for key, value in DICT.items()
for code, city in airports.items():
    print(code, city)
print()

print(f"airports.keys(): {airports.keys()}")
print(f"airports.values(): {airports.values()}")









