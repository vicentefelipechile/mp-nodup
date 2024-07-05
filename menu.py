from customtkinter import CTk as CustomTK

class Menu(CustomTK):
    def __init__(self):
        super().__init__()
        self.title("Menu")
        self.geometry("300x300")
    

    def button_debug(self):
        print("Button Debug")