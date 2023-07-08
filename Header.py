
import flet as ft
from flet import *
import keyboard

class Header:

    def __init__(self,page):
        self.page = page
        self.heigth = 50
        self.width = page.window_width - 30
        self.padding = 5

    def minimize_clicked(self,e):
        self.page.window_minimized = True
        self.page.update()
    
    def full_screen_changed(self,e):

        if(self.page.window_full_screen == True):
            self.page.window_full_screen = False
        else:
            self.page.window_full_screen = True

        self.page.update()

    def close_window(self,e):
        keyboard.press_and_release('alt+f4')
        self.page.update()

    def controls(self):
        return  [ 
                ft.IconButton(icon=ft.icons.MINIMIZE_ROUNDED,   on_click=self.minimize_clicked,     icon_color=ft.colors.WHITE,),
                ft.IconButton(icon=ft.icons.SQUARE_ROUNDED,     on_click=self.full_screen_changed,  icon_color=ft.colors.WHITE,),
                ft.IconButton(icon=ft.icons.CLOSE_ROUNDED,      on_click=self.close_window,         icon_color=ft.colors.WHITE,)  
                ]                

    def draw(self):

        return [
            ft.Container(
                #bgcolor=ft.colors.YELLOW,
                bgcolor=None,
                padding=self.padding,
                width=self.width*(26/30),
                height=self.heigth,
                border_radius=10,
            ),
            ft.Container(
                #bgcolor=ft.colors.YELLOW_900,
                bgcolor=None,
                padding=self.padding,
                width=self.width*(4/30),
                content=ft.Row(self.controls(),alignment=ft.MainAxisAlignment.END),
                height=self.heigth,
                border_radius=10,
            ),
        ]

