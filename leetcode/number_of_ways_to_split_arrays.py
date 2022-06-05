nums = [i for i in range(10**5)]
res = 0


for i in range(len(nums)):
    print(nums[i])

    print(nums[:5000])
    #
    # arr2 = nums[i+1:]
    #
    # if len(arr2) >= 1 and len(arr1) >= 1:
    #     if sum(arr1) >= sum(arr2):
    #         res += 1
    # else:
    #     break


print(res)
