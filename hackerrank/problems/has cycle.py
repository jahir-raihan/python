def stringAnagram(dictionary, query):
    res = []
    for i in range(len(query)):
        temp = query[i]
        t = query[i]
        ana = 0

        for j in range(len(dictionary)):
            temp1 = dictionary[j]

            for k in range(len(temp1)):
                c = dictionary[j][k]
                temp = temp.replace(c, '')
                temp1 = temp1.replace(c, '')

            ana += 1 if temp == temp1 else 0
            temp = t

        res.append(ana)

    return res

    # Write your code here


# dictionary_count = int(input().strip())

dictionary = ['heater', 'cold', 'clod', 'reheat', 'docl', ]

# for _ in range(dictionary_count):
#     dictionary_item = input()
#     dictionary.append(dictionary_item)

# query_count = int(input().strip())

query = ['cold', 'heater', 'abcd']

# for _ in range(query_count):
#     query_item = input()
#     query.append(query_item)

print(stringAnagram(dictionary, query))