
i = 0
while i < 3:
    print(f"i: {i}")
    i += 1
print()

while True:
    country = input("What country do you want to visit? ")
    if country == 'q':
        break
    if country == '':
        print("PLEASE ENTER A COUNTRY")
        continue
    print(f"Have a nice time in {country}") 

