#slicing in list
num = [0 ,1 , 2, 3, 4, 5, 6, 7, 8, 9]

# slice from 2 to 5
slice1 = num[2:6]
print(slice1)

# begining to index 4
slice2 = num[:5]
print(slice2)


# get every 2nd item from the list
slice3 = num[::2]
print(slice3)

# get last 3 item from the list
slice4 = num[-3:]
print(slice4)

# get every 2nd item from index 1 to 8
slice5 = num[1:9:2]
print(slice5)