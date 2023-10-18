import sys

print("This will NOT WORK")

print(f"sys.argv: {sys.argv}")

if len(sys.argv) >= 2:
    color = sys.argv[1]
    print(f"Using color {color}")
else:
    print("Please specify a color on the command line")
    sys.exit(1)

#  () [] {}  
#   "abc"  "def" 
# (
#   "long string part 1"
#    "long string part 2"
# )








