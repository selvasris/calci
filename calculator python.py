# Author : Selvasri
# Code : Creating "Calculator"using python with the help of tkinter GUI module

# importing GUI modules

import customtkinter
from tkinter import END
from tkinter import messagebox

# execution of called functions


# execution of answer
def answer():
  expression = entryField.get()
  try:
    result = eval(expression)
    ans = round(result, 1)
    entryField.delete(0,END)
    entryField.insert(0,ans)
  except SyntaxError:
    messagebox.showerror("ERROR,INVALID EXPRESSION")
  except ZeroDivisionError:
    messagebox.showerror("ERROR,INVALID EXPRESSION")


def click(number):
  entryField.insert(END, number)


# To delete the data
def clear():
  entryField.delete(0, END)


# creationg the interface (or) frame for app

app = customtkinter.CTk()
app.title('Selva Calculator')
app.geometry("300x320")

app.config(bg="black")

#creating field for calculation

entryField = customtkinter.CTkEntry(app,
                                    font=('arial', 20, 'bold'),
                                    text_color='white',
                                    fg_color='black',width=280,height=50,corner_radius=10,
                                    border_color='white',bg_color='black')
entryField.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

#creating buttons in Calculator

# first row
b7 = customtkinter.CTkButton(app,
                             text='7',
                             font=("arial", 20, "bold"),
                             width=60,
                             bg_color="black",
                             cursor="hand2",
                             command=lambda: click("7"))
b7.grid(row=1, column=0, pady=10)

b8 = customtkinter.CTkButton(app,
                             text='8',
                             font=("arial", 20, "bold"),
                             width=60,
                             bg_color="black",
                             cursor="hand2",
                             command=lambda: click("8"))
b8.grid(row=1, column=1)

b9 = customtkinter.CTkButton(app,
                             text='9',
                             font=("arial", 20, "bold"),
                             width=60,
                             bg_color="black",
                             cursor="hand2",
                             command=lambda: click("9"))
b9.grid(row=1, column=2)

b_plus = customtkinter.CTkButton(app,
                                 text='+',
                                 font=("arial", 20, "bold"),
                                 width=60,
                                 bg_color="black",
                                 cursor="hand2",
                                 fg_color="orange",
                                 command=lambda: click(""))
b_plus.grid(row=1, column=3)

# Second row
b4 = customtkinter.CTkButton(app,
                             text='4',
                             font=("arial", 20, "bold"),
                             width=60,
                             bg_color="black",
                             cursor="hand2",
                             command=lambda: click("4"))
b4.grid(row=2, column=0, pady=10)

b5 = customtkinter.CTkButton(app,
                             text='5',
                             font=("arial", 20, "bold"),
                             width=60,
                             bg_color="black",
                             cursor="hand2",
                             command=lambda: click("5"))
b5.grid(row=2, column=1)

b6 = customtkinter.CTkButton(app,
                             text='6',
                             font=("arial", 20, "bold"),
                             width=60,
                             bg_color="black",
                             cursor="hand2",
                             command=lambda: click("6"))
b6.grid(row=2, column=2)

b_minus = customtkinter.CTkButton(app,
                                  text='-',
                                  font=("arial", 20, "bold"),
                                  width=60,
                                  bg_color="black",
                                  cursor="hand2",
                                  fg_color="orange",
                                  command=lambda: click("-"))
b_minus.grid(row=2, column=3)

# Third row
b1 = customtkinter.CTkButton(app,
                             text='1',
                             font=("arial", 20, "bold"),
                             width=60,
                             bg_color="black",
                             cursor="hand2",
                             command=lambda: click("1"))
b1.grid(row=3, column=0, pady=10)

b2 = customtkinter.CTkButton(app,
                             text='2',
                             font=("arial", 20, "bold"),
                             width=60,
                             bg_color="black",
                             cursor="hand2",
                             command=lambda: click("2"))
b2.grid(row=3, column=1)

b3 = customtkinter.CTkButton(app,
                             text='3',
                             font=("arial", 20, "bold"),
                             width=60,
                             bg_color="black",
                             cursor="hand2",
                             command=lambda: click("3"))
b3.grid(row=3, column=2)

b_multiply = customtkinter.CTkButton(app,
                                     text='*',
                                     font=("arial", 20, "bold"),
                                     width=60,
                                     bg_color="black",
                                     cursor="hand2",
                                     fg_color="orange",
                                     command=lambda: click("*"))
b_multiply.grid(row=3, column=3)

b0 = customtkinter.CTkButton(app,
                             text='0',
                             font=("arial", 20, "bold"),
                             width=60,
                             bg_color="black",
                             cursor="hand2",
                             command=lambda: click("0"))
b0.grid(row=4, column=0, pady=10)

#last row
b_dot = customtkinter.CTkButton(app,
                                text='.',
                                font=("arial", 20, "bold"),
                                width=60,
                                bg_color="black",
                                cursor="hand2",
                                command=lambda: click("."))
b_dot.grid(row=4, column=1)

b_clear = customtkinter.CTkButton(app,
                                  text='C',
                                  font=("arial", 20, "bold"),
                                  width=60,
                                  bg_color="black",
                                  cursor="hand2",
                                  fg_color="red",
                                  hover_color="red4",
                                  command=clear)
b_clear.grid(row=4, column=2)

b_divide = customtkinter.CTkButton(app,
                                   text='/',
                                   font=("arial", 20, "bold"),
                                   width=60,
                                   bg_color="black",
                                   cursor="hand2",
                                   fg_color="orange",
                                   command=lambda: click("/"))
b_divide.grid(row=4, column=3)


b_equal = customtkinter.CTkButton(app,
                                  text='=',
                                  font=("arial", 20, "bold"),
                                  width=280,
                                  bg_color="black",
                                  cursor="hand2",
                                  fg_color="green",
                                  hover_color="dark green",
                                  command=answer)
b_equal.grid(row=5, column=0, columnspan=4, pady=10)

app.mainloop()