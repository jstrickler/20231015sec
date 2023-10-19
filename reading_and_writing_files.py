
file_path = "DATA/mary.txt"  # same for Windows!

# x = "DATA\nelly.txt"

# mary_in = open(file_path)
with open(file_path, 'r') as mary_in:
    print(f"mary_in: {mary_in}")
    for raw_line in mary_in:  # iterate over lines
        record = raw_line.rstrip()  # remove trailing white space \n \r \t ' '
        print(f"record: {record}")
print('-' * 60)

with open(file_path) as mary_in:
    whole_file = mary_in.read()
    print(whole_file)
    print()
    print(repr(whole_file))
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_with_newlines = mary_in.readlines()
    print(f"all_lines_with_newlines: {all_lines_with_newlines}")
    all_lines_without_newlines = [line.rstrip() for line in all_lines_with_newlines]
    print(f"all_lines_without_newlines: {all_lines_without_newlines}")
    
fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')
print()


