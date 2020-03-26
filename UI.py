from tkinter import *
import Administrator
import WaitList


def main_screen():
    global screen
    global wait_list
    wait_list = WaitList()
    screen = Tk()
    screen.geometry("600x300")
    screen.title("Attendance System Login")
    # screen.configure(background='turquoise')

    Label(screen, text="Club/Organization ID", width="20", height="2", font=("new roman", 15)).grid(row=1, column=0)
    Entry(screen, width="20").grid(row=2, column=0)
    Label(screen, text="Password", width="20", height="2", font=("new roman", 15)).grid(row=3)
    Entry(screen, width="20").grid(row=4, column=0)
    Label(screen, text="").grid(row=5)

    # highlightbackground = 'green'
    Button(screen, text="Login", height="3", width="20", command=login, fg='black').grid(row=6, column=0)

    Button(screen, text="Administrator", height="3", width="20", command=admin, fg='black', ).grid(row=2, column=2)
    Button(screen, text="Member", height="3", width="20", command=member, fg='black', ).grid(row=3, column=2)

    Button(screen, text="Login", height="3", width="20", command=login, fg='black').grid(row=6, column=0)
    Button(screen, text="Forget/Reset Password", height="3", width="20", command=forget, fg='black').grid(row=6,
                                                                                                          column=1)

    Button(screen, text="New Club Register", height="3", width="20", command=club_register, fg='black').grid(row=6,
                                                                                                             column=2)

    # global button
    # button = Button(screen,text='Submit',command=changeText)
    # button.pack()

    screen.mainloop()


# def changeText():
#     if (button['text'] == 'Submit'):
#         button['text'] = 'Submitted'
#     else:
#         button['text'] = 'Submit'

def club_info():
    file = open(club_id.get() + ".txt", "w")
    file.write(club_id.get() + "\n")
    file.write(club_name.get() + "\n")
    file.write(club_email.get() + "\n")
    file.write(club_password.get() + "\n")
    file.write(club_confirm_password.get() + "\n")
    file.close()

    club_id_entry.delete(0, END)
    club_name_entry.delete(0, END)
    club_email_entry.delete(0, END)
    club_password_entry.delete(0, END)
    club_confirm_password_entry.delete(0, END)

    Label(screen1, text="Registration sent", fg="green", font=("new roman", 15)).pack()
    global admin
    admin = Administrator(club_id.get(), club_name.get(), club_email.get(), club_password.get(), wait_list)

def member_info():

    file = open(member_id.get() + ".txt", "w")
    file.write(member_id.get() + "\n")
    file.write(member_name.get() + "\n")
    file.write(member_email.get() + "\n")
    file.write(member_password.get() + "\n")
    file.write(member_confirm_password.get() + "\n")
    file.write(member_apply_club_id.get() + "\n")
    file.close()

    member_id_entry.delete(0,END)
    member_name_entry.delete(0,END)
    member_email_entry.delete(0,END)
    member_password_entry.delete(0,END)
    member_confirm_password_entry.delete(0,END)
    member_apply_club_id_entry.delete(0,END)

    Label(screen1, text = "Registration sent", fg = "green", font=("new roman", 15)).pack()


def club_register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("New Club Registration")
    screen1.geometry("600x570")

    global club_id
    global club_name
    global club_email
    global club_password
    global club_confirm_password

    club_id = StringVar()
    club_name = StringVar()
    club_email = StringVar()
    club_password = StringVar()
    club_confirm_password = StringVar()

    global club_id_entry
    global club_name_entry
    global club_email_entry
    global club_password_entry
    global club_confirm_password_entry

    # 1
    Label(screen1, text="").pack()
    Label(screen1, text="Club/Organization ID").pack()
    club_id_entry = Entry(screen1, textvariable=club_id)
    club_id_entry.pack()

    # 2
    Label(screen1, text="").pack()
    Label(screen1, text="Name of the Club/Organization").pack()
    club_name_entry = Entry(screen1, textvariable=club_name)
    club_name_entry.pack()
    # 3
    Label(screen1, text="").pack()
    Label(screen1, text="Club/Organization Email").pack()
    club_email_entry = Entry(screen1, textvariable=club_email)
    club_email_entry.pack()
    # 4
    Label(screen1, text="").pack()
    Label(screen1, text="Password").pack()
    club_password_entry = Entry(screen1, textvariable=club_password)
    club_password_entry.pack()
    # 5
    Label(screen1, text="").pack()
    Label(screen1, text="Confirm Password").pack()
    club_confirm_password_entry = Entry(screen1, textvariable=club_confirm_password)
    club_confirm_password_entry.pack()

    # 6
    Label(screen1, text="").pack()
    Button(screen1, text="Register", height="3", width="20", command=club_info).pack()



def member_register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("New Club Registration")
    screen1.geometry("600x570")

    global member_id
    global member_name
    global member_email
    global member_password
    global member_confirm_password
    global member_apply_club_id

    member_id = StringVar()
    member_name = StringVar()
    member_email = StringVar()
    member_password = StringVar()
    member_confirm_password = StringVar()
    member_apply_club_id = StringVar()

    global member_id_entry
    global member_name_entry
    global member_email_entry
    global member_password_entry
    global member_confirm_password_entry
    global member_apply_club_id_entry

    # 1
    Label(screen1, text="").pack()
    Label(screen1, text="User ID").pack()
    member_id_entry = Entry(screen1, textvariable=member_id)
    member_id_entry.pack()
    # 2
    Label(screen1, text="").pack()
    Label(screen1, text="Name").pack()
    member_name_entry = Entry(screen1, textvariable=member_name)
    member_name_entry.pack()
    # 3
    Label(screen1, text="").pack()
    Label(screen1, text="Email").pack()
    member_email_entry = Entry(screen1, textvariable=member_email)
    member_email_entry.pack()
    # 4
    Label(screen1, text="").pack()
    Label(screen1, text="Password").pack()
    member_password_entry = Entry(screen1, textvariable=member_password)
    member_password_entry.pack()
    # 5
    Label(screen1, text="").pack()
    Label(screen1, text="Confirm Password").pack()
    member_confirm_password_entry = Entry(screen1, textvariable=member_confirm_password)
    member_confirm_password_entry.pack()
    # 6
    Label(screen1, text="").pack()
    Label(screen1, text="Club/Organization ID").pack()
    member_apply_club_id_entry = Entry(screen1, textvariable=member_apply_club_id)
    member_apply_club_id_entry.pack()
    # 7
    Label(screen1, text="").pack()
    Button(screen1, text="Register", height="3", width="20", command=member_info).pack()



def admin():
    Label(screen, text="Club/Organization ID", width="20", height="2", font=("new roman", 15)).grid(row=1, column=0)
    Label(screen, text="Password", width="20", height="2", font=("new roman", 15)).grid(row=3)
    Button(screen, text="New Club Register", height="3", width="20", command=club_register, fg='black').grid(row=6,
                                                                                                             column=2)


def member():
    Label(screen, text="User ID", width="20", height="2", font=("new roman", 15)).grid(row=1, column=0)
    Button(screen, text="New Member Register", height="3", width="20", command=member_register, fg='black').grid(row=6,
                                                                                                                 column=2)


def login():
    print("Login session started")


def forget():
    print("U SUCK")


main_screen()