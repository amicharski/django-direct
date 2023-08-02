from tkinter import *
import tkinter.ttk as ttk
from tools import Tool
from canvas import SmartCanvas


class Window:

    def __init__(self, master):
        tool = Tool(master)

        notebook = ttk.Notebook(master, height=100)
        notebook.place(x=0, y=0)
        file_tab = ttk.Frame(notebook)
        insert_tab = ttk.Frame(notebook)

        notebook.add(file_tab, text='File')
        notebook.add(insert_tab, text='Insert')
        notebook.pack(side=TOP, fill=X)

        canvas = SmartCanvas(master)
        canvas.pack(side=TOP, fill=BOTH, expand=TRUE)

        file_pane = ttk.PanedWindow(file_tab, orient=HORIZONTAL)
        file_pane.pack()

        #### New
        new_frame = ttk.LabelFrame(file_pane, text='New', width=100, height=100)

        new_er_diagram_button = ttk.Button(new_frame, text='New ER Diagram')
        new_er_diagram_button.pack()

        new_eer_diagram_button = ttk.Button(new_frame, text='New EER Diagram')
        new_eer_diagram_button.pack()

        #### Open
        open_frame = ttk.LabelFrame(file_pane, text='Open', width=100, height=100)

        open_file_button = ttk.Button(open_frame, text='Open File')
        open_file_button.pack()

        #### Save
        save_frame = ttk.LabelFrame(file_pane, text='Save', width=100, height=100)

        save_button = ttk.Button(save_frame, text='Save')
        save_button.pack()

        save_as_button = ttk.Button(save_frame, text='Save As')
        save_as_button.pack()

        #### Export
        export_frame = ttk.LabelFrame(file_pane, text='Export', width=100, height=100)

        export_to_django_button = ttk.Button(export_frame, text='Export to Django models.py')
        export_to_django_button.pack()

        export_to_pdf_button = ttk.Button(export_frame, text='Export to PDF')
        export_to_pdf_button.pack()

        export_to_vsdx_button = ttk.Button(export_frame, text='Export to Visio')
        export_to_vsdx_button.pack()

        file_pane.add(new_frame)
        file_pane.add(open_frame)
        file_pane.add(save_frame)
        file_pane.add(export_frame)

        insert_pane = ttk.Panedwindow(insert_tab, orient=HORIZONTAL)
        insert_pane.pack()

        #### Shapes
        shapes_frame = ttk.Labelframe(insert_pane, text='Shapes', width=100, height=100)

        entity_button = ttk.Button(shapes_frame, text='Entity', command=canvas.create_entity)
        entity_button.pack()

        attribute_button = ttk.Button(shapes_frame, text='Attribute')
        attribute_button.pack()

        #### Connectors
        connectors_frame = ttk.Labelframe(insert_pane, text='Connectors', width=100, height=100)

        relationship_button = ttk.Button(connectors_frame, text='Relationship')
        relationship_button.pack()

        #### Font Adjustments
        font_frame = ttk.Labelframe(insert_pane, text='Font', width=100, height=100)

        font_family_combobox = ttk.Combobox(font_frame, values=('Arial', 'Comic Sans', 'Sans', 'Sans-serif', 'Times New Roman'))
        font_family_combobox.set('Arial')
        font_family_combobox.pack()

        font_size_combobox = ttk.Combobox(font_frame, values=(8, 10, 11, 12, 14, 16, 18, 20))
        font_size_combobox.set(12)
        font_size_combobox.pack()

        #### Tools
        tools_frame = ttk.Labelframe(insert_pane, text='Tools', width=100, height=100)

        pan_button = ttk.Button(tools_frame, text='Pan', command=tool.set_pan)
        pan_button.pack()

        select_button = ttk.Button(tools_frame, text='Select', command=tool.set_select)
        select_button.pack()

        insert_pane.add(shapes_frame)
        insert_pane.add(connectors_frame)
        insert_pane.add(font_frame)
        insert_pane.add(tools_frame)


root = Tk()
root.geometry('1600x700')
root.title('Django Direct')
window = Window(root)
root.mainloop()