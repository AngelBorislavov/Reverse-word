from tkinter import *

root = Tk()
root.title('Revers word')

def my_button():
    word_value = word.get()[::-1]
    write.config(text = word_value)
    write.pack()

#add widgets
word = Entry(root , width= 40 , font=24)
button = Button(root,text = 'Revers',padx= 40 , pady= 10,command=my_button)
write = Label(root ,padx= 20 ,pady= 10 , font=24)

#show widgets
word.pack()
button.pack()

root.mainloop()

