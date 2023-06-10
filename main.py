# import sys
# from PIL import Image,ImageTk

from tkinter import *

tk = Tk()
tk.title("Watermark Desktop App")
tk.geometry("500x600")
# tk.minsize(width=500,height=600)
tk.config(bg="#fefbd8")

canvas = Canvas(width=450, height=350)
canvas.config(bg="#B1DDC6", highlightthickness=0)
canvas.grid(row=0, column=0)
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

bg_pos = (0, 0)
bg_front = PhotoImage(file="files/img/background.png")
background = canvas.create_image(bg_pos, image=bg_front)
canvas.itemconfig(background, image=bg_front)


tk.mainloop()