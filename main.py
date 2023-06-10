# import sys
# from PIL import Image,ImageTk

from tkinter import *
from PIL import Image, ImageTk

#-----------------------------------------------------
# CONFIGURATION
#-----------------------------------------------------
tk_width  = 500
tk_height = 600

canvas_width  = 450
canvas_height = 350
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
  columnspan = 4
)


#-----------------------------------------------------
# CANVAS IMAGE
#-----------------------------------------------------

def set_img( path = None ) :
  open_image   = Image.open(path)
  resize_img   = open_image.resize(canvas_img_size)
  result_image = ImageTk.PhotoImage(resize_img)
  return result_image
  
beginning_img = set_img("files/img/background1.png")
canvas_img = canvas.create_image(canvas_img_pos, image=beginning_img)

#-----------------------------------------------------
# BUTTON UPLOAD
#-----------------------------------------------------

def upload_img() :
  img_path = "files/img/background2.png"
  img = PhotoImage(file=img_path)
  print(img)
  canvas.itemconfig(canvas_img, image=img)
  print('Upload Image')

logo_btn_upload = Image.open("files/img/btn_upload_img.png")
logo_btn_upload_img = logo_btn_upload.resize(btn_size)
btn_upload_img = ImageTk.PhotoImage(logo_btn_upload_img)
btn_upload = Button(
  image = btn_upload_img, 
  highlightthickness = 0, 
  command = upload_img
)

btn_upload.grid(pady = padding_btn_y, row=1, column=0)

#-----------------------------------------------------
# BUTTON DOWNLOAD
#-----------------------------------------------------

def download_img() :
  img_path = "files/img/background3.png"
  img = PhotoImage(file=img_path)
  # img = set_img(img_path)
  print(img)
  canvas.itemconfig(canvas_img, image=img)
  print('Download Image')
  
logo_btn_download = Image.open("files/img/btn_download_img.png")
logo_btn_download_img = logo_btn_download.resize(btn_size)
btn_download_img = ImageTk.PhotoImage(logo_btn_download_img)
btn_donwload = Button(
  image = btn_download_img,
  highlightthickness = 0, 
  command = download_img
)

btn_donwload.grid(pady = padding_btn_y, row=1, column=1)

#-----------------------------------------------------
# BUTTON ADD TEXT
#-----------------------------------------------------

def add_text() :
  print('Add Text')
  
logo_btn_add_text = Image.open("files/img/btn_add_text_img.png")
logo_btn_add_text_img = logo_btn_add_text.resize(btn_size)
btn_add_text_img = ImageTk.PhotoImage(logo_btn_add_text_img)
btn_add_text = Button(
  image = btn_add_text_img,
  highlightthickness = 0, 
  command = add_text
)

btn_add_text.grid(pady = padding_btn_y, row=1, column=2)

#-----------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------

tk.mainloop()