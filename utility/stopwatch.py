__author__ = 'Reece'


import tkinter as tk

class App():
    def __init__(self):
        self.base_m_seconds = 0
        # Root Configuration
        self.root = tk.Tk()
        self.root.title("Timer")
        self.root.configure(bg="black")
        self.root.wm_attributes("-topmost", 1)
        self.root.focus()
        # Rest
        self.text = tk.Label(text="Time passed", fg="green2", bg="black", font=("fixedsys", 20))
        self.timer = tk.Label(text="00:00:00", fg="green2", bg="black", font=("fixedsys", 20))
        self.start_stop = tk.Button(text="Start", command=self.start,
                                fg="green2", bg="black", font=("fixedsys", 15), borderwidth=0)
        self.reset_button = tk.Button(text="Reset", command=self.reset,
                                fg="green2", bg="black", font=("fixedsys", 15), borderwidth=0)
        self.text.pack()
        self.timer.pack()
        self.start_stop.pack()
        self.reset_button.pack()
        self.count = False
        self.root.mainloop()

    def update_clock(self):
        if self.count:
            now = self.time_work()
            self.timer.configure(text = now)
            self.root.after(100, self.update_clock)

    def start(self):
        self.count = True
        self.update_clock()
        self.start_stop.configure(text="Stop", command=self.stop)

    def stop(self):
        self.count = False
        self.start_stop.configure(text="Start", command=self.start)

    def reset(self):
        self.base_m_seconds = 0
        self.timer.configure(text="00:00:00")
        self.stop()

    def time_work(self):
        if self.count:
            m_seconds = self.base_m_seconds + 1
        else:
            m_seconds = self.base_m_seconds
        self.base_m_seconds = m_seconds
        seconds = m_seconds//10
        minutes = seconds // 60
        hours = minutes // 60
        minutes -= hours * 60
        seconds -= (minutes * 60) + (hours * 60 * 60)
        m_seconds -= (seconds * 10) + (minutes * 600) + (hours * 60 * 600)
        return "{}:{}:{}".format(str(hours).zfill(2), str(minutes).zfill(2),
                                    str(seconds).zfill(2))
app=App()