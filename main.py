import random
import pandas as pd
from tkinter import *

window = Tk()
window.title("Calculator")
window.minsize(width=250, height=280)
window.config(padx=20, pady=20)
window.resizable(0,0)

#I prepared an English-Turkish dictionary in Excel
#We read the Excel file and convert it into a dictionary
#specify the file path
path = "specify the file path"
read = pd.read_excel(path)
ing = list(read.ing)
tr = list(read.tr)
dic = dict(zip(ing, tr))

def data():
    global soru
    global answers
    global cevap

    #We choose a random question from the dictionary
    liste = random.choices(list(dic.items()))
    cevap = liste[0][0]
    soru = liste[0][1]

    #We randomly choose three answers from the dictionary
    list_cevap = list(cevap.split(" "))
    rdb1 = random.choices(list(dic.keys()))
    rdb2 = random.choices(list(dic.keys()))
    rdb3 = random.choices(list(dic.keys()))

    #We mix the 4 answers we chose
    answers = (list_cevap + rdb1 + rdb2 + rdb3)
    random.shuffle(answers)

count1 = 0
count2 = 0
def start():
    data()

    global word
    global question


    button.config(state=DISABLED)
    label.config(text="")
    label2.config(text="")
    label3.config(text="")


    def result():
        global count1
        global count2

        a = str(radio.get())

        if a == cevap:
            button.config(state=NORMAL)
            label.config(text="Correct.", font=("Ariel", 10, "bold"))
            label3.config(text="{} = {}".format(soru, cevap), font=("Ariel", 10, "bold"), fg="blue")
            word.destroy()
            question.destroy()
            rad_but1.destroy()
            rad_but2.destroy()
            rad_but3.destroy()
            rad_but4.destroy()
            count1 += 1
            label_count1.config(text="Correct={}".format(count1), font=("Ariel", 10, "bold"), fg="blue")
        else:
            button.config(state=NORMAL)
            label.config(text="Wrong!", font=("Ariel", 10, "bold"))
            label2.config(text="{} = {}".format(soru, cevap), font=("Ariel", 10, "bold"), fg="red")
            word.destroy()
            question.destroy()
            rad_but1.destroy()
            rad_but2.destroy()
            rad_but3.destroy()
            rad_but4.destroy()
            count2 += 1
            label_count2.config(text="Wrong={}".format(count2), font=("Ariel", 10, "bold"), fg="red")

    word = Label(text=soru, font=("Ariel", 10, "bold"), fg="red")
    word.pack()
    question = Label(text="Kelimenin ingilizce karşılığı nedir?")
    question.pack()
    radio = StringVar(value=1)
    rad_but1 =Radiobutton(text=answers[0], variable=radio, value=answers[0], command=result)
    rad_but1.pack()
    rad_but2 =Radiobutton(text=answers[1], variable=radio, value=answers[1], command=result)
    rad_but2.pack()
    rad_but3 =Radiobutton(text=answers[2], variable=radio, value=answers[2], command=result)
    rad_but3.pack()
    rad_but4 =Radiobutton(text=answers[3], variable=radio, value=answers[3], command=result)
    rad_but4.pack()


button = Button(text="Start", command=start, font=("Ariel", 10, "bold"))
button.pack()

label = Label()
label.pack()

label2 = Label()
label2.pack()

label3 = Label()
label3.pack()

label_count1 = Label()
label_count1.place(x=150, y=-3)
label_count2 = Label()
label_count2.place(x=150, y=20)

window.mainloop()
