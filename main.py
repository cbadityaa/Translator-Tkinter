from optparse import Values
from tkinter import *
from tkinter import ttk , messagebox
import googletrans
from googletrans import Translator

root=Tk()
root.title("Translator")
root.geometry("1080x400")
root.resizable(False,False)
root.configure(background="#1E1E1E")

def label_ch():
    c1=combo1.get()
    c2=combo2.get()
    label1.configure(text=c1)
    label2.configure(text=c2)
    root.after(1000,label_ch)

def translate_now():
    txt=txt1.get(1.0,END)
    t1=Translator()
    trans_text=t1.translate(txt,src=combo1.get(),dest=combo2.get())
    trans_text=trans_text.text

    txt2.delete(1.0,END)
    txt2.insert(END,trans_text)



image=PhotoImage(file="logo.png")
root.iconphoto(False,image)

arrowimg=PhotoImage(file="R.png")
image_label=Label(root,image=arrowimg,width=150,bg="#1E1E1E")
image_label.place(x=460,y=150)


language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

#combobox1
combo1=ttk.Combobox(root,values=languageV,font="Robot 14",state="r")
combo1.place(x=110,y=20)
combo1.set("SELECT LANGUAGE")

label1=Label(root,text="SELECT LANGUAGE",font="segoe 30 bold",bg="#2f3333",width=18,bd=5,relief=GROOVE,fg="white")
label1.place(x=10,y=50)

#combobox2
combo2=ttk.Combobox(root,values=languageV,font="Robot 14",state="r")
combo2.place(x=730,y=20)
combo2.set("SELECT LANGUAGE")

label2=Label(root,text="SELECT LANGUAGE",font="segoe 30 bold",bg="#2f3333",width=18,bd=5,relief=GROOVE,fg="white")
label2.place(x=620,y=50)

#frame1
f=Frame(root,bg="#1E1E1E",bd=5)
f.place(x=10,y=118,width=440,height=210)

txt1=Text(f,font="Robote 20",bg="#2E2E2E",relief=GROOVE,wrap=WORD,insertbackground="white",fg="white")
txt1.place(x=0,y=0,width=430,height=200)

scrollbar1=Scrollbar(f)
scrollbar1.pack(side='right',fill='y')

scrollbar1.configure(command=txt1.yview)
txt1.configure(yscrollcommand=scrollbar1.set)

#frame2
f2=Frame(root,bg="#1E1E1E",bd=5)
f2.place(x=620,y=118,width=440,height=210)

txt2=Text(f2,font="Robote 20",bg="#2E2E2E",relief=GROOVE,wrap=WORD,insertbackground="white",fg="white")
txt2.place(x=0,y=0,width=430,height=200)

#test lol
# txt2.tag_add("here","1.0","1.4")
# txt2.tag_config("here",foreground="white")

scrollbar2=Scrollbar(f2)
scrollbar2.pack(side='right',fill='y')

scrollbar2.configure(command=txt2.yview)
txt2.configure(yscrollcommand=scrollbar2.set)


#translatebutton
translate=Button(root,text="Translate",font=("Robot",15),activebackground="white",cursor="hand2",bd=1,width=10,height=2,bg="#2E2E2E",fg="white",command=translate_now)
translate.place(x=476,y=300)



label_ch()


root.mainloop()