import tkinter

FONT = ("Arial", 14, 'normal')
window = tkinter.Tk()
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)
window.title("Mile to KM Converter")

mile_input = tkinter.Entry()
mile_input.config(font=FONT, width=10)
mile_input.grid(column=1, row=0)

mile_lbl = tkinter.Label(text='Miles')
mile_lbl.config(font=FONT)
mile_lbl.grid(column=2, row=0)

equal_lbl = tkinter.Label(text='is equal to')
equal_lbl.config(font=FONT)
equal_lbl.grid(column=0, row=1)

result_lbl = tkinter.Label(text='0')
result_lbl.config(font=FONT)
result_lbl.grid(column=1, row=1)

km_lbl = tkinter.Label(text='Km')
km_lbl.config(font=FONT)
km_lbl.grid(column=2, row=1)

def calc():
    result_lbl.config(text=round(int(mile_input.get()) * 1.609344, 4))
calc_btn = tkinter.Button(text='Calculate', command=calc)
calc_btn.config(font=FONT)
calc_btn.grid(column=1, row=2)


window.mainloop()