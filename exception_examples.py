import logging

logging.basicConfig(
    level = logging.INFO,
    filename="secdemo.log",
    # format=...
    # datefmt=...
)

logger = logging.getLogger()

logger.info("Starting program")

#

try:
    file_path = "world_bitcoin_futures.csv"
    with open(file_path) as bc_in:
        pass
except (FileNotFoundError, PermissionError)  as err:
    logger.error("Unable to open file %s", file_path)

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

try:
    print(fruits[29])
except IndexError as err:
    print(err)
except Exception as err:
    print("UNEXPECTED!", err)

nums = [800, 80, 17, 1000, 32, -4, 0,  255, -8, 400, 0, 5, 5000]

for num in nums:
    try:
        result = 10000 / num
    except ZeroDivisionError as err:
        print(err)
    else:
        print(result)

logger.info("Ending program")










print("ALL DONE")
