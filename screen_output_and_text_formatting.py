person = "Liam Hemsworth"
city = "Los Angeles"
value = 38.437930323932


print(person)
print(person , city)   # str(person) + ' ' + str(city) + '\n'

print(person, end=" ")
# if ....
#    print...
# else
#    print...
print(city)
print()

print(person, city, value, sep=".")
print(person, city, value, sep="/")
print(person, city, value, sep="")
print(person, city, value, sep=", ")
print()

# city:person
print(f"{city}:{person}")
print(f"2 + 2 = {2 + 2}")

print(f"{person} lives in {city}, CA")  #  python 3.6+

print("{} lives in {}, CA".format(person, city))  # python -3.5

print(f"Value is {value:.2f}")

print(f"actor is {person.upper()}")









