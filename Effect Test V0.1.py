from customtkinter import *
from PIL import Image

win = CTk()
win.geometry('400x300')
win.title('Effect Test')


label = CTkLabel(win, text='Pick an Effect!', font=('Arial', 14, 'bold'))
label.grid(row=0,column=0,pady=20)


btn_1 = CTkButton(win, text='Fire',width=300)
btn_1.grid(row=1,column=1,pady=20)
img1= Image.open('fire3.jpg')
img_ctk1 = CTkImage(light_image=img1, size=(350, 200))

btn_2 = CTkButton(win, text='Water')
btn_2.grid(row=1, column=2)
img2= Image.open('water5.jpg')
img_ctk2 = CTkImage(light_image=img2, size=(350, 200))

btn_3 = CTkButton(win, text='Acid')
btn_3.grid(row=1,column=3)
img3= Image.open('acid5.jpg')
img_ctk3 = CTkImage(light_image=img3, size=(350, 200))

btn_4 = CTkButton(win, text='Lava')
btn_4.grid(row=2, column=1)
img4= Image.open('lava.jpg')
img_ctk4 = CTkImage(light_image=img4, size=(350, 200))


btn_5 = CTkButton(win, text='Night')
btn_5.grid(row=2,column=2)
img5= Image.open('night.jpg')
img_ctk5 = CTkImage(light_image=img5, size=(350, 200))

btn_6 = CTkButton(win, text='Plasma')
btn_6.grid(row=2, column=3)
img6= Image.open('plasma2.jpg')
img_ctk6 = CTkImage(light_image=img6, size=(350, 200))


win.mainloop()