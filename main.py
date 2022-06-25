import time
import pywhatkit
from pathlib import Path
from datetime import datetime as dt
from datetime import timedelta as td
import datetime

msg = [w for w in Path('word.txt').read_text(encoding="utf-8").split('\n')]  #  список передоваемых сообщений
yesterday = datetime.datetime(2022, 6, 20, 0, 0)  #  датаВремя с которого будут считаться таймаут цыкла
tries = 6

while True:
    time_runStep1 = dt.now()
    if (time_runStep1.strftime("%Y-%m-%d %H:%M") == '2022-06-20 00:03'):  #  время старта программы
        print('begin step 1')
        for i in msg:
            for i_try in range(tries):
                try:
                    time_runStep2 = dt.now()
                    #if (time_runStep1.strftime("%Y-%m-%d %H:%M") == '2022-05-25 19:4'):
                    print('done! step 2 ' + time_runStep2.strftime("%Y-%m-%d %H:%M"))
                    time_run = dt.now() + td(minutes=1)
                    hourToMsg = time_run.hour
                    minetsToMsg = time_run.minute
                    pywhatkit.sendwhatmsg_to_group('numbePfone', i, int(hourToMsg), int(minetsToMsg), 10, True, 10)  # функция отправки сообщения
                    yesterday = yesterday + td(minutes=15)  # Прибавляем время для расчета след запуска
                    date_now = dt.now()
                    x3 = yesterday-date_now
                    print(x3)
                    x4 = str(x3)
                    print(x4.find('-'))
                    if x4.find('-') != -1:
                        raise Exception('dade is not valid')
                    else:
                        print('date valid')
                    print('wait >> ' + str(x3))
                    time.sleep(int(x3.seconds-20))
                except:
                    if i_try < tries - 1:
                        print('ERROR! retry ' + str(i_try+1) + ' >> ' + str(tries))
                        continue
                    else:
                        print('ERROR! retry ' + str(tries) + ' >> ' + str(tries))
                        raise
                break
        print('список окончен')
        break
    print('NotReady')
    time.sleep(30)

