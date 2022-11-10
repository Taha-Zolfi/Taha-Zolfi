from tkinter import *
# from eliot import text


def click():
    print("user clicked")
    from eliot import run_elliot

win = Tk()

# win.geometry("800x800")

win.title('bro AI')

picture = PhotoImage(file='ol.png')

pic = PhotoImage(file='de.png')

pic1 = PhotoImage(file='rt.png')

pic2 = PhotoImage(file='rel.gif')
photo = PhotoImage(file='pic.gif')

win.iconphoto(True, photo)

win.config(background='#9761fa')


lable = Label(
    win,
    text='welcome to your AI assessment',
    font=('Lalezar',40),
    fg='cyan',
    bg='#9761fa',
    compound='bottom'
    )
lable.pack()


buttons = Button(
    win,
    text="کلیک کن",
    command=click,
    font=('Lalezar',20),
    fg="#9761fa",
    bg="#9761fa",
    activebackground="#9761fa",
    activeforeground='cyan',
    image=picture)
buttons.pack()

lable2 = Label(win, image=pic,bg='#9761fa', compound='center' )
lable2.pack()

# entery = Entry(win,font=('Lalezar',30),text(text))
# entery.pack()
# submit = Button(win,text='submit',image=pic1,bg="#9761fa",activebackground="#9761fa")
# submit.pack()

win.mainloop()