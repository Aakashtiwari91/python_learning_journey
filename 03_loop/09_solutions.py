# find uniq value in list and if found duplicate print it

items = ["apple","banana","orange","apple","mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("duplicates: ",item)
        break
    unique_item.add(item)