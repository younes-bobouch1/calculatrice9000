#importe tous les paquets tkinter
from tkinter import *
from tkinter import messagebox

#from tkinter import simpledialog

"------------------------------------------------------------------------------------------------------------------"
#créer ma fenêtre
gui = Tk()
"------------------------------------------------------------------------------------------------------------------"
#titre
gui.title("Calculator 9000")
"------------------------------------------------------------------------------------------------------------------"
#taille de la fenêtre
gui.geometry("340x580")
"------------------------------------------------------------------------------------------------------------------"
#variable
calcul =""
historique = []
"------------------------------------------------------------------------------------------------------------------"
#mes fonctions
def cala(symbole):
    global calcul
    calcul+=str(symbole)
    resultat.delete(1.0, "end")
    resultat.insert(1.0, calcul)
    historique.append(str(calcul))
"------------------------------------------------------------------------------------------------------------------"
def faire_cala():
    global calcul
    try:
        calcul=str(eval(calcul))
        resultat.delete(1.0, "end")
        resultat.insert(1.0, calcul)

    except:
        del_cala()
        resultat.insert(1.0, "Erreur")
"------------------------------------------------------------------------------------------------------------------"
def del_cala():
    global calcul
    calcul=""
    resultat.delete(1.0, "end")
"------------------------------------------------------------------------------------------------------------------"
def historique_resultat():
    messagebox.showinfo("Historique des résultats", "\n".join(historique))

def delete_histo():
    global historique
    historique.clear()
"------------------------------------------------------------------------------------------------------------------"
#paramètres tkinter
nomApp = Label(gui,text="CALCULATOR 9000",font=("Courier",25,"bold"),fg="black")
nomApp.place(x=20, y=20)

resultat = Text(gui,height=2,width=18,font=("Courier",22,"bold"),bd=5,state='normal')
resultat.place(x=10, y=180)

zero = Button (gui, text='0',command=lambda:cala(0), font=("Courier", 20), width=4, height=1)
zero.place(x=90, y=520)

un = Button (gui, text='1',command=lambda:cala(1), font=("Courier", 20), width=4, height=1)
un.place(x=10, y=460)

deux = Button (gui, text='2',command=lambda:cala(2), font=("Courier", 20), width=4, height=1)
deux.place(x=90, y=460)

trois = Button (gui, text='3',command=lambda:cala(3), font=("Courier", 20), width=4, height=1)
trois.place(x=170, y=460)

quatre = Button (gui, text='4',command=lambda:cala(4), font=("Courier", 20), width=4, height=1)
quatre.place(x=10, y=400)

cinq = Button (gui, text='5',command=lambda:cala(5), font=("Courier", 20), width=4, height=1)
cinq.place(x=90, y=400)

six = Button (gui, text='6',command=lambda:cala(6), font=("Courier", 20), width=4, height=1)
six.place(x=170, y=400)

sept = Button (gui, text='7',command=lambda:cala(7), font=("Courier", 20), width=4, height=1)
sept.place(x=10, y=340)

huit = Button (gui, text='8',command=lambda:cala(8), font=("Courier", 20), width=4, height=1)
huit.place(x=90, y=340)

neuf = Button (gui, text='9',command=lambda:cala(9), font=("Courier", 20), width=4, height=1)
neuf.place(x=170, y=340)

add = Button (gui, text='+',command=lambda:cala("+"), font=("Courier", 20),bg="grey", width=4, height=1)
add.place(x=250, y=460)

sous = Button (gui, text='-',command=lambda:cala("-"), font=("Courier", 20),bg="grey", width=4, height=1)
sous.place(x=250, y=280)

mul = Button (gui, text='x',command=lambda:cala("*"), font=("Courier", 20),bg="grey", width=4, height=1)
mul.place(x=250, y=400)

div = Button (gui, text='/',command=lambda:cala("/"), font=("Courier", 20),bg="grey", width=4, height=1)
div.place(x=250, y=340)

pourc = Button (gui, text='%',command=lambda:cala("%"), font=("Courier", 20),bg="grey", width=4, height=1)
pourc.place(x=10, y=280)

rac = Button (gui, text='√',command=lambda:cala(), font=("Courier", 20),bg="grey", width=4, height=1)
rac.place(x=90, y=280)

dot = Button (gui, text='.',command=lambda:cala("."), font=("Courier", 20),bg="grey", width=4, height=1)
dot.place(x=170, y=520)

eg = Button (gui, text='=',command=faire_cala, font=("Courier", 20), width=4, height=1, bg="#81FFFF")
eg.place(x=250, y=520)

delete = Button (gui, text='C',command=del_cala, font=("Courier", 20),bg="grey", width=4, height=1)
delete.place(x=170, y=280)

boutton_historique = Button(gui,text="HISTORIQUE",font=("Courier",10),command=historique_resultat)
boutton_historique.place(x=10, y=120,height=50,width=150)

del_historique = Button(gui,text="SUPP HISTORIQUE",font=("Courier",11),command=delete_histo)
del_historique.place(x=175, y=120,height=50,width=150)
"------------------------------------------------------------------------------------------------------------------"
#j'appelle ma fenêtre
gui.mainloop()


