import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
win = Tk()
width= win.winfo_screenwidth()
height= win.winfo_screenheight()
win.geometry("%dx%d" % (width, height))
background_image = PhotoImage(file="gradient.png")
label = Label(win, text="Rural Health Monitoring System", font=('Times', 50))
label.configure(bg="#ffffff")
label.place(x=width/2-400,y=10)

image1 = Image.open("Logo.png")
image1 = image1.resize((150, 150))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=width-200, y=10)

image1 = Image.open("5GLab.jpg")
image1 = image1.resize((150, 150))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=50, y=10)


#dropdown
options = ["       🟢  Usha               ", "       🔴  Prajwal       ","       🟢  Amogh               ","       🔴  Ananda       "]
selected_option = StringVar(win)
selected_option.set("Usha")
dropdown = OptionMenu(win, selected_option, *options, '''command=update_labels''')
dropdown.configure(bg='blue',fg='white',width=20, font=('Helvetica',20))
dropdown["menu"].configure(font=("Helvetica", 20), fg="white", bg = "blue")
#dropdown["menu"].configure(width=20)
dropdown.place(x=50,y=height/2-200)
# combobox = ttk.Combobox(win, textvariable=selected_option, values=options, width=30)
# combobox.place(x=50,y=height/2-200)
# style = ttk.Style()
# style.configure("TCombobox", background="blue", foreground="white")

#Labels Left Column
label1 = Label(win, text="History", font=('Helvetica', 20))
label1.configure(bg='blue',fg='white',width=21)
label1.place(x=50,y=height/2+100)

label2 = Label(win, text="Reports", font=('Helvetica', 20))
label2.configure(bg='blue',fg='white',width=21)
label2.place(x=50,y=height/2 + 175)

label3 = Label(win, text="Search", font=('Helvetica', 20))
label3.configure(bg='blue',fg='white',width=21)
label3.place(x=50,y=height/2 + 250)

image2 = Image.open("search.png")
image2 = image2.resize((34, 34))
test = ImageTk.PhotoImage(image2)
label4 = tkinter.Label(image=test)
label4.image = test
label4.place(x=7, y=height/2 + 250)

#Labels Center Column
image1 = Image.open("Usha.jpg")
image1 = image1.resize((350, 250))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=width/2-150,y=height/2-200)

label5 = Label(win, text="Name and Aadhaar", font=('Helvetica', 20))
label5.configure(bg='blue',fg='white',width=21)
label5.place(x=width/2-150,y=height/2+100)

label6 = Label(win, text="BPM", font=('Helvetica', 20))
label6.configure(bg='blue',fg='white',width=21)
label6.place(x=width/2-150,y=height/2+175)

label7 = Label(win, text="Temperature", font=('Helvetica', 20))
label7.configure(bg='blue',fg='white',width=21)
label7.place(x=width/2-150,y=height/2+250)

#Labels Right Column
image1 = Image.open("Graph.png")
image1 = image1.resize((300, 200))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=width-400, y=height/2-200)

# gif_image = PhotoImage(file="Graph.gif")
# image_label = Label(win, image=gif_image)
# image_label.pack()

def update_labels(event):
    # selected_option = selected_option.get()
    selected_option = selected_option.get()
    print("Hi")

    if selected_option == "Usha":
        label9.configure(text="Usha")
        label10.config(text="72")
        label11.config(text="93.33")
    elif selected_option == "Prajwal":
        label9.configure(text="Prajwal")
        label10.config(text="Some other value")
        label11.config(text="Another value")
    elif selected_option == "Amogh":
        label9.config(text="Amogh")
        label10.config(text="Different value")
        label11.config(text="Another value")
    elif selected_option == "Ananda":
        label9.config(text="Ananda")
        label10.config(text="Another value")
        label11.config(text="Different value")

label9 = Label(win, text="Usha  284612024037", font=('Helvetica', 20))
label9.configure(bg='blue',fg='white',width=21)
label9.place(x=width-400,y=height/2+100)

label10 = Label(win, text="72", font=('Helvetica', 20))
label10.configure(bg='blue',fg='white',width=21)
label10.place(x=width-400,y=height/2+175)

label11 = Label(win, text="93.33", font=('Helvetica', 20))
label11.configure(bg='blue',fg='white',width=21)
label11.place(x=width-400,y=height/2+250)

#end
mainloop()
