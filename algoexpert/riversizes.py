matrix = [
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
]


def river_size(matrix):
    """
    This program is to find out how many adjacent 1 are available
    in the whole matrix.

    While looping if we encounter 1 , then we pushed the index location of that one in a stack
    to find out more adjacent 1 .
    """
    visited = {}  # This dict will be used for determining whether any index is visited or not.

    stack = []  # Stack for continues loop to find out all adjacent 1.

    res = []    # Final result will be stored at here.

    for i in range(len(matrix)):    # Looping through the matrix length.

        for j in range(len(matrix[i])):     # Looping through the inner matrix list length.

            if matrix[i][j] == 1:   # If 1 encountered

                stack.append((i, j))    # Add it to stack .To check vertically and horizontally.

                output = func(visited, stack)   # Function call to check all adjacent 1 .

                if output > 0:  # If the function returns a value which is grater then 0.

                    res.append(output)  # we will store the output in res list.
            else:
                visited[(i, j)] = True  # If 1 not encountered , we've just marked it as visited.

    return res  # Finally returning the result


def func(visited, stack):   # This function took 2 parameters a dict and a stack. Dict which is a visited markup .

    cnt = 0     # initial value . will be update later if we encounter 1 again.

    while stack:    # Looping until the stack becomes empty.

        p = stack.pop()     # Popping the last element from the stack.

        if p not in visited:    # Checking whether the popped stack element is already in the visited dict or not.

            visited[p] = True   # If not visited then mark it as visited , which will help us to not visit it again.

            cnt += 1    # increasing the value by one .Because the popped index contain 1 in the matrix.

            """
            This conditions are used for checking the popped element left side , right side , top and bottom side.
            If we find 1 in any direction, we've just pushed the index location again in to the stack for checking 
            again.
            
            """
            if p[1] + 1 <= len(matrix[p[0]]) - 1 and matrix[p[0]][p[1] + 1] == 1:
                stack.append((p[0], p[1] + 1))

            if p[0] + 1 <= len(matrix) - 1 and matrix[p[0] + 1][p[1]] == 1:
                stack.append((p[0] + 1, p[1]))

            if p[1] - 1 >= 0 and matrix[p[0]][p[1] - 1] == 1:
                stack.append((p[0], p[1] - 1))

            if p[0] - 1 >= 0 and matrix[p[0] - 1][p[1]] == 1:
                stack.append((p[0] - 1, p[1]))

    return cnt
