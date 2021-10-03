from collections import Counter
[print(*c) for c in Counter(sorted(input())).most_common(3)]

