from subprocess import REALTIME_PRIORITY_CLASS
import customtkinter, tkinter
from tkinter import *
from PIL import Image, ImageTk
import os
import sys



PATH = os.path.dirname(os.path.realpath(__file__))

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(PATH + "\\assets/themes/dark-blue.json")  # Themes: "blue" (standard), "green", "dark-blue"
dossier = ("C:\\Users\\Nephystos\\Downloads")
liste_extensions  = {}



class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget
 
    def write(self, s):
        self.text_widget.insert('end', s)
        self.text_widget.see('end')




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        global txt
        self.geometry("800x750+400+100")
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
        self.clear_img = self.load_image("/assets/images/delete.png", 60)
        self.home_image = self.load_image("/assets/images/home.png", 20)
        #alm return realtime Hours, Minutes, Seconds
        
        label = customtkinter.CTkLabel(master=self.frame_1,
                                    image=self.add_app_logo_image,
                                    width=140,
                                    height=25,
                                    fg_color=("white", "gray40"),
                                    corner_radius=8)
        label.grid(row=0, column=0, columnspan=3, padx=10, pady=(5,3), sticky="nsew")
        
######################################################################################################################


        self.combobox = customtkinter.CTkComboBox(master=self.frame_1,
                                            values=["option 1", "option 2"],
                                            command=self.combobox_callback,
                                            width=220)

        self.combobox.grid(row=1, column=0, columnspan=3, padx=10, pady=(0,0), sticky="nsew") #
        self.combobox.set("option 2") 
######################################################################################################################


        self.button_1 = customtkinter.CTkButton(master=self.frame_1, image=self.add_folder_image, text="Add Folder", height=32,
                                                compound="right", command=self.liste_fichiers(dossier))                                  
        self.button_1.grid(row=2, column=0, columnspan=3,padx=10, pady=(30,0),  sticky="nsew")

        self.button_2 = customtkinter.CTkButton(master=self.frame_1, image=self.add_list_image, text="Add Item", height=32,
                                                compound="right", fg_color="#D35B58", hover_color="#C77C78",
                                                command=self.clearext)
        self.button_2.grid(row=3, column=0, columnspan=3, padx=10, pady=(5,0),  sticky="nsew")

        self.button_31 = customtkinter.CTkButton(master=self.frame_1, image=self.clear_img, text="", width=40, height=32,
                                                corner_radius=10, fg_color="#292929", hover_color="#292929",

                                                command=self.clear_txt)
        self.button_31.grid(row=4, column=0, columnspan=1, padx=10, pady=10, sticky="w")

        self.button_3 = customtkinter.CTkButton(master=self.frame_1, image=self.chat_image, text="", width=40, height=40,
                                                corner_radius=10, fg_color="gray40", hover_color="gray25",
                                                command=self.affiche_extensions_triees)
        self.button_3.grid(row=4, column=1, columnspan=1, padx=10, pady=10, sticky="w")

        self.button_4 = customtkinter.CTkButton(master=self.frame_1, image=self.home_image, text="", width=40, height=40,
                                                corner_radius=10, fg_color="gray40", hover_color="gray25",
                                                command=self.liste_fichiers(dossier))
        self.button_4.grid(row=4, column=2, columnspan=1, padx=10, pady=10, sticky="e")

        self.button_6 = customtkinter.CTkButton(master=self.frame_2, image=self.add_user2_image, text="Miam !", width=130, height=30, border_width=2,
                                                corner_radius=10, border_color="gray25", fg_color=("gray84", "gray25"),
                                                hover_color="#f2c831", command=self.eat)
        self.button_6.grid(row=5, column=3, padx=20, pady=10, sticky="nsew")

        txt = Text(master=self.frame_1, bg="grey25", fg="white", font="Roboto" , width=60, highlightbackground="grey25", highlightthickness=0, borderwidth=0, relief="ridge") 
        txt.grid(row=5, column=0, columnspan=3, padx=10, pady=10 , sticky="nsew")

        self.button_5 = customtkinter.CTkButton(master=self.frame_2, image=self.add_user_image, text="Walk", width=130, height=60, border_width=2,
                                                corner_radius=10, border_color="gray25", fg_color=("gray84", "gray25"),
                                                hover_color="#8aea8a", command=self.walk)
        self.button_5.grid(row=0, column=3, padx=20, pady=10 , sticky="nsew")
    
        

        #run the update liste_extensions function every 2 second
        self.after(1000, self.update)


    def combobox_callback(self, choice):
        print("combobox dropdown clicked:", choice)
    def load_image(self, path, image_size):
        """ load rectangular image with path relative to PATH """
        return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))

    def clear_txt(self):
        txt.delete(1.0, END)   
        


    def eat(self):
        txt.insert(END, "Affichage via insert"+"\n")
        txt.see(END)

    def printect(self):
        print(self.liste_extensions)
    
    def clearext(self):
        liste_extensions.clear()
        print(liste_extensions)

    def walk(self):
        print("Affichage via print")



    
    def button_function(self):
        print("button clicked")

    def liste_fichiers(self, dossier):
        for root, dirs, files in os.walk(dossier):
            for fichier in files:
                extension = os.path.splitext(fichier)[1]
                if extension not in liste_extensions:
                    liste_extensions[extension] = 1
                else:
                    liste_extensions[extension] += 1

    def affiche_extensions_triees(self):
        """affiche les extensions et le nombre de fichiers de chaque type"""
        for extension, nombre in sorted(liste_extensions.items(), key=lambda x: x[1], reverse=True):
            print(extension, nombre)
    
    #realtime update of the liste_extensions
    def update():
        app.liste_fichiers(dossier)
        app.after(1000, update)

          




if __name__ == "__main__":
    app = App()
    #run update()

    sys.stdout = StdoutRedirector(txt)
    app.mainloop()







