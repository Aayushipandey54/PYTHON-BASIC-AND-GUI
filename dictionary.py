from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import nltk
from nltk.corpus import wordnet
from googletrans import Translator

root = tk.Tk()
root.title('Dictionary')
root.geometry('600x300')
root['bg'] = 'white'
frame = Frame(root, width=200, height=300, borderwidth=1, relief=RIDGE) 
frame.grid(sticky="W") 

def get_meaning():
    get_word = entry.get()
    language = langauage.get()

    if get_word == "":
        messagebox.showerror('Dictionary', 'Please write the word')
    elif language == 'English-to-English':
        syns = wordnet.synsets(get_word)
        if syns:
            definition = syns[0].definition()
            output.insert('end', definition)
        else:
            messagebox.showerror('Dictionary', 'No definition found for this word')
    elif language == 'English-to-Hindi':
        translator = Translator()
        t = translator.translate(get_word, dest='hi')
        output.insert('end', t.text)

def exit_app():
    root.destroy()

img = ImageTk.PhotoImage(Image.open('dict.png'))
pic = Label(root, image=img)
pic.place(x=40, y=70)

word = Label(root, text="Enter Word", bg="white", font=('verdana', 10, 'bold'))
word.place(x=250, y=23)

a = tk.StringVar() 
langauage = ttk.Combobox(root, width=20, textvariable=a, state='readonly', font=('verdana', 10, 'bold')) 
langauage['values'] = (
    'English-to-English',
    'English-to-Hindi',
)
langauage.place(x=380, y=10)
langauage.current(0) 

entry = Entry(root, width=50, borderwidth=2, relief=RIDGE)
entry.place(x=250, y=50)

search = Button(root, text="Search", font=('verdana', 10, 'bold'), cursor="hand2", relief=RIDGE, command=get_meaning)
search.place(x=430, y=80)

quit_btn = Button(root, text="Quit", font=('verdana', 10, 'bold'), cursor="hand2", relief=RIDGE, command=exit_app)
quit_btn.place(x=510, y=80)

meaning = Label(root, text="Meaning", bg="white", font=('verdana', 15, 'bold'))
meaning.place(x=230, y=120)

output = Text(root, height=8, width=40, borderwidth=2, relief=RIDGE)
output.place(x=230, y=160)

root.mainloop()
