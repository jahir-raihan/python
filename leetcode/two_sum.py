nums = [i for i in range(10**4)]

target = 19
res = 0
for i in range(1, len(nums) - 1):
    br = False
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            res = [i, j]
            br = True
            break
    if br:
        break

print(res)
