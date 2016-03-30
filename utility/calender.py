__author__ = "Reece"

import tkinter as tk
from datetime import datetime, time


class DayOfWeek():
    def __init__(self, name, col, *lessons):
        self.name = name
        self.col = col

        self.lessons_dict = {}

        self.name_label = tk.Label(text=self.name, font=("fixedsys", 18, "bold"), bg="black", fg="lightgray")
        self.name_label.grid(column=self.col, row=0)
        for l in zip(range(1, len(lessons)+1), lessons):
            self.lessons_dict[l[0]] = tk.Label(text=l[1], font=("fixedsys", 14), bg="black", fg="lightgray")
            if l[1] in ["Lunch", "Break"]:
                self.lessons_dict[l[0]].configure(fg="purple1")
            self.lessons_dict[l[0]].grid(column=self.col, row=l[0])

    def change_colour(self, box):
        self.name_label.configure(fg="green2")
        for l in self.lessons_dict:
            if box == l:
                self.lessons_dict[l].configure(fg="green2")

            elif self.lessons_dict[l].cget("text") in ["Lunch", "Break"]:
                self.lessons_dict[l].configure(fg="purple1")

            elif box == 0:
                self.name_label.configure(fg="lightgray")

            else:
                self.lessons_dict[l].configure(fg="lightgray")


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.config(bg="black")
        self.root.title("Calender")
        break_vmg = "Break"
        lunch = "Lunch"
        self.mon = DayOfWeek("Monday", 1, "", "Tutor", break_vmg,
                             "Computing", lunch, "Computing", "Computing")

        self.tus = DayOfWeek("Tuesday", 2, "Chemistry", "Chemistry", break_vmg,
                             "Physics", lunch, "Physics", "Physics")

        self.wed = DayOfWeek("Wednesday", 3, "Maths", "Maths", '',
                             "", '', "", "")

        self.thu = DayOfWeek("Thursday", 4, "Computing", "Computing", break_vmg,
                             "Maths", "Maths", lunch, "Maths")

        self.fri = DayOfWeek("Friday", 5, "Physics", "Physics", break_vmg,
                             "Chemistry", "Chemistry", lunch, "Chemistry")

        self.days = {
            1: self.mon,
            2: self.tus,
            3: self.wed,
            4: self.thu,
            5: self.fri
        }

        self.check_day()
        self.root.mainloop()

    def check_day(self):
        date = datetime.today().weekday() + 1
        self.days[date].change_colour(self.check_time())
        self.root.after(1000, self.check_day)

    @staticmethod
    def check_time():
        # 8:25
        a = 30300
        # 9:25
        b = 33900
        # 10:25
        c = 37500
        # 11:00
        d = 39600
        # 12:00
        e = 43200
        # 13:00
        f = 46800
        # 13:30
        g = 48600
        # 14:30
        h = 52200

        # External
        utcnow = datetime.utcnow()
        midnight_utc = datetime.combine(utcnow.date(), time(0))
        delta = utcnow - midnight_utc
        secs = delta.seconds + (60*60)
        if a <= secs < b:
            return 1
        elif b <= secs < c:
            return 2
        elif c <= secs < d:
            return 3
        elif d <= secs < e:
            return 4
        elif e <= secs < f:
            return 5
        elif f <= secs < g:
            return 6
        elif g <= secs < h:
            return 7
        else:
            return 0

app = App()