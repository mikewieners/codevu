# cost = -(loan_amount * ((call_center_price - 100)/100))
# Enter Product Name: 10003.20.001
# Enter Lock Period : 45
# Loan Amount       : 250000
# |--------------|--------|----------------|--------|
# |              |  Lock  |                |        |
# | Product Name | Period |      Cost      |  Rate  |
# |--------------|--------|----------------|--------|
# | 10003.20.001 |     45 |      $5,955.00 | 4.250% |
# | 10003.20.001 |     45 |      $4,355.00 | 4.375% |
# | 10003.20.001 |     45 |      $2,512.50 | 4.500% |
# | 10003.20.001 |     45 |      $1,865.00 | 4.625% |
# | 10003.20.001 |     45 |      $1,557.50 | 4.750% |
# | 10003.20.001 |     45 |          $0.00 | 4.875% |
# | 10003.20.001 |     45 |       $-607.50 | 4.990% |
# | 10003.20.001 |     45 |     $-1,270.00 | 5.125% |
# | 10003.20.001 |     45 |     $-1,582.50 | 5.250% |
# | 10003.20.001 |     45 |     $-1,875.00 | 5.375% |
# | 10003.20.001 |     45 |     $-2,202.50 | 5.500% |
# | 10003.20.001 |     45 |     $-2,480.00 | 5.625% |
# | 10003.20.001 |     45 |     $-2,795.00 | 5.750% |
# | 10003.20.001 |     45 |     $-4,380.00 | 5.875% |

def get_pricing_data(loan_amount, values):
    cost = calculate_cost(loan_amount, float(values[2]))
    rate = values[3]

    return cost, rate

def calculate_cost(loan_amount, call_center_price):
    return -(loan_amount * ((call_center_price - 100)/100))

def print_header():
    print('|--------------|--------|----------------|--------|')
    print('|              |  Lock  |                |        |')
    print('| Product Name | Period |      Cost      |  Rate  |')
    print('|--------------|--------|----------------|--------|')



requested_product = '10003.20.001'
lock_period = 45
loan_amount = 250000
cost_list = list()

with open('pricing_sheet.csv') as file_handler:
    for row in file_handler:
        if row.startswith(requested_product):
            values = row.split(',')
            if values[2].lower() != 'n/a' and int(values[1]) == lock_period:
                cost_list.append(get_pricing_data(loan_amount, values))

if len(cost_list) > 0:
    print_header()
    for i in sorted(cost_list, reverse=True):
        print(f'| {requested_product} | {lock_period:>6} | {f"${i[0]:,.2f}":>14} | {float(i[1])/100:.3%} |')

else:
    print(f'The specified product and rate combination of {requested_product} and {lock_period} is not available.')