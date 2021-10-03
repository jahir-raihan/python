matrix = [
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 1]
  ]


def river_size(matrix):
    visited = {}
    stack = []
    res = []
    for i in range(len(matrix)):

        for j in range(len(matrix[i])):

            if matrix[i][j] == 1:
                stack.append((i, j))
                output = func(visited, stack)
                if output > 0:
                    res.append(output)
            else:
                visited[(i, j)] = True
    return res


def func(visited, stack):
    cnt = 0
    while stack:
        p = stack.pop()
        if p not in visited:
            visited[p] = True
            cnt += 1
            try:
                if p[1] + 1 <= len(matrix[p[0]]) and matrix[p[0]][p[1] + 1] == 1:

                    stack.append((p[0], p[1] + 1))
            except:
                pass


            try:
                if matrix[p[0] + 1][p[1]] == 1:
                    stack.append((p[0] + 1, p[1]))
            except:
                pass
    return cnt


print(river_size(matrix))


