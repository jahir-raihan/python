nums1 = [1, 3]
nums2 = [2]
lst = sorted(nums1 + nums2)

if len(lst) % 2 != 0:
    median = float(lst[len(lst)//2])

else:
    length = len(lst)//2
    median = (lst[length-1] + lst[length]) / 2

print(median)
