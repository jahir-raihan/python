       # Hard solution without any counter function

# s = input()
# di = {}
# for i in set(s):
#  di[i] = s.count(i)
#   s = s.replace(i, '')

# print('dict',di)


# sorted_list = list(sorted(di.items(), key=lambda x: (x[1]), reverse=True))
# res = []
# for i in range(len(di)):
# print('sorted_list', sorted_list)
# try:
#  if sorted_list[0][1] == sorted_list[1][1]:
#       try:
#            if sorted_list[1][1] == sorted_list[2][1]:
#                 temp = dict(sorted_list[:3])
#                  res += sorted(temp.items(), key=lambda x: (x[0]))
#                   sorted_list = sorted_list[3:]
#
#          break
#       else:
#            temp = dict(sorted_list[:2])
#             res += sorted(temp.items(), key=lambda x: (x[0]))
#              sorted_list = sorted_list[2:]
#       except IndexError:
#            temp = dict(sorted_list[:2])
#             res += sorted(temp.items(), key=lambda x: (x[0]))
#               continue
#
# else:
#      res.append(sorted_list[0])
#       sorted_list.pop(0)
# except IndexError:
#     if not sorted_list:
#          break
#       res.append(sorted_list[0])
#        sorted_list.pop(0)


# for i in res[:3]:
#  print(*i)


        # Simple solution with Counter method of Collections

from collections import Counter
[print(*c) for c in Counter(sorted(input())).most_common(3)]