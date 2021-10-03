from datetime import datetime
time = [15,30,00]
time2 = [16,00,00]
strtime = ':'.join(str(i) for i in time)
strtime2 = ':'.join(str(i) for i in time2)
n = datetime.strptime(strtime, '%H:%M:%S') - datetime.strptime(strtime2, '%H:%M:%S')
left_time = int(abs(n).total_seconds())//60


if left_time>=30:
    print('i have time')