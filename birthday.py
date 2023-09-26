import smtplib
import random as r
import datetime as dt

back_ground = "lightblue"
EMAIL = "vinaykanuku7565@gmail.com"
PASSWORD = "sbmvdfpedvnpnwof"
with open("quotes.txt", "r") as data:
    quotes = data.readlines()


def send_mail(q):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs="chintapuneeth@gmail.com", msg=f"Subject:Birth day-wish\n\n{q}")


day = dt.datetime.today().date().day
month = dt.datetime.today().date().month
with open("birthdays.csv", "r") as csv:
    csv = csv.readlines()
    for i in csv:
        day_li = int(i.split(",")[2])
        month_li = int(i.split(",")[3])
        if day == day_li and month == month_li:
            with open("letter1.txt", "r") as letters:
                letter = letters.read()
                send = letter.replace("[NAME]", i.split(",")[0])
                send_mail(send)