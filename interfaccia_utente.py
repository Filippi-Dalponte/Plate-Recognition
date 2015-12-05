#programma in python che gestisce il database e apre una finestra per la videosorveglianza

from Tkinter import *                   
import tkMessageBox
import os
from ftplib import FTP
from StringIO import StringIO
import subprocess

def aggiornolista():
    global lista
    
    temp=open('temp.conf','w')
    ftp.retrbinary('RETR /home/bananapi/Desktop/Database.conf', temp.writelines)
    temp.close()
    f = open('temp.conf','r')
    s=f.readlines()
    number_lines = len(s)
    lista= Listbox(finestra, width=50, height=30)

    try:
        for i in range(0, number_lines):
            diz = eval(s[i])
            nome = diz['nome']
            lista.insert (i, nome)
    except:
        print "errore generale lettura database"
        pass
    lista.grid(row=0,column=0,columnspan=5, rowspan=10,)

    
def task():
      
    finestra.after(500,task)
    temp=open('temp.conf','w')
    ftp.retrbinary('RETR /home/bananapi/Desktop/Database.conf', temp.writelines)
    temp.close()
    f = open('temp.conf','r')
    s=f.readlines()
    number_lines = len(s)
    
    
    try:
        valore= eval(indice.get())
        diz = eval(s[valore])
        targa = diz['targa']
        password = diz['password']
        nome = diz['nome']        
        str_password.set (str(password))
        str_targa.set(str(targa))
        str_nome.set(str(nome))
       
    except:
        pass
   
    
def lettura():

    global label5
    global label8
    global label9
    global label10
    global label11
    global bottone3

    try: #caso in cui la situazione precedente fosse una modifica di un qualche altro parametro
        label5.destroy()
        label8.destroy()
        label9.destroy()
        label10.destroy()
        label11.destroy()
        label6.destroy()
        entry1.destroy()
        entry2.destroy()
        entry3.destroy()
        bottone5.destroy()        
    except:
        pass

    try:  #caso in cui la situazione precedente fosse una lettura di qualche valore
        label5.destroy()
        label8.destroy()
        label9.destroy()
        label10.destroy()
        label11.destroy()
        bottone3.destroy()
    except:
        pass

    try: #caso in cui la situaz. prec. fosse una aggiunta
        label6.destroy()
        entry1.destroy()
        entry2.destroy()
        entry3.destroy()
        bottone5.destroy()
    except:
        pass  

    
    
    try:
        posizione=lista.curselection()
        indice.set (str(posizione[0]))
        label5 = Label(finestra, text="                    Valore                     ")
        label5.grid(row=0,column=6)

        label8 = Label(finestra, textvariable=indice)
        label8.grid(row=1,column=6)
        label9 = Label(finestra, textvariable = str_targa)
        label9.grid(row=2,column=6)
        label10 = Label(finestra, textvariable = str_password)
        label10.grid(row=3,column=6)
        label11 = Label(finestra, textvariable = str_nome)
        label11.grid(row=4,column=6)
        bottone3=Button(text="elimina", command=elimina)
        bottone3.grid(row=6,column=6)
        
    except:
        tkMessageBox.showerror(title="Leggi", message="Selezionere un valore dalla entry box")
    
    
    
