
import flet as ft
from flet import *

class page(ft.Page):
    
    def __init__(self,page):
        self.page = page
        self.uncertainityheight = 175
        self.uncertainitywidht = 23

    def setup(self):
        self.page.window_frameless = True
        self.page.bgcolor =  ft.colors.BLACK

    def update(self):
        self.page.update()

    def getuncertainitywidht(self):
        return self.uncertainitywidht

    def getuncertainityheight(self):
        return self.uncertainityheight
    
    def getpage(self)->ft.Page:
        return self.page
    
    def getcolor(self)->ft.colors:
        return self.page.bgcolor
    
    def setcolor(self,color)->None:
        self.page.bgcolor = color 
    


    