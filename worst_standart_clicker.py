from tkinter import *
 
clicks = 0
 
def click_button():
    global clicks
    clicks += 1
    label1 = Label(text="{}".format(clicks), fg="#eee", bg="#333") #не знаю как редачить в этом строку видимо никак лол
    label1.place(relx=.45, rely=.4)
 
root = Tk()
root.title("clicker")
root.geometry("300x200")
 
btn = Button(text="Click Me", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.place(relx=.45, rely=.1)
btn.pack()
 
root.mainloop()