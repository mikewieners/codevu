to_do_list = dict()
choice = 0
while choice != 3:
    user_input = input("To Do Options\n1) Add To Do\n2) View To Dos\n3) Exit \n")
    try:
        choice = int(user_input)
    except:
        print("Please enter a valid menu choice ")
        continue