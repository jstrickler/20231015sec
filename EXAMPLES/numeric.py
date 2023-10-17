import sys


a = 5
b = 10
c = 20.22
d = 0o123        # Octal
e = 0xdeadbeef   # Hex
f = 0b10011101   # Binary 

print("a, b, c", a, b, c)
print("a + b", a + b)
print("a + c", a + c)
print("d", d)
print("e", e)
print("f", f)

print(sys.float_info)  # 15 digits of precision

x = 23
y = 8

print(x + y, x - y, x * y)
print(x / y, x // y, x // -y)
print(x ** y, x % y)

x = 5
x += 3  # x = x + 3
x /= 2  # x = x / 2 
print(x)

a = 123
b = "456"

# result = a + b  INVALID
print(a + int(b))
print(str(a) + b)

b = "456.5"
print(int(float(b)))

print(globals())



