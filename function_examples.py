data = ["$1000", "$540", "$800", "$950"]

def strip_dollar(value):
    return int(value.lstrip('$').replace(',', ''))

clean_data = [strip_dollar(d) for d in data]
print(f"clean_data: {clean_data}")

result = strip_dollar("$239,891")
print(f"result: {result}")

def bark():
    print("Woof! Woof!")

x = bark()
print(f"x: {x}")




