from collections import OrderedDict
ordered_dictionary = OrderedDict()

for i in range(int(input())):
    name = input().split()
    price = 0
    for j in name:
        try:
            price = int(j)
            name.pop()
        except:
            continue
    name = ' '.join(name)
    if name in ordered_dictionary:
        ordered_dictionary[name] += int(price)
    else:
        ordered_dictionary[name] = int(price)

for name, price in ordered_dictionary.items():
    print(name, price)
