to_do_list = {
    'Watch The Masters': 4,
    'Have a snack': 5,
    'Take a break after completing two items': 3,
    "Check off first task": 2,
    'Start list': 1,
    'Nap': 6,
    'Have lunch': 7,
    'Take another break': 8,
    'Shower (if smelly)': 9,
    'Snack time!': 10
}

print("--- My To Do List ---")
# for i in range(1, 11):
#     for k, v in to_do_list.items():
#         if v == i:    
#             print(f"Priority {v}:\n-", k)

# for i in to_do_list.items():
#     print(type(i))
#     print(f"{i[0]}: {i[1]}")

def sort_to_dos(some_dict):
    list_out = []
    for key, value in some_dict.items():
        list_out.append((value, key))

    list_out.sort()
    return list_out

sorted_to_dos = []
sorted_to_dos = sort_to_dos(to_do_list)
print(sort_to_dos(to_do_list))