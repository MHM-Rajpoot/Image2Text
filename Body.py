
import flet as ft
import os
import base64

import cv2
from io import BytesIO
from PIL import Image
from pytesseract import pytesseract

class Body:

    def __init__(self,page,footer):
        self.page = page
        self.footer = footer
        self.heigth = page.window_height - 175
        self.width = page.window_width
        self.padding = 5

        self.file_picker = ft.FilePicker(on_result=self.pick_files_result)

        self.selectedfile = str()
        self.uploadpath = './uploads/inp.jpg'
        self.dummyimg = './uploads/dummy.jpg'
        self.outputtext = './output/output.txt'

    def getfilepicker(self):
        return self.file_picker

    def fileextensioncheck(self,filename:str):
        fileextension = ['png','PNG','jpg','jpeg',]

        for i in fileextension:
            if(filename.endswith(i)):
                return True
        
        return False

    def upscale_image(self,image_path, scale_factor):

        # Load the low-resolution image
        image = cv2.imread(image_path)

        # Calculate the new dimensions for upscaling
        width = int(image.shape[1] * scale_factor)
        height = int(image.shape[0] * scale_factor)

        # Upscale the image using bicubic interpolation
        upscaled_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_CUBIC)

        cv2.imwrite(self.uploadpath, upscaled_image, [cv2.IMWRITE_JPEG_QUALITY, 90])

    def pick_files_result(self,e: ft.FilePickerResultEvent):
        
        self.showimage.content.src = self.dummyimg

        uf = []
        if self.file_picker.result != None and self.file_picker.result.files != None:
            for f in self.file_picker.result.files:
                if(self.fileextensioncheck(f.name)):
                    self.file_picker.upload(uf)
                    
                    self.selectedfile = f.path
                    
                    self.uploadbutton.disabled = False
                    self.footer.updates(e,str(f.path),1)

                else:
                    self.footer.updates(e,str('Wrong File'),0)
        else:
            self.footer.updates(e,str('No File'),0)

    def file_upload(self,e):
        
        ## Assignment ##
        self.upscale_image(self.selectedfile,1)

        try:
            
            pil_img = Image.open(self.uploadpath)

            buff = BytesIO()
            pil_img.save(buff, format="JPEG")

            new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")
            self.img.src_base64 = new_image_string
            self.img.update()

            """
            img = Image.open(filepath)
            img.save(self.uploadpath,format='JPEG')
            self.showimage.content.src = self.uploadpath
            self.showimage.update()
            """

            self.extract.disabled = False
            self.uploadbutton.disabled = True
            self.footer.updates(e,str('Upload SucessFull'),1)

        except:
            self.footer.updates(e,str('Upload UnSucessFull'),0)
       
    def extract_text(self,e):

        self.footer.updates(e,str('Processing'),0)

        path_to_tesseract = './tesseract/tesseract.exe'
        path_to_image = self.uploadpath

        # Tesseract
        pytesseract.tesseract_cmd = path_to_tesseract
        img = Image.open(path_to_image)
        text = pytesseract.image_to_string(img)

        lis = text.split("\n")

        with open(self.outputtext, 'w') as ftxt:
            ftxt.write(text)

        self.final_text.value =  "\n" * 2 + text
        self.page.update()

        self.footer.updates(e,str('Done  NOTE :: If NO Text in Next to Extact Button then NO Text Found'),1)
        
        #os.remove(self.uploadpath)

    def buttons(self):
        
        widthRow1 = (self.width - 50)*(1/4)
        widthRow2 = (self.width - 30)*(1/2) - 159

        heightROw1 = self.heigth * (1/4)
        heightROw2 = (self.heigth - 8)* (3/4) - 4
        
        self.uploadbutton = ft.ElevatedButton(
                        "Upload",
                        color = ft.colors.WHITE,
                        bgcolor=None,
                        width=widthRow1,
                        height=heightROw1,
                        icon=ft.icons.UPLOAD,
                        on_click=self.file_upload,
                        disabled=True,
                    )
        
        self.img = ft.Image(src = self.dummyimg,aspect_ratio=True)

        self.showimage = ft.Container(
                        content = self.img ,
                        #bgcolor=ft.colors.YELLOW,
                        bgcolor=None,
                        width=widthRow2,
                        height=heightROw2,
                        padding=5,
                        border_radius=10,
                    )
        
        self.extract = ft.ElevatedButton(
                        "Extract",
                        color = ft.colors.WHITE,
                        bgcolor=None,
                        width=widthRow1,
                        height=heightROw1,
                        icon=None,
                        on_click=self.extract_text,
                        disabled=True,
                    )
        
        self.final_text = ft.Text(
                    value="\n" * 5 + "Dummy Text",
                    size=25,
                    visible=True,
                    color=ft.colors.WHITE,
                    selectable=True,
                    text_align="center"
                    )

        return  [

                ft.Row([
                    ft.Container(
                        #bgcolor=ft.colors.YELLOW,
                        bgcolor=None,
                        width=widthRow1,
                        height=heightROw1,
                        padding=5,
                        border_radius=10,
                    ),
                    ft.ElevatedButton(
                        "Select Image",
                        color = ft.colors.WHITE,
                        bgcolor=None,
                        width=widthRow1,
                        height=heightROw1,
                        icon=ft.icons.FOLDER_OPEN,
                        on_click=lambda _: self.file_picker.pick_files(allow_multiple=False),
                    ),
                    self.uploadbutton,
                    ft.Container(
                        #bgcolor=ft.colors.YELLOW,
                        bgcolor=None,
                        width=widthRow1,
                        height=heightROw1,
                        padding=5,
                        border_radius=10,
                    ),
                ],),

                ft.Row([
                    self.showimage,
                    self.extract,
                    ft.Container(
                        content = self.final_text,
                        #bgcolor=ft.colors.YELLOW,
                        bgcolor=None,
                        width=widthRow2,
                        height=heightROw2,
                        padding=5,
                        border_radius=10,
                    ),
                ],),
        ]

    def draw(self):
        body = ft.Column(
            width=self.width,
            height=self.heigth,
            controls=self.buttons(),
            ),
        return body

