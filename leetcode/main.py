dic = {
    '1': 'I',
    '5': 'V',
    '10': 'X',
    '50': 'L',
    '100': 'C',
    '500': 'D',
    '1000': 'M',

    '4': 'IV',
    '40': 'XL',
    '90': 'XC',
    '9': 'IX',
    '400': 'CD',
    '900': 'CM'

}
s = '30'
L = int(s)
i = 0
res = ""
while L>0:
    if s[i+1:] == len(s[i+1:])*'0':
        temp = int(s) // int(s[i])
        if dic[str(temp)]:
            res = dic[str(temp)] + res
            L -= temp
    print(L)
print(res)