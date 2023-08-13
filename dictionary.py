from tkinter import *
from PyDictionary import PyDictionary
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Dictionary")
root.geometry("620x470")


def lookup():
    my_text.delete(1.0,END)

    dictionary = PyDictionary()
    defination = dictionary.meaning(my_entry.get())

    for key,value in defination.items():
        my_text.insert(END,key+"\n\n")

        for values in value:
            my_text.insert(END,f" - {values}\n\n")

    
my_labelframe = customtkinter.CTkFrame(root,corner_radius=50)
my_labelframe.pack(pady=20)

my_entry = customtkinter.CTkEntry(my_labelframe,width=400,height=40,border_width=1,placeholder_text="Enter a word")
my_entry.grid(row=0,column=0,padx=10,pady=10)

my_button = customtkinter.CTkButton(my_labelframe,text="Lookup",command=lookup)
my_button.grid(row=0,column=1,padx=10)


text_frame = customtkinter.CTkFrame(root,corner_radius=10)
text_frame.pack(pady=10)

my_text = Text(text_frame,height=20,width=65,wrap=WORD,bd=0,bg="#292929",fg="silver")
my_text.pack(pady=10,padx=10)


root.mainloop()
