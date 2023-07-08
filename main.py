import flet as ft
from flet import *

from Header import Header
from Body import Body
from Footer import Footer
from Page import page as mhmp

def main(page: ft.Page):
    
    objp = mhmp(page)
    objp.setup()
    objp.update()

    objh = Header(objp.getpage())
    objf = Footer(objp.getpage())
    objB = Body(objp.getpage(),objf.getfooter())

    filepicker = objB.getfilepicker()
    
    ##### Header & Footer #####
    objp.getpage().add(
        ft.Column(
        controls=[
                ft.Row(objh.draw(),),
                ft.Row(objB.draw()),
                ft.Row(objf.draw(),),
                filepicker,
            ],),
        )

ft.app(target=main)