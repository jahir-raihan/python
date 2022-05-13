def int_to_roman(s):
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

    L = str(s)
    intL = int(L)

    res = ""

    while intL > 0:

        def check_recursively(L, i=0, res='', intL=0):
            try:
                res = dic[L[i:]] + res
                intL -= int(L[i:])
                L = str(intL)
                return [res, L, intL]
            except:
                if len(L) > 1 and L[i + 1:] == len(L[i + 1:]) * '0':
                    temp = str(int(L) // int(L[i]))
                    try:
                        res = dic[temp]
                        intL -= int(temp)
                        L = str(intL)
                        return [res, L, intL]
                    except:
                        pass
                elif L[i:] == L[-1]:
                    res = "I" + res
                    intL -= 1
                    L = str(intL)
                    return [res, L, intL]
                else:

                    return check_recursively(L[i+1:], i=0,  res=res, intL=intL)
        data = check_recursively(L, intL=intL)
        L = data[1]
        res = data[0] + res
        intL = data[2]
    return res



print(int_to_roman(58))