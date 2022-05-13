a = 'a##c'
b = '#a#c'

i = 0
while '#' in a:
    if a[i] == '#':
        a = a[1:] if i == 0 else a[:i - 1] + a[i + 1:]
        i = 0
        continue
    i += 1

i = 0

while '#' in b:
    if b[i] == '#':
        b = b[1:] if i == 0 else b[:i - 1] + b[i + 1:]
        i = 0
        continue
    i += 1

print(a == b)

