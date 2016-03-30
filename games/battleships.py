import tkinter as tk
import time


class Row():
    rows1 = {}
    rows2 = {}

    def __init__(self, row, player):
        self.row_num = row
        self.player = player
        self.shipnum = 0
        self.sunk = 0
        self.row_buttons = {}
        self.n = False

        for i in range(1, 6):
            self.row_buttons[i] = tk.Button(text="O", command=lambda x=i: self.select(x), bg="black", fg="green2",
                                            borderwidth=0, width=3, height=1)

        if self.player == 1:
            Row.rows1[self.row_num] = self
        else:
            Row.rows2[self.row_num] = self

    def draw(self):
        for i in self.row_buttons:
            self.row_buttons[i].grid(column=i, row=self.row_num)

    def undraw(self):
        for i in self.row_buttons:
            self.row_buttons[i].grid_forget()

    def press(self, but_num):
        for i in self.row_buttons:
            if i == but_num and self.row_buttons[i].cget("text") == "O":
                if self.player == 1:
                    if "".join([str(i), str(self.row_num)]) in Player.ship_pos2:
                        self.row_buttons[i].configure(text="X")
                        self.sunk += 1
                    else:
                        self.row_buttons[i].configure(text="M")
                else:
                    if "".join([str(i), str(self.row_num)]) in Player.ship_pos1:
                        self.row_buttons[i].configure(text="X")
                        self.sunk += 1
                    else:
                        self.row_buttons[i].configure(text="M")
                self.n = True

    def select(self, but_num):
        for i in self.row_buttons:
            if i == but_num and self.row_buttons[i].cget("text") == "O":
                self.row_buttons[i].configure(text="S")
                if self.player == 1:
                    Player.ship_pos1.append("{}{}".format(i, self.row_num))
                else:
                    Player.ship_pos2.append("{}{}".format(i, self.row_num))
                self.shipnum += 1


class Player():
    ship_pos1 = []
    ship_pos2 = []

    def __init__(self, player):
        self.game_state = "selecting"
        self.next = False
        self.player = player
        self.use_row = {}
        self.ship_pos = []

        self.main_lab = tk.Label(text="Player {}, select your ship positions (5)".format(self.player), bg="black",
                                 fg="green2")

        self.r1 = Row(1, player)
        self.r2 = Row(2, player)
        self.r3 = Row(3, player)
        self.r4 = Row(4, player)
        self.r5 = Row(5, player)

    def update_rows(self):
        print(self.ship_pos)
        if self.player == 1:
            self.use_row = Row.rows1
            self.ship_pos = Player.ship_pos1
        else:
            self.use_row = Row.rows2
            self.ship_pos = Player.ship_pos2
        if self.game_state == "selecting":
            tot = 0
            for i in self.use_row:
                tot += self.use_row[i].shipnum
            self.main_lab.configure(text="Player {}, select your ship positions ({})".format(self.player, 5 - tot))
            if tot == 5:
                self.game_state = "playing"
                for row in self.use_row:
                    for button in self.use_row[row].row_buttons:
                        self.use_row[row].row_buttons[button].configure(
                            command=lambda x=button, r=row: self.use_row[r].press(x), text="O")
                self.next = True

        elif self.game_state == "playing":
            sunk = 0
            for i in self.use_row:
                sunk += self.use_row[i].sunk
            self.main_lab.configure(text="Player {}'s turn to pick ({} ships remaining)".format(self.player, 5 - sunk))
            for r in self.use_row:
                if self.use_row[r].n:
                    self.next = True
                    self.use_row[r].n = False
                    break

    def draw(self):
        self.main_lab.grid(column=1, row=0, columnspan=5, sticky="N")
        for r in self.use_row:
            self.use_row[r].draw()


    def undraw(self):
        self.main_lab.grid_forget()
        for r in self.use_row:
            self.use_row[r].undraw()


class App():
    def __init__(self):
        self.root = tk.Tk()

        self.player1 = Player(1)
        self.player2 = Player(2)

        self.current_player = self.player1

        self.current_player.update_rows()
        self.current_player.draw()

        self.root.title("Battleships")
        self.root.configure(bg="black")
        self.update_game()
        self.root.mainloop()

    def update_game(self):
        self.current_player.update_rows()
        if self.current_player.next:
            self.current_player.next = False
            time.sleep(1)
            self.current_player.undraw()
            if self.current_player.player == 1:
                self.current_player = self.player2
            else:
                self.current_player = self.player1
            self.current_player.update_rows()
            self.current_player.draw()
        self.root.after(200, self.update_game)


app = App()