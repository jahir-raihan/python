def find_longest_p(s):
    i, li = 0, ''
    k = length = len(s)
    for n in range(length):
        for j in range(length):

            if s[i:k] and s[i:k] == s[i:k][::-1]:
                li = s[i:k] if len(s[i:k]) > len(li) else li
                k -= 1
                continue
            k -= 1

        i += 1
        k = length
    return li


string = 'cbbd'
# 2


def find_mid(string):
    i = 0
    for j in range(len(string), 0, -1):
        print(string[i:j])
        i += 1
        j -= 1


def printing_backwards(string):
    i = 0
    j = len(string)

    for k in range(len(string)):
        print(string[i:j][::-1])
        i += 1


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

matrix.reverse()
for i in range(len(matrix)):
    for j in range(i):
        matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

print(*matrix, sep='\n')
