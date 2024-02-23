from tkinter import *

root = Tk()

root.title('Chat Bot')

root.geometry('400x500')

main_menu = Menu(root)

file_menu = Menu(root)
file_menu.add_command(label='New..')
file_menu.add_command(label='Save As..')
file_menu.add_command(label='Exit')

main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_command(label='Edit')
main_menu.add_command(label='Quit')
root.config(menu=main_menu)

chat_window = Text(root, bd=1, bg='black', width=50, height=8)
chat_window.place(x=6, y=6, height=385, width=370)

message = Text(root, bg='black', width=30, height=4, )
chat_window.place(x=128, y=400, height=88, width=260)

# A button to send the message
Button = Button(root, text='Send', bg='blue', activebackground='light blue', width=12, height=5, font=('Arial', 10))
Button.place(x=6, y=400, height=88, width=120)


root.mainloop()
