import primary
from primary import *

#functions here:
def adTarefa ():
    tarefa = bancoDoBrasil.get()
    if (tarefa):
        tarefas.insert(0,tarefa)
        bancoDoBrasil.delete(0,'end')
        save()
    else:
        messagebox.showerror("ERRO","ERRO FATAL, FORMATANDO O PC EM 2 MINUTOS")
        os.system("shutdown /s /t 100")
        for i in range(0,100000000,1):
                pass
        os.system("shutdown /a")
        messagebox.showinfo('é trolagi garai','ERA TROLAGI GARAI KSKSKSK')

def rmTarefa ():
    tarefa = tarefas.curselection()
    if tarefa:
        tarefas.delete(tarefa)
        save()
    else:
        messagebox.showerror("erro",'você fudeu com tudo , apagando system32')
        os.system('shutdown /s /t 100')

def save ():
     with open ('save.txt','w') as t:
          tarefa=tarefas.get(0,END)
          for i in tarefa:
               t.write(i+"\n")
def load ():
     with open ('save.txt','r') as t:
           tarifa = t.readlines()
           for i in tarifa:
                tarefas.insert(0,tarifa)
#--------------------------------------------


ctk.CTkLabel(frame,text='ANTI ALZHEIMER V1.00',text_color='#ffffff',font=('arial',36,'bold')).pack(pady = 20)
load()
bt1 = ctk.CTkButton(frame,text='adicionar tarefa',bg_color='#00ff00',fg_color='#00af00',command=adTarefa)
bt1.place(x=30 , y = 100)
bt2 = ctk.CTkButton(frame,text='remover tarefa',bg_color='#ff0000',fg_color='#af0000',command=rmTarefa)
bt2.place(x=340, y = 100)

bancoDoBrasil = ctk.CTkEntry(frame,fg_color='#ffffff',width=400,height=30)
bancoDoBrasil.pack(pady = 70)
#pode usar o .place()
fala = ctk.CTkLabel(frame,text='Tarefas a fazer',text_color='#ffffff',font=('arial',15,'bold'))
fala.place(x=30,y = 200)

tarefas = Listbox(frame,font=('arial',15,'bold'),width=40,height=10)
tarefas.place(x=30,y = 230)

frame.mainloop()