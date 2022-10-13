from tkinter import messagebox as MessageBox
from tkinter import *
import psycopg2
NAME = ""
PASSW = ""
TABLE = ""


def sql():
    db = nameE.get()
    pas = password2.get()
    tabla = tabla2.get()

    global NAME;
    global PASSW;
    global TABLE;

    NAME = db
    PASSW = pas
    TABLE = tabla

    nameE.delete(0,'end')
    password2.delete(0,'end')
    tabla2.delete(0,'end')

    try:
        if psycopg2.connect(host = 'localhost',user= 'postgres',password= pas,database = db):

            conn = psycopg2.connect(
                host = 'localhost',
                user = 'postgres',
                password = pas,
                database = db
            )

            cursorD = conn.cursor()

            cursorD.execute("select exists(select * from information_schema.tables where table_name=%s)", (f'{tabla}',))
            if cursorD.fetchone()[0]:
                MessageBox.showinfo("Bien", "Datos correctos")
            else:
                MessageBox.showinfo("about", "La tabla ingresada no fue encontrada")
                nameE.delete(0,'end')
                password2.delete(0,'end')
                tabla2.delete(0,'end')
            conn.close()
    except Exception as exce:
        MessageBox.showinfo("error", "No se conecto")


#Alfabeto que se usa
A = [
'0','1','2','3','4','5','6','7','8','9','=',';',' ',',',"'",
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

#Tabla de transición
TablaT = [
    #UPDATE, update
[1,'U',2],[2,'P',3],[3,'D',4],[4,'A',5],[5,'T',6],[6,'E',7],
[1,'u',2],[2,'p',3],[3,'d',4],[4,'a',5],[5,'t',6],[6,'e',7],
#espacios y simbolos = ' ;
[7,' ', 8],[9,' ',10],[9,'=',13],[9,';',24],[12,' ',26],[13,"'",14],
[15,"'",16],[16,',',17],[17,' ',9],[25,',',17],[16,' ',18],[23,' ',9],
[25,';',27],[25,';',24],[16,';',24],
#mayusculas y minisculas 8-9
[8,'a',9],[8,'b',9],[8,'c',9],[8,'d',9],[8,'e',9],[8,'f',9],[8,'g',9],
[8,'h',9],[8,'i',9],[8,'j',9],[8,'k',9],[8,'l',9],[8,'m',9],[8,'n',9],
[8,'o',9],[8,'p',9],[8,'q',9],[8,'r',9],[8,'s',9],[8,'t',9],[8,'u',9],
[8,'v',9],[8,'w',9],[8,'x',9],[8,'y',9],[8,'z',9],
[8,'A',9],[8,'B',9],[8,'C',9],[8,'D',9],[8,'E',9],[8,'F',9],[8,'G',9],
[8,'H',9],[8,'I',9],[8,'J',9],[8,'K',9],[8,'L',9],[8,'M',9],[8,'N',9],
[8,'O',9],[8,'P',9],[8,'Q',9],[8,'R',9],[8,'S',9],[8,'T',9],[8,'U',9],
[8,'V',9],[8,'W',9],[8,'X',9],[8,'Y',9],[8,'Z',9],
#SET, set
[8,'S',10],[10,'E',11],[11,'T',12],[25,' ',18],
[8,'s',10],[10,'e',11],[11,'t',12],
#mayusculas y minisculas 26-8 
[26,'a',8],[26,'b',8],[26,'c',8],[26,'d',8],[26,'e',8],[26,'f',8],[26,'g',8],
[26,'h',8],[26,'i',8],[26,'j',8],[26,'k',8],[26,'l',8],[26,'m',8],[26,'n',8],
[26,'o',8],[26,'p',8],[26,'q',8],[26,'r',8],[26,'s',8],[26,'t',8],[26,'u',8],
[26,'v',8],[26,'w',8],[26,'x',8],[26,'y',8],[26,'z',8],
[26,'A',8],[26,'B',8],[26,'C',8],[26,'D',8],[26,'E',8],[26,'F',8],[26,'G',8],
[26,'H',8],[26,'I',8],[26,'J',8],[26,'K',8],[26,'L',8],[26,'M',8],[26,'N',8],
[26,'O',8],[26,'P',8],[26,'Q',8],[26,'R',8],[26,'S',8],[26,'T',8],[26,'U',8],
[26,'V',8],[26,'W',8],[26,'X',8],[26,'Y',8],[26,'Z',8],
#mayusculas y minisculas 26-8 
[14,'a',15],[14,'b',15],[14,'c',15],[14,'d',15],[14,'e',15],[14,'f',15],
[14,'f',15],[14,'g',15],[14,'h',15],[14,'i',15],[14,'j',15],[14,'k',15],
[14,'l',15],[14,'m',15],[14,'n',15],[14,'o',15],[14,'p',15],[14,'q',15],
[14,'r',15],[14,'s',15],[14,'t',15],[14,'u',15],[14,'v',15],[14,'w',15],
[14,'x',15],[14,'y',15],[14,'z',15],
[14,'A',15],[14,'B',15],[14,'c',15],[14,'D',15],[14,'E',15],[14,'F',15],
[14,'F',15],[14,'G',15],[14,'H',15],[14,'I',15],[14,'J',15],[14,'K',15],
[14,'L',15],[14,'M',15],[14,'N',15],[14,'O',15],[14,'P',15],[14,'Q',15],
[14,'R',15],[14,'S',15],[14,'T',15],[14,'U',15],[14,'V',15],[14,'W',15],
[14,'X',15],[14,'Y',15],[14,'Z',15],
#Numeros del 0 al 9
[13,'0',25],[13,'1',25],[13,'2',25],[13,'3',25],[13,'4',25],[13,'5',25],
[13,'6',25],[13,'7',25],[13,'8',25],[13,'9',25],
#WHERE, where
[18,'W',19],[19,'H',20],[20,'E',21],[21,'R',22],[22,'E',23],
[18,'w',19],[19,'h',20],[20,'e',21],[21,'r',22],[22,'e',23]]


def validar():
    salida = True
    #Estados a comparar
    TablaC = []
    #Final
    EF = [24,27]
    #Inicio
    E = 1
    #Actual
    EA = E
   
    validos = []
    invalidos = []

    CE = sent2.get()

    for c in CE:
    #Verificar
    
        if c in A:
        
            for f in TablaT:
           
                if c in f and EA in f:
                #Tabla final
                    TablaC.append([EA,c,f[2]])
                    EA = f[2]
                    validos.append(c)
        else:
            invalidos.append(c)
            salida = False
    #Pasa o nel
    if (EA in EF) and (salida == True):

        return True
      
    else:
        return False


def ver ():

    mostrar = validar()
    tex = sent2.get()

    try:
        conn = psycopg2.connect(
                host = 'localhost',
                user = 'postgres',
                password = PASSW,
                database = NAME
            )
        if mostrar: 
            try:
                cone = conn.cursor()

                print(tex)
                cone.execute(tex)        
                #pruebas = cone.fetchone()              
                MessageBox.showinfo("bien","Sentencia se valida y tiene consistendia")
            except psycopg2.Error as e:                
                MessageBox.showinfo("mal","Sentencia valida pero sin consistencia a la base de datos")    
            finally:
                conn.close()
        else:
            MessageBox.showinfo("error","Sentencia invalida")

    except Exception as ex:
        pass
    finally:
        sent2.delete(0,'end')
        conn.close()


#Vista
root = Tk()
root.title("Automatas")
root.geometry("800x400")
root.config(background="Medium purple")

name = Label(root, text="DBName:", background="Salmon")
name.place(x=60, y=40,height=25,width=80)

nameE = Entry(root,)
nameE.place(x=150, y=40,height=25,width=220)

password1 = Label(root, text="Password:", background="Salmon")
password1.place(x=450, y=40,height=25,width=80)

password2 = Entry(root, )
password2.place(x=540, y=40,height=25,width=220)

tabla = Label(root, text="Nombre de la tabla:", background="Salmon")
tabla.place(x=245, y=100, height=25, width=120)

tabla2 = Entry(root, )
tabla2.place(x=375, y=100, height=25, width=220)


boton = Button(root,text="Enviar",background="green",command=sql)
boton.place(x=370, y=150, height=30, width=80)


sent = Label(root, text="Ingrese la Sentencia: ",background="Salmon")
sent.place(x=235, y=250, height=25, width=120)

sent2 = Entry(root)
sent2.place(x=370, y=250,height=25,width=220)

boton2 = Button(root,text="Validar", background="green",command= ver)
boton2.place(x=370,y=300,height=25,width=90)

root.mainloop()
