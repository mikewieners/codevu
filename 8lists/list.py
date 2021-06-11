collection = [0, 1]
print(collection)

while len(collection) < 11:
    collection.append(collection[-1]+collection[-2])

for i in collection:
    print(i)