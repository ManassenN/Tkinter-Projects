from tkinter import *
from tkinter import filedialog

from PIL import ImageTk,Image


# --------------------------------------------------OPEN--------------------------------------------------
def open():
    browse_text.set('Loading...')
    photo_name = filedialog.askopenfilename(initialdir="C:/Users/nerya/PycharmProjects/Image-Watermarking-Desktop-App"
                                               , title="Select A File",
                                               filetypes=(("png files", "*.png"), ("all files", "*.*")))
    if photo_name:
        image = Image.open(photo_name)
        wm_image = Image.open("watermark.png")

        wm_resized = wm_image.resize((round(image.size[0] * .35), round(image.size[1] * .35)))
        image.paste(wm_resized)
        image.show()


# --------------------------------------------------SAVE--------------------------------------------------
def save():
    pass
# --------------------------------------------------QUIT--------------------------------------------------
def quit():
    root.destroy()

# GUI should allow you to select photo / path to add images,
#  Outgoing photo name / path
root = Tk()
root.title("Photo Watermark App")

canvas = Canvas(root, width=600, height=500)
canvas.grid(columnspan=5, rowspan=4)

logo = Image.open("logo.png")
logo = logo.resize((200, 200))
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.grid(column=2, row=0)

instruction_label = Label(root,text = 'Select photo to watermark.',font =(("courirer"),30))
instruction_label.grid(column = 0,row =1,columnspan=5,padx = 10)

# Browse dialog button
browse_text = StringVar()
browse_button = Button(root, command = open,textvariable =browse_text,height = 5,width = 15,bg = 'white')
browse_text.set("Browse")
browse_button.grid(column = 0,row = 3)


quit_button = Button(root, command = quit,text ="Quit",height = 5,width = 15,bg = 'white')
quit_button.grid(column = 4,row = 3)


root.mainloop()