
import os


def initialize(directory, schedule, classes):

    days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    empty_schedule = ["", "", "", "", "", "", ""]

    # Получаем список файлов
    files = os.listdir(directory)
    #print(files)

    for f in files:
        file_path = os.path.join(directory, f)
        klass = f.split('.')[0]
        classes.append(klass)
        schedule[klass] = [d for d in empty_schedule]

        #print(klass, file_path)

        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.rstrip() for line in file]

        day = -1
        dayschedule = ""
        for l in lines:

            if(l.lower() in days):
                # Смена дня в расписании

                if(day != -1 and len(dayschedule) > 0):
                    # print("SCHEDULE", dayschedule, klass, day)
                    schedule[klass][day] = dayschedule

                dayschedule = ""
                # Определить следующий день в расписании
                day = days.index(l.lower())
                #print("DAY", l, day)
            else:
                if(len(l.strip()) > 0):
                    if(len(dayschedule) > 0):
                        dayschedule += '\n'
                    dayschedule = dayschedule + l

    print(schedule)
