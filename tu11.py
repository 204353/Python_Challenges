import tkinter
import random
window = tkinter.Tk()
firstname = ["Jack", "James", "Jerry", "Jerome", "Jaques", "John", "Johnny"]
lastname = ["Strong", "Davis", "Blaze", "Tom"]
def randomnames():
    d = random.choice(firstname)
    y = random.choice(lastname)
    names.configure(text = str(d) + " " + str(y))
mytitle = tkinter.Label(window, text = 'Name with J', font = "Helvetica 16")
mytitle.pack()
MyButton = tkinter.Button(window, command = randomnames)
MyButton.pack()
names = tkinter.Label(window, text = "Click the button for a name")
names.pack()
window.mainloop()