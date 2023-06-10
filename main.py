# import sys
# from PIL import Image,ImageTk

from tkinter import *
from PIL import Image, ImageTk

#-----------------------------------------------------
# CONFIGURATION
#-----------------------------------------------------
tk_width  = 500
tk_height = 600

canvas_width  = 470
canvas_height = 370
canvas_img_size = (canvas_width,canvas_height)
canvas_img_pos  = (canvas_width/2,canvas_height/2)
canvas_pad_x  = 50
canvas_pad_y  = 50

button_width  = 50
button_height = 50
padding_btn_y = 20
btn_size  = (button_width, button_height)

tk = Tk()
tk.title("Watermark Desktop App")
tk.minsize(width = tk_width,height = tk_height)
tk.config( padx = 20, pady = 20,bg = "#36486b")

canvas = Canvas(master = tk, width = canvas_width, height = canvas_height)
canvas.config(bg = "#fefbd8", highlightthickness = 0)
canvas.grid( 
  padx   = canvas_pad_x, 
  pady   = canvas_pad_y, 
  row    = 0, 
  column = 0,
  columnspan = 5
)

#-----------------------------------------------------
# IMAGES & IMAGE CONTAINER
#-----------------------------------------------------
bg1_img = ImageTk.PhotoImage(Image.open("files/img/background1.png").resize(canvas_img_size))
bg2_img = ImageTk.PhotoImage(Image.open("files/img/background2.png").resize(canvas_img_size))
bg3_img = ImageTk.PhotoImage(Image.open("files/img/background3.png").resize(canvas_img_size))

btn_upload_img   = ImageTk.PhotoImage(Image.open("files/img/btn_upload_img.png").resize(btn_size))
btn_download_img = ImageTk.PhotoImage(Image.open("files/img/btn_download_img.png").resize(btn_size))
btn_add_text_img = ImageTk.PhotoImage(Image.open("files/img/btn_add_text_img.png").resize(btn_size))
btn_add_icon_img = ImageTk.PhotoImage(Image.open("files/img/btn_add_icon_img.png").resize(btn_size))
btn_reset_img    = ImageTk.PhotoImage(Image.open("files/img/btn_reset_img.png").resize(btn_size))

canvas_img_container = canvas.create_image( canvas_img_pos, image = bg1_img)

#-----------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------

def upload_img() :
  canvas.itemconfig(canvas_img_container, image = bg2_img)
  print('Upload Image')

def download_img() :
  canvas.itemconfig(canvas_img_container, image = bg3_img)
  print('Download Image')
  
def add_text() :
  print('Add Text')

def add_icon() :
  print('Add Icon')
  
def reset_img() :
  canvas.itemconfig(canvas_img_container, image = bg1_img)
  print('Reset Image')
  
#-----------------------------------------------------
# ELEMENTS
#-----------------------------------------------------

btn_upload   = Button( image = btn_upload_img, highlightthickness = 0, command = upload_img)
btn_donwload = Button( image = btn_download_img, highlightthickness = 0, command = download_img )
btn_add_text = Button( image = btn_add_text_img, highlightthickness = 0, command = add_text )
btn_add_icon = Button( image = btn_add_icon_img, highlightthickness = 0, command = add_icon )
btn_reset    = Button( image = btn_reset_img, highlightthickness = 0, command = reset_img )

#-----------------------------------------------------
# GRIDS (COLUMNS AND ROWS)
#-----------------------------------------------------

btn_upload.grid(pady = padding_btn_y, row=1, column=0)
btn_donwload.grid(pady = padding_btn_y, row=1, column=1)
btn_add_text.grid(pady = padding_btn_y, row=1, column=2)
btn_add_icon.grid(pady = padding_btn_y, row=1, column=3)
btn_reset.grid(pady = padding_btn_y, row=1, column=4)

#-----------------------------------------------------
# OTHER
#-----------------------------------------------------

tk.mainloop()