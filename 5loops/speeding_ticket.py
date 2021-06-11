
DIVIDER = "---"
NO_TICKET = "no ticket"

def is_birthday(birthday_text):
    birthday_text = birthday_text.lower()
    
    if birthday_text == "y" or birthday_text == "yes":
        return True
    
    # Assumes any other answer is "no" or backtalk/sass resulting in full fine
    return False

def check_speed(speed, is_birthday):
    #   if it is the person's birthday, they get a 5mph break
    if is_birthday:
        speed-=5
    if speed <= 60:
        return NO_TICKET
    if speed <= 80:
        return "small ticket"
    return "big ticket"

def traffic_stop():
    vehicle_speed = float(input("How fast were they going?:  "))
    is_driver_birthday = is_birthday(input("Is it their birthday (y/n): "))
    # print result of check speed function
    stop_outcome = check_speed(vehicle_speed, is_driver_birthday)
    print(stop_outcome)
    # if the result of the stop is not a ticket
    if stop_outcome == NO_TICKET:
        return False
    return True


print("\n")
# Ask the user for the quota and validate to the program doesn't fail
while True:
    try:    
        quota = int(input("What is today's quota?: "))
        break
    except ValueError:
        print("That is not valid input for quota. Please try again.")
        continue

# Prompt the user enough times to reach the quota
# Some variable to tell us how many tickets have been written
tickets_written = 0

# while we have not yet reached the quota, prompt again
tickets_array = []
hightest_speed = 0

while tickets_written < quota:
    # traffic stop
    # make sure the stop resulted in a ticket
    speed = traffic_stop()
    if speed > 60:
        # Increment the ticket var 
        tickets_written += 1
        # change traffic_stop to return speed
        tickets_array.append(speed)
    # compare quota to numer of times through the loop
    print(DIVIDER)
    
print("\n")