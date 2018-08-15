# -*- coding: utf8 -*-
from Tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append('两两相忘')
r.update() # now it stays on the clipboard after the window is closed
r.destroy()
