import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, 'bold'))
my_label.pack()

#Button
def button_clicked():
    my_label['text'] = input.get()
my_btn = tkinter.Button(text='Click me!', command=button_clicked)
my_btn.pack()

#Entry
input = tkinter.Entry(width=10)
input.pack()



tkinter.mainloop()