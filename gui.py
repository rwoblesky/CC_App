#simple GUI

from Tkinter import *

#create the window

root = Tk()

#modify root window
root.title("CC Tracking App")
root.geometry("400x400")

app = Frame(root)
app.grid()
button = Button(app, text = "This is a button")
button.grid()

button2 = Button(app)
button2.grid()
button2.configure(text = "This will show text")

button3 = Button(app)
button3.grid()

button3["text"] = "This will show up as well"


#kick off the event loop
root.mainloop()