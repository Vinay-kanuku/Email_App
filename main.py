from tkinter import *
import smtplib
back_ground = "lightgreen"
EMAIL = "vinaykanuku7565@gmail.com"
PASSWORD = "sbmvdfpedvnpnwof"
FONT = "Cascadia Mono", 15, "normal"


def Send():
    mes = message_entry.get("1.0", "end-1c")
    sub = sub_entry.get()
    email = to_mail_entry.get()
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=email, msg=f"Subject:{sub}\n\n{mes}")
    exit(0)


window = Tk()
window.config(padx=50, pady=50, bg=back_ground)
window.title("Email")
canvas = Canvas(width=140, height=140)
image = PhotoImage(file="gmail_5968534.png")
canvas.create_image(70, 50, image=image)
canvas.config(bg=back_ground, highlightthickness=0)
canvas.grid(column=1, row=0)
my_mail = Label(text="From: ", font=FONT, bg=back_ground)
my_mail.grid(column=0, row=1)
my_mail_entry = Entry(width=30, bg=back_ground, font=FONT)
my_mail_entry.insert(0, string="vinaykanuku7565@gmail.com")
my_mail_entry.config(highlightcolor="blue", highlightthickness=1)
my_mail_entry.grid(column=1, row=1, columnspan=1)

to_mail_label = Label(text=" To:", font=FONT, bg=back_ground)
to_mail_entry = Entry(width=30, bg=back_ground, font=FONT)
to_mail_entry.config(highlightcolor="blue", highlightthickness=1)
to_mail_label.grid(column=0, row=2)
to_mail_entry.grid(column=1, row=2, columnspan=1)

sub_label = Label(text="Subject:    ", font=FONT, bg=back_ground)
sub_entry = Entry(width=30, bg=back_ground, font=FONT)
sub_entry.config(highlightcolor="blue", highlightthickness=1)
sub_label.grid(column=0, row=3)
sub_entry.grid(column=1, row=3)

message_label = Label(text="Message:    ", font=FONT, bg=back_ground)
message_label.grid(column=0, row=4)
message_entry = Text(width=30, height=5, font=FONT, bg=back_ground)
message_entry.grid(column=1, row=4)
message_entry.config(highlightcolor="blue", highlightthickness=1)
send = Button(width=10, text="send", font=FONT, bg=back_ground, command=Send)
send.grid(column=1, row=5)

Label = Label(text="", width=15, bg=back_ground)
Label.grid(column=2, row=2)
window.mainloop()
