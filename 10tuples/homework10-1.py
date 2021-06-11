# function to calculate cost
def cost(loan_amount, price):
    loan_amount = float(loan_amount)
    price = float(price)
    return -(loan_amount*(price-100)/100)

# list to hold data from file
price_data = []

# get data from pricing_sheet.csv
file_name = "pricing_sheet.csv"

# open the file in a try catch block, print error if
# it's an invalid file
try:
    with open(file_name, "r") as file_handler:
        # read each line of the file into a list of lines
        lines = file_handler.readlines()

        # for each line, trim and split at comma
        # append these lists of values to the data list
        # order is: Product Name,Lock Period,Call Center Price,Rate,Investor Pricing,Srp
        for line in lines:
            line = line.strip()
            price_data.append(line.split(','))

except:
    print("File not found: ", file_name)
    exit()

# get user input for product, lock period, and loan amt
# validate input for lock and loan so we only accept integers

product = '10003.20.001'
while True:
    try:
        lock_period = int('45')
        break
    except:
        print("Invalid input, please enter a whole number.")

while True:
    try:
        loan_amount = int('250000')
        break
    except:
        print("Invalid input, please enter a whole number.")

# list to hold the lists from the csv file that match our product # and lock period
match_list = []

# search our price_data and get all lists that match our product number
for item in price_data:
    if item[0] == product:
        if int(item[1]) == lock_period:
            if item[2] != 'N/A':
                match_list.append(item)

if not match_list:
    print("Sorry, no product matches these terms.")
    exit()

# print header of data table
print("|--------------|--------|----------------|--------|")
print("|              |  Lock  |                |        |")
print("| Product Name | Period |      Cost      |  Rate  |")
print("|--------------|--------|----------------|--------|")
# format final data
# calculate cost based on loan amt and call center price
for data_line in match_list:
    table_product = data_line[0]
    table_lock = data_line[1]
    table_cost = float(cost(loan_amount, data_line[2]))
    table_cost = f'${table_cost:,.2f}'
    table_rate = float(data_line[3])
    print(f'| {table_product} | {table_lock: >6} | {table_cost: >14} | {table_rate:.3f}% |')

# Order is: Product Name,Lock Period,Call Center Price,Rate,Investor Pricing,Srp
