fruit_lst = ["mango", "banana", "Apple"]
print(fruit_lst)

print(fruit_lst[2])

fruit_lst[2] = "orange"
print(fruit_lst)

# append
fruit_lst.append("pears")
print(fruit_lst)

# remove
fruit_lst.remove("banana")
print(fruit_lst)

# delete item by index
del fruit_lst[1]
print(fruit_lst)

# remove last item
fruit_lst.pop()
print(fruit_lst)

fruit_lst.insert(1,"apple")
print(fruit_lst)


