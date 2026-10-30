n = input(str("enter string"))
vow = 0
cons = 0

for ch in n:
    if ch.isalpha:
        if ch in "aeiouAEIOU":
            vow += 1
        else :
            cons += 1
print(vow);
print(cons);
