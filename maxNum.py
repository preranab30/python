lst = []
n = int(input())
for i in range(n):
    el = int(input())
    lst.append(el)

tuple = tuple(lst)

max = tuple[0]
for i in range (1, len(tuple)):
    if tuple[i] > max:
        max = tuple[i]
print("Maximum Number: ", max)

