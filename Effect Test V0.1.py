from customtkinter import *
from PIL import Image

win = CTk()
win.geometry('600x600')
win.title('Effect Test')


label = CTkLabel(win, text='Pick an Effect!', font=('Arial', 14, 'bold'))
label.grid(row=0,column=2,columnspan=3,pady=20,padx=10)

def btn_1_click():
    label_text.configure(text="11111")

img1= Image.open('fire3.jpg')
img_ctk1 = CTkImage(light_image=img1, size=(100, 100))
btn_1 = CTkButton(win, text='Fire',width=100,image=img_ctk1,command=btn_1_click)
btn_1.grid(row=1,column=1,pady=20,padx=10)


def btn_2_click():
    label_text.configure(text="22222")
img2= Image.open('water5.jpg')
img_ctk2 = CTkImage(light_image=img2, size=(100, 100))
btn_2 = CTkButton(win, text='Water',width=100,image=img_ctk2,command=btn_2_click)
btn_2.grid(row=1, column=2,pady=20,padx=10)

def btn_3_click():
    label_text.configure(text="33333")
img3= Image.open('acid5.jpg')
img_ctk3 = CTkImage(light_image=img3, size=(100, 100))
btn_3 = CTkButton(win, text='Acid',width=100,image=img_ctk3,command=btn_3_click)
btn_3.grid(row=1,column=3,pady=20,padx=10)

def btn_4_click():
    label_text.configure(text="444444")
img4= Image.open('lava.jpg')
img_ctk4 = CTkImage(light_image=img4, size=(100, 100))
btn_4 = CTkButton(win, text='Lava',width=100,image=img_ctk4,command=btn_4_click)
btn_4.grid(row=2, column=1,pady=20,padx=10)

def btn_5_click():
    label_text.configure(text="55555")
img5= Image.open('night.jpg')
img_ctk5 = CTkImage(light_image=img5, size=(100, 100))
btn_5 = CTkButton(win, text='Night',width=100,image=img_ctk5,command=btn_5_click)
btn_5.grid(row=2,column=2,pady=20,padx=10)

def btn_6_click():
    label_text.configure(text="6666666")
img6= Image.open('plasma2.jpg')
img_ctk6 = CTkImage(light_image=img6, size=(100, 100))
btn_6 = CTkButton(win, text='Plasma',width=100,image=img_ctk6,command=btn_6_click)
btn_6.grid(row=2, column=3,pady=20,padx=10)


label_text = CTkLabel(win, text='text', font=('Arial', 14, 'bold'))
label_text.grid(row=3,column=1,columnspan=3,pady=20,padx=10)
win.mainloop()
