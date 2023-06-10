# import sys
# from PIL import Image,ImageTk

from tkinter import *
from PIL import Image, ImageTk

#-------------------------------------------------------------------------------
# CONFIGURATION
#-------------------------------------------------------------------------------
tk = Tk()
tk.title("Watermark Desktop App")
tk.minsize(width=500,height=600)
tk.config(bg="#fefbd8")

canvas_height = 350
canvas_width  = 450

canvas = Canvas(width=canvas_width, height=canvas_height)
canvas.config(bg="#B1DDC6", highlightthickness=0)
canvas.grid(row=0, column=0)
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

#-------------------------------------------------------------------------------
# IMAGE MODIFICATION
#-------------------------------------------------------------------------------

image = Image.open("files/img/background.png")

img_size = (canvas_width,canvas_height)
img_pos = (canvas_width/2,canvas_height/2)

image = image.resize(img_size)
photo_img = ImageTk.PhotoImage(image)

upload_img = canvas.create_image(img_pos, image=photo_img, anchor=CENTER)
canvas.itemconfig(upload_img, image=photo_img)

tk.mainloop()