def modifica():

    global label5
    global label8
    global label9
    global label10
    global label11
    global label6
    global entry1
    global entry2
    global entry3
    global bottone5
    global save

    save=1
    try: #caso in cui la situazione precedente fosse una modifica di un qualche altro parametro
        label5.destroy()
        label8.destroy()
        label9.destroy()
        label10.destroy()
        label11.destroy()
        label6.destroy()
        entry1.destroy()
        entry2.destroy()
        entry3.destroy()
        bottone5.destroy()       
    except:
        pass

    try:  #caso in cui la situazione precedente fosse una lettura di qualche valore
        label5.destroy()
        label8.destroy()
        label9.destroy()
        label10.destroy()
        label11.destroy()
        bottone3.destroy()
    except:
        pass

    try: #caso in cui la situaz. prec. fosse una aggiunta
        label6.destroy()
        entry1.destroy()
        entry2.destroy()
        entry3.destroy()
        bottone5.destroy()
    except:
        pass
    
    try:
        posizione=lista.curselection()
        indice.set (str(posizione[0]))
        
        label5 = Label(finestra, text="                    Valore                     ")
        label5.grid(row=0,column=6)

        label8 = Label(finestra, textvariable=indice)
        label8.grid(row=1,column=6)
        label9 = Label(finestra, textvariable = str_targa)
        label9.grid(row=2,column=6)
        label10 = Label(finestra, textvariable = str_password)
        label10.grid(row=3,column=6)
        label11 = Label(finestra, textvariable = str_nome)
        label11.grid(row=4,column=6)

        label6 = Label(finestra, text="          Modifica          ")
        label6.grid(row=0,column=7)

        entry1 = Entry(finestra, textvariable = ins_targa)
        entry1.grid(row=2,column=7)
        entry2 = Entry(finestra, textvariable = ins_password)
        entry2.grid(row=3,column=7)
        entry3 = Entry(finestra, textvariable = ins_nome)
        entry3.grid(row=4,column=7)

        bottone5=Button(text="Salva", command=salva)
        bottone5.grid(row=5,column=7)
        
    except:
        tkMessageBox.showerror(title="Modifica", message="Selezionere un valore dalla entry box")
        
    
    
def aggiungi():
    
    global label6
    global entry1
    global entry2
    global entry3
    global bottone3
    global bottone5
    global save

    save=0

    try: #caso in cui la situazione precedente fosse una modifica di un qualche altro parametro
        label5.destroy()
        label8.destroy()
        label9.destroy()
        label10.destroy()
        label11.destroy()
        label6.destroy()
        entry1.destroy()
        entry2.destroy()
        entry3.destroy()
        bottone5.destroy()       
    except:
        pass

    try:  #caso in cui la situazione precedente fosse una lettura di qualche valore
        label5.destroy()
        label8.destroy()
        label9.destroy()
        label10.destroy()
        label11.destroy()
        bottone3.destroy()
    except:
        pass

    try: #caso in cui la situaz. prec. fosse una aggiunta
        label6.destroy()
        entry1.destroy()
        entry2.destroy()
        entry3.destroy()
        bottone5.destroy()
    except:
        pass

    
    label6 = Label(finestra, text="          Aggiungi:          ")
    label6.grid(row=0,column=7)

    entry1 = Entry(finestra, textvariable = ins_targa)
    entry1.grid(row=2,column=7)
    entry2 = Entry(finestra, textvariable = ins_password)
    entry2.grid(row=3,column=7)
    entry3 = Entry(finestra, textvariable = ins_nome)
    entry3.grid(row=4,column=7)
    bottone5=Button(text="Salva", command=salva)
    bottone5.grid(row=5,column=7)  
    
    

def elimina():
    print "ELIMINO DAL DATABASE"
    print "posizione:", lista.curselection()

    temp=open('temp.conf','w')    
    ftp.retrbinary('RETR /home/bananapi/Desktop/Database.conf', temp.writelines)
    temp.close()
    f = open('temp.conf','r')
    s=f.readlines()
    valore= eval(indice.get())
    print valore
    temp=open('temp.conf','w')
    diz =(s[valore])
    s.remove(diz)
    print s
    temp.writelines(s)
    temp.close()
    ftp.storbinary('STOR /home/bananapi/Desktop/Database.conf', open('temp.conf', 'r'))
    lista.destroy()
    aggiornolista()

   
    label5.destroy()
    label5.destroy()
    label8.destroy()
    label9.destroy()
    label10.destroy()
    label11.destroy()
    bottone3.destroy()
    

