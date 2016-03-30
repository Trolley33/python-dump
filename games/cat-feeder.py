import tkinter as tk
import time


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cat feeder")

        self.hunger = 0
        self.start_time = int(time.time())
        self.days = 0

        self.h_label = tk.Label(text="Hunger: 0")
        self.d_label = tk.Label(text="Days: 0")

        self.f_button = tk.Button(text="Feed", command=self.feed)

        self.h_label.grid(column=0, row=0)
        self.d_label.grid(column=0, row=1)

        self.f_button.grid(column=0, row=2)

        self.update()
        self.root.mainloop()

    def feed(self):
        if self.hunger >= 5:
            self.hunger -= 5
        self.h_label.configure(text="Hunger: {}".format(self.hunger))
        self.d_label.configure(text="Days: {}".format(self.days))

    def update(self):
        if self.hunger >= 100:
            self.lose()
            return

        current_time = int(time.time())
        d_seconds = current_time - self.start_time
        print(d_seconds)
        if d_seconds % 60 == 0 and d_seconds != 0:
            self.hunger += 50
        self.days = d_seconds // (60*60*24)

        self.h_label.configure(text="Hunger: {}".format(self.hunger))
        self.d_label.configure(text="Days: {}".format(self.days))

        self.root.after(1000, self.update)

    def lose(self):
        self.h_label.configure(text="The cat died.")
        self.d_label.configure(text=":(")
        self.f_button.grid_forget()

app = App()