hour, minute, second_form = input().split(':', 2)

if 'PM' in second_form and int(hour) < 12:
    hour = str(int(hour)+12)
    n = second_form.replace('PM','')
    print(f'{hour}:{minute}:{n}')

elif int(hour) == 12 and 'PM' in second_form:
    n = second_form.replace('PM','')
    print(hour+':'+)


elif 'AM' in second_form and int(hour) == 12:
    hour = '00'
else:
    print(f'{hour}:{minute}:{second_form}')

