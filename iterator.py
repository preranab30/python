lst = [11, 22, 33,44, 55];

itr = iter(lst)

for i in range(0, len(lst)):
    print(next(itr))

    