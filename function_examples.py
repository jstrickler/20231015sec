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

def doit(a, b):
    print(f"a: {a}    b: {b}")

doit(5, 10)
doit('foo', 'bar')

doit(b=100, a="fred")

def double(x):
    return x * current_value

current_value = 25

print(f"double('take'): {double('take')}")
print(f"double(5): {double(5)}")


def ugh():
    """
      Just some random function. 
      Not for professional use. Your mileage may vary.
    """
    current_value = 100  # local variable

ugh()

print(f"value: {current_value}")

name = "Gandalf"
name.lstrip()

















