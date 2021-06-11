
NO_TICKET = "no ticket"
SMALL_TICKET = "small ticket"
BIG_TICKET = "big ticket"
DIVIDER = "---"

def is_birthday(birthday_text):
    birthday_text = birthday_text.lower()
    
    if birthday_text == "y" or birthday_text == "yes":
        return True
    
    # Assumes any other answer is "no" or backtalk resulting in full fine
    return False

def check_speed(speed, birthday):
    print("speed:", speed, "birthday:", birthday)
#   if it is the person's birthday, they get a 5mph break
    if birthday:
        speed-=5
    if speed <= 60:
        return NO_TICKET
    if speed <= 80:
        return SMALL_TICKET
    return BIG_TICKET

def validate_speed(speed):
    try:
        return float(speed)
    except ValueError:
        print(f"{speed} is not a valid speed. Please try again")
        return
        
def traffic_stop():
    while True:
        vehicle_speed = validate_speed(input("How fast were they going?:  "))

        if vehicle_speed:
            break

    is_driver_birthday = is_birthday(input("Is it their birthday (y/n): "))
    outcome = check_speed(vehicle_speed, is_driver_birthday)
    print(outcome)
    return outcome != NO_TICKET

# Let's start with my solution to last week's in-class
# exercise. (Walk through the solution and prompt for questions)

# Introduce the enhancement request:
# The department loves the app!!
# Now leadership would like the ability to adjust quota.
# The program should now start by asking the user for 
# today's quota. It should then continue doing traffic
# stops and returning the output until the quota is reached
# Only stops that result in a ticket count toward quota!

# VERY IMPORTANT NOTE: Requests for enhancements are
# good! Enhancement requests mean you have delivered
# enough value that people are using your app and they
# trust you to make it even better!

stops_completed = 0
quota = int(input("What is today's quota?: "))
while stops_completed < quota:
    if traffic_stop():
        stops_completed += 1
    
    print(DIVIDER)

# Now that's implemented, let's do some error handling.
# Where might we do that and how?

# Validate vehicle speed
# def validate_speed(speed):
#     try:
#         return float(speed)
#     except ValueError:
#         print(f"{speed} is not a valid speed. Please try again")
#         return

# What about quota? What if the user means to enter 5
# and fat fingers 56 or some other large value? Should
# we give the user a way to start over? How would you
# implement this?