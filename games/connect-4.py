import tkinter as tk

# Button class to allow button specific variables
class MyButton(tk.Button):
	def __init__(self, **kwargs):
		super(MyButton, self).__init__(bg='azure', **kwargs)
		# 'r' = red, 'y' = yellow
		self.colour = ''
# Row class for use instead of many separate blocks
class Row():
	rows = dict()
	def __init__(self, width, rownum):
		self.buttons = dict()
		
		self.rownum = rownum
		
		
		for i in range(1, width+1):
			self.buttons[i] = MyButton(text="", width=2, command=lambda x=i: self.click(x))
			self.buttons[i].grid(column=i, row=rownum)
			
		Row.rows[rownum] = self
	
	def click(self, butnum):
		if App.state == 'p':
			if App.turn == 'r':
				self.buttons[butnum].configure(bg='red')
				self.buttons[butnum].colour = 'r'
				App.turn = 'y'
				App.state = 'f'
				
			elif App.turn == 'y':
				self.buttons[butnum].configure(bg='yellow')
				self.buttons[butnum].colour = 'y'
				App.turn = 'r'
				App.state = 'f'				
		
				
# Self contained app class for ease of variables
class App():
	turn = 'r'
	state = 'p'
	# Initialise window
	def __init__(self, size=7):
		self.root = tk.Tk()
		self.root.title("Connect420")
		
		self.colours = {
					'r':'red',
					'y':'yellow'
					}
		
		for r in range(1, size):
			Row(size, r)
		
		
		self.playing = ''
		self.main_update()
		
		self.root.mainloop()
		
	def main_update(self):
		fell = False
		if App.state == 'f':
			for r in Row.rows:
				for b in Row.rows[r].buttons:
					if Row.rows[r].buttons[b].colour != '':
						# Check below
						if Row.rows[r].rownum + 1 < 7:
							if Row.rows[r+1].buttons[b].colour == '':
								Row.rows[r+1].buttons[b].configure(bg=self.colours[Row.rows[r].buttons[b].colour])
								Row.rows[r+1].buttons[b].colour = Row.rows[r].buttons[b].colour
								
								Row.rows[r].buttons[b].configure(bg='azure')
								Row.rows[r].buttons[b].colour = ''
								
								fell = True
		if not fell:
			App.state = 'p'
			self.enable()
			for r in Row.rows.values():
				for b in r.buttons.values():
					if b.colour != '':
						b.configure(state='disabled')
		self.check()
		if self.playing == '':
			self.root.after(200, self.main_update)
		else:
			self.tmp = tk.Tk()
			self.tmp.title("Winner!")
			tk.Label(self.tmp, text="{} has won!".format(self.colours[self.playing])).pack()
			tk.Button(self.tmp, text="Exit", command=self.destroy).pack()
			

	def destroy(self):
		self.tmp.destroy()
		self.root.destroy()
	
	def disable(self):
		for r in Row.rows.values():
			for b in r.buttons.values():
				b.configure(state='disabled')
				
	def enable(self):
		for r in Row.rows.values():
			for b in r.buttons.values():
				b.configure(state='normal')
				
	def check(self):
		# Horizontal
		for r in Row.rows:
			for b in Row.rows[r].buttons:
				if Row.rows[r].buttons[b].colour != '':
					# Left
					if b-3 > 0:
						if Row.rows[r].buttons[b].colour == Row.rows[r].buttons[b-1].colour and Row.rows[r].buttons[b].colour == Row.rows[r].buttons[b-2].colour and Row.rows[r].buttons[b].colour == Row.rows[r].buttons[b-3].colour:
							self.playing = Row.rows[r].buttons[b].colour
							self.disable()
					# Up
					if r-3 > 0:
						if Row.rows[r].buttons[b].colour == Row.rows[r-1].buttons[b].colour and Row.rows[r].buttons[b].colour == Row.rows[r-2].buttons[b].colour and Row.rows[r].buttons[b].colour == Row.rows[r-3].buttons[b].colour:
							self.playing = Row.rows[r].buttons[b].colour
							self.disable()
							
					# Diagonal up-left
					if b-3 > 0 and r-3 > 0:
						if Row.rows[r].buttons[b].colour == Row.rows[r-1].buttons[b-1].colour and Row.rows[r].buttons[b].colour == Row.rows[r-2].buttons[b-2].colour and Row.rows[r].buttons[b].colour == Row.rows[r-3].buttons[b-3].colour:
							self.playing = Row.rows[r].buttons[b].colour
							self.disable()
					
					# Diagonal up-right
					if b+3 < 7 and r-3 > 0:
						if Row.rows[r].buttons[b].colour == Row.rows[r-1].buttons[b+1].colour and Row.rows[r].buttons[b].colour == Row.rows[r-2].buttons[b+2].colour and Row.rows[r].buttons[b].colour == Row.rows[r-3].buttons[b+3].colour:
							self.playing = Row.rows[r].buttons[b].colour
							self.disable()
app = App()