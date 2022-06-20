# def most_frequent(List):
#     dict = {}
#     count, itm = 0, ''
#     for item in List:
#         dict[item] = dict.get(item, 0) + 1
#         if dict[item] >= count:
#             count, itm = dict[item], item
#     return (itm)
#
#
# List = [5, 7, 5, 7, 4]
# print(most_frequent(List))
#


"""One day i will come back and solve this problem."""
#
# class FreqStack:
#
#     def __init__(self):
#         self.stack = []
#
#     def push(self, val):
#         self.stack.append(val)
#
#     def most_frequent(self, List):
#         dic = {}
#         count, itm = 0, ''
#         i = 0
#         for item in List:
#             dic[item] = dic.get(item, 0) + 1
#             if dic[item] >= count:
#                 count, itm = dic[item], item
#         dic = {}
#         for i in range(len(List)):
#             dic[List[i]] = i
#         return dic[itm]
#
#     def pop(self):
#         return self.stack.pop(self.most_frequent(self.stack))
#
#
# # Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(5)
# obj.push(7)
# obj.push(5)
# obj.push(7)
# obj.push(4)
# obj.push(5)
# obj.pop()
# obj.pop()
# obj.pop()
# obj.pop()
#
#
