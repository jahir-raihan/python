def roman_to_int(s):
    dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,

        'IV': 4,
        'XL': 40,
        'XC': 90,
        'IX': 9,
        'CD': 400,
        'CM': 900

    }
    res = 0
    length = len(s)
    i = 0
    while length > 0:
        try:
            res += dic[s[i]+s[i+1]]
            i += 2
            length -= 2
        except:
            res += dic[s[i]]
            i += 1
            length -= 1


roman_to_int("LVIII")
