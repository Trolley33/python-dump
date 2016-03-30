import tkinter as tk
import hashlib


class App():
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Hash-er")

        self.pass_label = tk.Label(text="Password:")
        self.salt_label = tk.Label(text="Salt:")

        self.pass_entry = tk.Entry(width=20)
        self.salt_entry = tk.Entry(width=20)

        self.submit = tk.Button(text="Hash", command=self.hash)

        self.hash_output = tk.Text()

        # ---- #

        self.pass_label.grid(column=3, row=0, sticky="e")
        self.salt_label.grid(column=3, row=1, sticky="e")

        self.pass_entry.grid(column=4, row=0)
        self.salt_entry.grid(column=4, row=1)

        self.submit.grid(column=4, row=2)

        self.hash_output.grid(column=0, row=3, columnspan=10)

        self.root.mainloop()

    def hash(self):
        self.hash_output.delete(1.0, "end")
        pazz = self.pass_entry.get()
        salt = self.salt_entry.get()

        string = "{}{}".format(pazz, salt)

        h = hashlib.sha256(string.encode('utf-8')).hexdigest()

        self.hash_output.insert(1.0, h)

app = App()