import tkinter as tk

from world import World
from simulation import Simulation


class Gui(tk.Tk):
    def __init__(self):
        super(Gui, self).__init__()
        self.width = 800
        self.height = 600
        self.title('Life Game')
        self.geometry(f'{self.width}x{self.height}')
        self.resizable(width=0, height=0)

        self.cells = []
        self.cell_color = ['black', 'green']
        self.worldsize = tk.IntVar(value=5)
        self.world = World(self.worldsize.get())


        self.create_widgets()

    def create_widgets(self):
        self.cellwidth = 50
        self.canvas = tk.Canvas(self, width=500, height=500)
        for i in range(5):
            for j in range(5):
                rect = self.canvas.create_rectangle((self.cellwidth*i, self.cellwidth*j, self.cellwidth*(i+1), self.cellwidth*(j+1)),
                                                fill=self.cell_color[0],
                                                tags=[f'{i}-{j}'])
                self.cells.append(rect)
                self.canvas.tag_bind(rect, '<Button-1>', self.cell_clicked(self.canvas, i, j, rect))
        self.canvas.pack()

        self.btns_frame = tk.Frame(self)
        self.btns_frame.pack()
        self.start_btn = tk.Button(self.btns_frame, text='Start', command=self.start_btn_clicked)
        self.start_btn.pack(side=tk.LEFT)
        self.clear_btn = tk.Button(self.btns_frame, text='Clear', command=self.clear_btn_clicked)
        self.clear_btn.pack(side=tk.LEFT)

    def canvas_update(self):
        for c in self.cells:
            i, j = map(int, self.canvas.itemcget(c, 'tags').split('-'))
            cn = self.world(i, j)
            self.canvas.itemconfig(c, fill=self.cell_color[cn])

    def start_btn_clicked(self):
        pass

    def clear_btn_clicked(self):
        self.world.clear()
        self.canvas_update()
    
    def cell_clicked(self, canvas, i, j, rect):
        def inner(e):
            self.world.inversion(i, j)
            canvas.itemconfig(rect, fill=self.cell_color[self.world(i, j)])
            
        return inner

    def run(self):
        self.mainloop()
    

gui = Gui()
gui.run()