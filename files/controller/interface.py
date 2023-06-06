from tkinter import*

class Interface :
  def __init__(self) :
    self.tk = Tk()
    self.tk.title("Watermark Desktop App")
    self.tk.minsize(width=350,height=550)
    self.tk.config(bg="#deeaee")
    self.update_attr()

  def update_attr(self) :
    pass

  def action_attr(self) :
    pass