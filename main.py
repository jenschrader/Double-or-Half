# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 09:11:15 2022

@author: JenSc
"""


###############################################################################

# =============================================================================
# *-- FINAL EXAM PT 2 --*
# *************************************
# program description
# this program creates a GUI application
# that allows users to input an integer
# and doubles the integer or halves it
# depending on what button the user pushes.
# *************************************
# naming convention
# =============================================================================
# *-- imports --*
# *************************************
import tkinter as tk
import customtkinter
from tkinter import messagebox
from PIL import Image
# *************************************

# =============================================================================
# *-- code --*
# *****************************************************************************

# creating a class for app


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # themes
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('green')

        # setting up window
        self.geometry('280x220+680+340')
        self.title('Jennifer Schrader')
        self.resizable(False, False)
        self.icon_img = tk.PhotoImage(file='icon.png')
        self.iconphoto(False, self.icon_img)
        
        self.img = customtkinter.CTkImage(dark_image=Image.open('img-export.png'), size=(50,50))


        # string var for result
        self.result_var = tk.StringVar()

        self.main_frame = customtkinter.CTkFrame(
            master=self,
            width=200,
            height=200)
        self.main_frame.pack(side='top', fill='both')

        # config grid
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        # self.rowconfigure((0, 1, 2), weight=1)
        self.img_label = customtkinter.CTkLabel(
            master=self.main_frame,
            image=self.img,
            text='')
        self.img_label.pack(
            side='top',
            pady=10)
        # label
        self.label = customtkinter.CTkLabel(
            master=self.main_frame,
            text='Enter an integer',
            width=120,
            height=30,
            fg_color=('transparent'),
            text_color=('white'),
            font=('Silkscreen', 14))
        # self.label.grid(row=1, column=1, padx=20, pady=20)
        self.label.pack(
            side='top',
            padx=20,
            pady=2)

        # entry
        self.entry = customtkinter.CTkEntry(
            master=self.main_frame,
            width=100,
            height=10,
            text_color=('white'),
            font=('Silkscreen', 14),
            justify='center')
        
        # self.entry.grid(row=2, column=1)
        self.entry.pack(
            side='top',
            padx=20,
            pady=20)
        
        self.btn_double = customtkinter.CTkButton(
            master=self.main_frame,
            width=30,
            height=30,
            text='double',
            text_color='white',
            font=('Silkscreen', 12),
            fg_color=('transparent'),
            border_width=1,
            border_color=('white'),
            command=self.double_btn_event)
        
        # self.btn_double.grid(
        #     row=5,
        #     column=1,
        #     pady=20)
        self.btn_double.pack(
            side='left',
            padx=10,
            pady=10)
        
        self.btn_half = customtkinter.CTkButton(
            master=self.main_frame,
            width=30,
            height=30,
            text='half',
            text_color='white',
            font=('Silkscreen', 12),
            fg_color='transparent',
            border_width=1,
            border_color='white',
            command=self.half_btn_event)

        # self.btn_half.grid(
        #     row=5,
        #     padx=(20, 0),
        #     column=1)
        self.btn_half.pack(
            side='right',
            padx=10,
            pady=10,
            ipadx=10)
        
        # result label
        self.result = customtkinter.CTkLabel(
           master=self.main_frame,
           textvariable=self.result_var,
           width=120,
           height=30,
           fg_color=('transparent'),
           text_color=('white'),
           font=('Silkscreen', 14))
        self.result.pack(side='bottom')
# *************************************

    # *-- functions --*
# *************************************
    def double_btn_event(self):
        # make sure something is entered
        if self.entry.get() == '':
            messagebox.showerror('error', 'enter a number first!')
        # make sure entry doesnt contain commas
        elif ',' in self.entry.get():
            messagebox.showerror('error', 'enter the number without commas!')
        else:
            # get entry
            self.user_entry = float(self.entry.get())
            # find result
            self.double_val = self.user_entry * 2
            # store temp in string var & format
            self.result_var.set(f'{self.double_val:.1f}')
            # clearing entry box
            self.entry.delete(0, tk.END)

    def half_btn_event(self):
        if self.entry.get() == '':
            messagebox.showerror('error', 'enter a number first!')
        elif ',' in self.entry.get():
            messagebox.showerror('error', 'enter the number without commas!')
        else:
            # get entry
            self.user_entry = float(self.entry.get())
            # find result
            self.half_val = self.user_entry / 2
            # store temp in string var & format
            self.result_var.set(f'{self.half_val:.1f}')
            # clearing entry box
            self.entry.delete(0, tk.END)
# *****************************************************************************


# =============================================================================


# *************************************
if __name__ == "__main__":
    app = App()
    app.mainloop()

# *************************************

###############################################################################
