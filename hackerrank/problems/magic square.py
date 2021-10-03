def findMinimumFromMS(arr, ms):
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if arr[i][j] != ms[i][j]:
                count += 1
    return count


def findMinimum(arr):
    ms = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]

    Min = 9
    for i in range(0, 8):
        x = findMinimumFromMS(arr, ms[i])
        if x < Min:
            Min = x

    return Min


if __name__ == "__main__":
    arr = []
    for i in range(3):
        arr.append(list(map(int, input().split())))
    print(findMinimum(arr))

