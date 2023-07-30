from tkinter import *
import tkinter.ttk as ttk

class Window:
    def __init__(self, master):
        notebook = ttk.Notebook(master, height=100)
        notebook.place(x=0, y=0)
        file = ttk.Frame(notebook)
        insert = ttk.Frame(notebook)

        notebook.add(file, text='File')
        notebook.add(insert, text='Insert')
        notebook.pack(side=TOP, fill=X)

        file_pane = ttk.PanedWindow(file, orient=HORIZONTAL)
        file_pane.pack()

        new = ttk.LabelFrame(file_pane, text='New', width=100, height=100)
        open = ttk.LabelFrame(file_pane, text='Open', width=100, height=100)
        save = ttk.LabelFrame(file_pane, text='Save', width=100, height=100)
        export = ttk.LabelFrame(file_pane, text='Export', width=100, height=100)
        file_pane.add(new)
        file_pane.add(open)
        file_pane.add(save)
        file_pane.add(export)

        insert_pane = ttk.Panedwindow(insert, orient=HORIZONTAL)
        insert_pane.pack()

        shapes = ttk.Labelframe(insert_pane, text='Shapes', width=100, height=100)
        connectors = ttk.Labelframe(insert_pane, text='Connectors', width=100, height=100)
        font = ttk.Labelframe(insert_pane, text='Font', width=100, height=100)
        tools = ttk.Labelframe(insert_pane, text='Tools', width=100, height=100)
        insert_pane.add(shapes)
        insert_pane.add(connectors)
        insert_pane.add(font)
        insert_pane.add(tools)

        canvas = Canvas(master)
        canvas.pack(side=TOP, fill=BOTH, expand=TRUE)


root = Tk()
root.geometry('1600x700')
root.title('Django Direct')
window = Window(root)
root.mainloop()