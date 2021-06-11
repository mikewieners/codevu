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

for i in to_do_list.items():
    print(type(i))

to_dos_for_sort = []

for key, value in to_do_list.items():
    to_dos_for_sort.append((value, key))

to_dos_for_sort.sort()

for i in to_dos_for_sort:
    print(f"Priority {v}:\n-", k)