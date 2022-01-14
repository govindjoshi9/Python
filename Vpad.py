import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry("1200x800")
main_application.title("Vpad text editer")

##################### MAIN MANUE ####################
main_manu = tk.Menu()
# new_icon = tk.PhotoImage(file='C:\Users\sundaram infotech\Downloads\icons2\new.png')

file = tk.Menu(main_manu, tearoff=False)
edit = tk.Menu(main_manu, tearoff=False)
view = tk.Menu(main_manu, tearoff=False)
color_them = tk.Menu(main_manu, tearoff=False)

#cascade
main_manu.add_cascade(label='File',menu= file)
main_manu.add_cascade(label='Edit',menu= edit)
main_manu.add_cascade(label='View',menu= view)
main_manu.add_cascade(label='Theme',menu= color_them)





main_application.config(menu=main_manu)
main_application.mainloop()