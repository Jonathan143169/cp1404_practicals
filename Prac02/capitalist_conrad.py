import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1
MAX_PRICE = 100
INITIAL_PRICE = 10.0
DAY = 0
file_name = 'OUTPUT_FILE.txt'
price = INITIAL_PRICE

out_file = open(file_name, 'w')
print("Starting price: ${:,.2f}".format(price), file=out_file)
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    DAY = DAY + 1
    price *= (1 + price_change)
    print("On day {} the price is: ${:,.2f}".format(DAY, price), file=out_file)

out_file.close()