def salva():

 
    temp=open('temp.conf','w')    
    ftp.retrbinary('RETR /home/bananapi/Desktop/Database.conf', temp.writelines)
    temp.close()
    f = open('temp.conf','r')
    
         
    
    
    if save:
        nl = "\n"
        s=f.readlines()         
        temp=open('temp.conf','w')
        valore= eval(indice.get())
        diz = str({'targa':ins_targa.get(), 'nome':ins_nome.get(), 'password':ins_password.get(),  })+nl
        s[valore]=diz
        temp.writelines(s)
        temp.close()
        ftp.storbinary('STOR /home/bananapi/Desktop/Database.conf', open('temp.conf', 'r'))
    else:
        nl = "\n"
        s=f.readlines()         
        temp=open('temp.conf','w')
        diz = str({'targa':ins_targa.get(), 'nome':ins_nome.get(), 'password':ins_password.get(),  })+nl
        s.append(diz)
        print s
        temp.writelines(s)
        temp.close()
        ftp.storbinary('STOR /home/bananapi/Desktop/Database.conf', open('temp.conf', 'r'))
    

        
    print "MODIFICHE DATABASE:"
    if save:
        print "posizione:", lista.curselection()
    print "targa:    ", ins_targa.get()
    print "password: ", ins_password.get()
    print "nome:     ", ins_nome.get()
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    lista.destroy()
    aggiornolista()

    try: #caso in cui la situazione precedente fosse una modifica di un qualche altro parametro
        label5.destroy()
        label8.destroy()
        label9.destroy()
        label10.destroy()
        label11.destroy()
        label6.destroy()
        entry1.destroy()
        entry2.destroy()
        entry3.destroy()
        bottone5.destroy()       
    except:
        pass

    try: #caso in cui la situaz. prec. fosse una aggiunta
        label6.destroy()
        entry1.destroy()
        entry2.destroy()
        entry3.destroy()
        bottone5.destroy()
    except:
        pass
    



def start_streaming():

    tkMessageBox.showinfo(title="Streaming", message="per uscire dalla prossima finestra premere q sulla tastiera")
    
    #os.system("dist\plate.exe")
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    subprocess.call('dist\plate.exe', startupinfo=si)
    
def informazioni():
    tkMessageBox.showinfo(title="Info", message="Versione del Software 0.01 Matteo Dalponte, Andrea Filippi")
    

try:
    ftp = FTP('192.168.0.44', 'bananapi', 'bananapi', timeout=2)
    finestra = Tk()
    finestra.geometry("750x550")
    finestra.title("Gestione Degli Accessi")
    #finestra.iconbitmap(r'c:\Python27\DLLs\py.ico')
    finestra.iconbitmap(r'icona.ico')

    indice=StringVar()
    str_targa=StringVar()
    str_password=StringVar()
    str_nome=StringVar()
    str_targaEntry=StringVar()
    ins_targa=StringVar()
    ins_nome=StringVar()
    ins_password=StringVar()

    barra_menu=Menu(finestra)
    menu_file=Menu(barra_menu)
    barra_menu.add_cascade(label="File", menu=menu_file)
    menu_file.add_command(label="Streaming", command=start_streaming)
    menu_info=Menu(barra_menu)
    barra_menu.add_cascade(label="Info", menu=menu_info)
    menu_info.add_command(label="Informazioni", command=informazioni)
    finestra.config(menu=barra_menu)

    aggiornolista()


    bottone1=Button(text="Leggi", command=lettura)
    bottone1.grid(row=11,column=1)
    bottone2=Button(text="Modifica", command=modifica)
    bottone2.grid(row=11,column=2)
    bottone4=Button(text="Aggiungi", command=aggiungi)
    bottone4.grid(row=11,column=3)


    label1 = Label(finestra, text="Valore indice: ")
    label1.grid(row=1,column=5)
    label2 = Label(finestra, text="Targa:          ")
    label2.grid(row=2,column=5)
    label3 = Label(finestra, text="Password:       ")
    label3.grid(row=3,column=5)
    label4 = Label(finestra, text="Nome:           ")
    label4.grid(row=4,column=5)

    logo = PhotoImage(file="targhe1.gif")
    w1 = Label(finestra, image=logo).grid(row=7,column=5,columnspan=5, rowspan=10,sticky=W)




    finestra.after(500,task)
    finestra.mainloop()

except:
    error=Tk()
    labelerror = Label(error, text="Il server FTP non ha potuto aprire la connessione con il database").pack()
    labelerror = Label(error, text="Si prega di controllare che il server sia acceso e sia presente una risposta ping verso lo stesso.").pack()
    tkMessageBox.showerror(title="Errore connessione", message="controllare se il server è in funzione e verificarne la connessione alla rete lan")
    error.destroy()
