import tkinter as tk

class SmartCanvas(tk.Canvas):
    def create_entity(self):
        entity = Entity('Employee', self)
        print(entity.id)


class Entity:
    def __init__(self, name, canvas, x=None, y=None):
        self.name = name
        self.canvas = canvas
        self.is_selected = False
        if x == None:
            self.x = canvas.winfo_reqwidth()+125
        else:
            self.x = x

        if y == None:
            self.y = 55
        else:
            self.y = y

        self.id = canvas.create_rectangle(canvas.winfo_reqwidth(), 10, canvas.winfo_reqwidth()+250, 100, fill='gray80', outline='gray2', activeoutline='blue4', activewidth=2)
        self.text_object = canvas.create_text(canvas.winfo_reqwidth()+125, 55, text=self.name, width=(canvas.winfo_reqwidth()+250)-(canvas.winfo_reqwidth()))

        canvas.bind('<B1-Motion>', self.select)

    def select(self, event):
        print(event)
        self.is_selected = True

    def move_left(self):
        self.canvas.move(self.id, -1, 0)

    def move_right(self):
        self.canvas.move(self.id, 1, 0)

    def move_up(self):
        self.canvas.move(self.id, 0, 1)

    def move_down(self):
        self.canvas.move(self.id, 0, -1)
