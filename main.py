# import sys
# from PIL import Image,ImageTk

from tkinter import *
from PIL import Image, ImageTk

#------------------------------------------------------------------
# CONFIGURATION
#------------------------------------------------------------------
tk_width  = 500
tk_height = 600

canvas_width  = 450
canvas_height = 350
canvas_img_size = (canvas_width,canvas_height)
canvas_img_pos  = (canvas_width/2,canvas_height/2)

button_width  = 50
button_height = 50
btn_size  = (button_width, button_height)

tk = Tk()
tk.title("Watermark Desktop App")
tk.minsize(width = tk_width,height = tk_height)
tk.config(bg = "#fefbd8")

canvas = Canvas(width = canvas_width, height = canvas_height)
canvas.config(bg = "#B1DDC6", highlightthickness = 0)
canvas.grid( row = 0, column = 0, columnspan = 4 )

#------------------------------------------------------------------
# IMAGE
#------------------------------------------------------------------

canvas_image = Image.open("files/img/background.png")

image = canvas_image.resize(canvas_img_size)
photo_img = ImageTk.PhotoImage(image)

canvas_img = canvas.create_image(
  canvas_img_pos, image = photo_img, anchor = CENTER
)
canvas.itemconfig(canvas_img, image=photo_img)

#------------------------------------------------------------------
# BUTTON UPLOAD
#------------------------------------------------------------------

def upload_img() :
  print('Upload Image')
  
logo_btn_upload = Image.open("files/img/btn_upload_img.png")
logo_btn_upload_img = logo_btn_upload.resize(btn_size)
btn_upload_img = ImageTk.PhotoImage(logo_btn_upload_img)
btn_upload = Button(
  image = btn_upload_img, 
  highlightthickness = 0, 
  command = upload_img
)

btn_upload.grid(row=1, column=0)

#------------------------------------------------------------------
# BUTTON DOWNLOAD
#------------------------------------------------------------------

def download_img() :
  print('Download Image')
  
logo_btn_download = Image.open("files/img/btn_download_img.png")
logo_btn_download_img = logo_btn_download.resize(btn_size)
btn_download_img = ImageTk.PhotoImage(logo_btn_download_img)
btn_donwload = Button(
  image = btn_download_img,
  highlightthickness = 0, 
  command = download_img
)

btn_donwload.grid(row=1, column=1)

#------------------------------------------------------------------
# BUTTON ADD TEXT
#------------------------------------------------------------------

def add_text() :
  print('Add Text')
  
logo_btn_add_text = Image.open("files/img/btn_add_text_img.png")
logo_btn_add_text_img = logo_btn_add_text.resize(btn_size)
btn_add_text_img = ImageTk.PhotoImage(logo_btn_add_text_img)
btn_donwload = Button(
  image = btn_add_text_img,
  highlightthickness = 0, 
  command = add_text
)

btn_donwload.grid(row=1, column=2)

#------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------

tk.mainloop()