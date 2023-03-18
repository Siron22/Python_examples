"""
Расписание занятий
Занятия проходят по понедельникам и четвергам в 19:15
Первое занятие произошло 17.10.2022.
Вывести список всех занятий в таком формате (номера лекций выровнены по правому краю):

Lecture  1: 17 Oct 2022 19:15
Lecture  2: 20 Oct 2022 19:15
...
Lecture  9: 14 Nov 2022 19:15
Lecture 10: 17 Nov 2022 19:15
...
Lecture 32: 02 Feb 2023 19:15
"""
import datetime
start_datetime = datetime.datetime(year=2022, month=10, day=17, hour=19, minute=15)
diff_between_lectures_on_week = datetime.timedelta(days=3)
one_week_diff = datetime.timedelta(days=7)
lecture_number = 1


def get_line(lecture_number, datetime_of_lecture):
    date_format_string = "%d %b %Y %H:%M"
    return f"Lecture {lecture_number:>2}: {datetime_of_lecture.strftime(date_format_string)}"


for i in range(16):
    datetime_of_first_lecture_on_week = start_datetime
    print(get_line(lecture_number, datetime_of_first_lecture_on_week))
    lecture_number += 1
    datetime_of_second_lecture_on_week = (start_datetime + diff_between_lectures_on_week)
    print(get_line(lecture_number, datetime_of_second_lecture_on_week))
    lecture_number += 1
    start_datetime += one_week_diff
