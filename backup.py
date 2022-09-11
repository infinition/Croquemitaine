from cgitb import grey
from turtle import color
import customtkinter, tkinter
from tkinter import *
from PIL import Image, ImageTk
from assets import *
import os
import time



PATH = os.path.dirname(os.path.realpath(__file__))



customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"

#customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("assets/themes/dark-blue.json")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x700+400+100")
        self.title("Croquemitaine")
        self.iconbitmap(PATH + "/assets/images/logo.ico")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1, minsize=200)



        self.frame_1 = customtkinter.CTkFrame(master=self, width=250, height=240, corner_radius=15)
        self.frame_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.frame_1.grid_columnconfigure(0, weight=1)
        self.frame_1.grid_columnconfigure(1, weight=1)

        self.frame_2 = customtkinter.CTkFrame(master=self, width=150, height=240, corner_radius=15)
        self.frame_2.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.frame_2.grid_columnconfigure(0, weight=1)
        self.frame_2.grid_columnconfigure(1, weight=1)

        self.settings_image = self.load_image("/assets/images/settings.png", 20)
        self.bell_image = self.load_image("/assets/images/bell.png", 20)
        self.add_folder_image = self.load_image("/assets/images/add-folder.png", 20)
        self.add_list_image = self.load_image("/assets/images/add-folder.png", 20)
        self.add_user_image = self.load_image("/assets/images/logo.png", 100)
        self.add_user2_image = self.load_image("/assets/images/logo2.png", 100)
        self.add_app_logo_image = self.load_image("/assets/images/logo.ico", 20)
        self.chat_image = self.load_image("/assets/images/chat.png", 20)
        self.home_image = self.load_image("/assets/images/home.png", 20)

        text_var = tkinter.StringVar(value="CTkLabel")
        label = customtkinter.CTkLabel(master=self.frame_1,
                                    textvariable=text_var,
                                    width=140,
                                    height=25,
                                    fg_color=("white", "gray40"),
                                    corner_radius=8)
        label.grid(row=0, column=0, columnspan=2, padx=10, pady=(5,3), sticky="nsew")
      
        

        def combobox_callback(choice):
            print("combobox dropdown clicked:", choice)
        
        def send(self):
            send = "Vous -> " + e.get() 
            self.txt.insert(END, "\n" + send)
            txt.insert(END, "\n" + "")
            #wait 1 second
            txt.see(END)

        def send2():
            send = "Vous -> " + e.get() 
            self.txt.insert(END, "\n" + send)
            txt.insert(END, "\n" + "")
            #wait 1 second

        def clear_txt():
            txt.delete(1.0, END)
        
        

    

        self.combobox = customtkinter.CTkComboBox(master=self.frame_1,
                                            values=["option 1", "option 2"],
                                            command=combobox_callback,
                                            width=220)

        self.combobox.grid(row=1, column=0, columnspan=2, padx=10, pady=(0,0), sticky="nsew") #
        self.combobox.set("option 2") 
        
        

        self.button_1 = customtkinter.CTkButton(master=self.frame_1, image=self.add_folder_image, text="Add Folder", height=32,
                                                compound="right", command=self.button_function)
                                                
        self.button_1.grid(row=2, column=0, columnspan=2,padx=10, pady=(30,0),  sticky="nsew")

        self.button_2 = customtkinter.CTkButton(master=self.frame_1, image=self.add_list_image, text="Add Item", height=32,
                                                compound="right", fg_color="#D35B58", hover_color="#C77C78",
                                                command=self.button_function)
        self.button_2.grid(row=3, column=0, columnspan=2, padx=10, pady=(5,0),  sticky="nsew")

        self.button_3 = customtkinter.CTkButton(master=self.frame_1, image=self.chat_image, text="", width=40, height=40,
                                                corner_radius=10, fg_color="gray40", hover_color="gray25",
                                                command=self.button_function)
        self.button_3.grid(row=4, column=0, columnspan=1, padx=10, pady=10, sticky="w")

        self.button_4 = customtkinter.CTkButton(master=self.frame_1, image=self.home_image, text="", width=40, height=40,
                                                corner_radius=10, fg_color="gray40", hover_color="gray25",
                                                command=self.button_function)
        self.button_4.grid(row=4, column=1, columnspan=1, padx=10, pady=10, sticky="e")



        self.button_6 = customtkinter.CTkButton(master=self.frame_2, image=self.add_user2_image, text="Miam !", width=130, height=30, border_width=2,
                                                corner_radius=10, border_color="gray25", fg_color=("gray84", "gray25"),
                                                hover_color="#f2c831", command=self.button_function)
        self.button_6.grid(row=5, column=2, padx=20, pady=10, sticky="nsew")




        def write_on_txt():
            send = "Button clicked"
            txt.insert(END, "\n" + send)
            txt.see(END)
        



        txt = Text(master=self.frame_1, bg="grey25", fg="white", font="Roboto" , width=60)
        txt.grid(row=5, column=0, columnspan=2, padx=10, pady=10 , sticky="nsew")
        



             
        self.button_5 = customtkinter.CTkButton(master=self.frame_2, image=self.add_user_image, text="Walk", width=130, height=60, border_width=2,
                                                corner_radius=10, border_color="gray25", fg_color=("gray84", "gray25"),
                                                hover_color="#8aea8a", command=write_on_txt)
        self.button_5.grid(row=0, column=2, padx=20, pady=10 , sticky="nsew")






    def load_image(self, path, image_size):
        """ load rectangular image with path relative to PATH """
        return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))

    def button_function(self):
        self.txt.insert(END, "\n" + "Button clicked")
        self.txt.insert(END, "\n" + "")
            #wait 1 second
        self.txt.see(END)
        print("button pressed")
    





if __name__ == "__main__":
    app = App()
    app.mainloop()






