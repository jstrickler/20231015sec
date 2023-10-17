
print('26\u00B0')  # Use \uXXXX where XXXX is the Unicode value in hex
print(r'26\u00B0\n')  # unicode is not evaluated in raw strings

print('we spent \u20ac1.23M for an original C\u00e9zanne')
print("Romance in F\u266F Major")
print()

print("hallo, wereld")  # Dutch!
print("\u0928\u092e\u0938\u094d\u0924\u0947\u0020\u0926\u0941\u0928\u093f\u092f\u093e!") # hindi
print("\u4f60\u597d\u4e16\u754c!") # chinese
print("\u0417\u0434\u0440\u0430\u0432\u0435\u0439\u0020\u0441\u0432\u044f\u0442!") # bulgarian
print("\u00a1\u0048\u006f\u006c\u0061\u0020\u004d\u0075\u006e\u0064\u006f\u0021") # spanish
print("!\u0645\u0631\u062d\u0628\u0627\u0020\u0628\u0627\u0644\u0639\u0627\u0644\u0645") # arabic
print()

data = ['\U0001F95A', '\U0001F414']  # answers the age-old question (at least for Python)
print("unsorted:", data)
print("sorted:", sorted(data))

m = "Mississippi"
print('iss' in m)
print('wombat' in m)
print("Mississippi" in m)

a = 'donut'
b = "hole"
c = a + b
print(c)

print(len(c), len(m))

actor = "Chris Hemsworth"

print(actor.upper())
#  .upper() .lower() .title() .capitalize()

x = actor.upper()   # calling method from object
y = len(actor)   # passing object to function

print(actor.count('h'))
print(actor.lower().count('h'))

# .startswith(s) .endswith(s)

file = "poodle.pdf"
trimmed_file = file.removesuffix('.pdf')
print(file)
print(trimmed_file)

languages = "Python Perl C# Java Kotlin Scala Prolog Pascal"

language_list = languages.split()
print(language_list)

date = "10/12/2023"
date_parts = date.split('/')
print(date_parts)

# timestamp = "10/23/2023 08:22:19"

# timestamp_parts = timestamp.split(" /:")
# print(timestamp_parts)

s = "     Guido is a Dutch guy who changed the world     "
print(s + "|")
print(s.rstrip() + "|")
print(s.lstrip() + "|")
print(s.strip() + "|")

s = "uogtGuido is a Dutch guy who changed the worldgoua"
print(s.strip("toguamr") + "|")

s = "$423"
print(s.lstrip('$'))

s = "34593#"
s = s.rstrip("#")
print(s)

print(actor)
print(actor[:-3])
print(actor.find('Chris'))
print(actor.find('wor'))
print(actor.find('Liam'))












