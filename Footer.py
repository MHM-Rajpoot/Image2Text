
import flet as ft
from flet import *

class Footer:

    def __init__(self,page):
        self.page = page
        self.heigth = 50
        self.width = page.window_width - 19 
        self.padding = 5

    def getfooter(self):
        return self

    def updates(self,e,update:str,condition:bool):

        if(condition):
            self.footer.content.value = update
            self.footer.bgcolor = ft.colors.GREEN
        else:
            self.footer.content.value = update
            self.footer.bgcolor = ft.colors.RED
        
        self.page.update()

    def draw(self):
        self.footer = ft.Container(
                content = ft.Text(value="Empty",color=ft.colors.WHITE,size=self.heigth/2),
                #bgcolor=ft.colors.BLUE,
                bgcolor=None,
                padding=5,
                width=self.width,
                height=self.heigth,
                border_radius=10,
            )
        return [self.footer,]

