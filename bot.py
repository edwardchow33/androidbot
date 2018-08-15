# coding=utf-8

from guibot.guibot_simple import *
import pyautogui
import pyperclip
from Tkinter import Tk
import time
class Bot:
    def __init__(self):
        initialize()
        add_path('images')
        self.NEXT = 'next.png'
        self.ADD ='add.png'
        self.CLOSE = 'close.png'
        self.CAPTION = 'caption.png'
        self.BACK = 'back.png'
        self.GALLERY = 'gallery.png'
        self.DISCARD = 'discard.png'

    def iclick(self,target):
        match = find(target)
        buttonx = match.target.x
        buttony = match.target.y
        pyautogui.click(buttonx,buttony)

    def back_to_home(self):
        if exists(self.CLOSE):
            self.iclick(self.CLOSE)
            wait(self.ADD,5)
        elif exists(self.BACK):
            while exists(self.BACK):
                if exists(self.DISCARD):
                    self.iclick(self.DISCARD)
                    break
                try:
                    self.iclick(self.BACK)
                    time.sleep(1)
                except:
                    print "test"
            wait(self.CLOSE, 1)
            self.iclick(self.CLOSE)
            wait(self.ADD, 5)

    def create_post(self):
        self.back_to_home()
        self.iclick(self.ADD)
        wait(self.CLOSE,5)
        self.iclick(self.GALLERY)

    def choose_media(self,target):
        self.iclick(target)
        self.iclick(self.NEXT)
        self.iclick(self.NEXT)

    def copy2clip(self,caption):
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(caption)
        r.update()  # now it stays on the clipboard after the window is closed
        r.destroy()

    def type_caption(self,caption):
        self.iclick(self.CAPTION)
        self.copy2clip(caption)
        pyautogui.hotkey('ctrl', 'v')

bot = Bot()
bot.create_post()
bot.choose_media('test.png')
bot.type_caption("#一大班 #朋友 #總有人係")

