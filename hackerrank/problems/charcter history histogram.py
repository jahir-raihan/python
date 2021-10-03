from os import strerror


class StudentsDataException(Exception):
    pass


class BadLineError(StudentsDataException):
    pass


class FileEmpty(StudentsDataException):
    # Write your code here.
    pass


file = 'Book1.csv'

d = {}
try:
    f = open(f'/Users/nazrulislam/Desktop/{file}', 'rt')
    j = f.readlines()
    if len(j) == 0:
        raise FileEmpty

    for ch in j:
        temp = ch.split()
        if len(temp) > 3 or len(temp) < 3:
            raise BadLineError
        f_l = temp[0] + temp[1]
        if f_l in d:
            d[f_l] += float(temp[2])
        else:
            d[f_l] = float(temp[2])

    print(dict(sorted(d.items())))
except FileNotFoundError as e:
    print('No such File in directory')
except BadLineError as e:
    print('Not enough data to extract', e)
except FileEmpty as e:
    print('No such data in the file',e )
except StudentsDataException as e:
    print('No such file on directory', e)

