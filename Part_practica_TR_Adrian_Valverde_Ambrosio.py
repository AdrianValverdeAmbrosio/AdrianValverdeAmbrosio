# Import llibreria per a la base de dades 
import sqlite3

# Import llibreries per a la GUI
# Llibreria per a la creació de la GUI
import tkinter as tk
from tkinter import *
# Llibreria per a millorar l'estètica de la GUI 
import customtkinter
# Llibreria per a l'aparició de missatges d'error
from tkinter import messagebox
# Llibreria per a la possibilitat de modificar les fonts
from tkinter.font import Font

# Connexió a la base de dades de l'arxiu anomenat "BaseDeDades" que està creat amb l'arxiu "Base De Dades Part Pràctica.py"
basededades=sqlite3.connect("BaseDeDades")
# Mètode per a fer possible les operacions amb la base de dades
connexio=basededades.cursor()

# Creació de la informació que sortirà en tots els cercadors
# Seleccionem la taula que volem seleccionar, en aquest cas amb l'informació dels alumnes que sortirà en el cercador d'alumnes
connexio.execute("SELECT * FROM INFORMACIO")
# Apliquem la informació seleccionada a la variable anomenada "informacio"
informacio=connexio.fetchall()
b1=" "
# Hem de crear un bucle que ho repeteixi per a cada alumne (Cada fila anomenada "persona") dins de la taula dels alumnes ("informacio")
for persona in informacio:
    # Seleccionem el identificador de la persona, persona[0] significa la primera columna i l'assignem a la variable "ident7"
    ident7=persona[0]
    # Seleccionem el nom de l'alumne, persona[1] significa la segona columna i l'assignem a la variable "nom7"
    nom7=persona[1]
    # Seleccionem el primer cognom de l'alumne, persona[2] significa la tercera columna i l'assignem a la variable "primer_cognom7"
    prmer_cognom7=persona[2]
    # Seleccionem el segon cognom de l'alumne, persona[3] significa la quarta columna i l'assignem a la variable "segon_cognom7"
    segon_cognom7=persona[3]
    # Creem la frase que sortirà per a cada alumne, Identificador + el nom complet de la persona i l'assignem a la variable "a1" 
    a1="Identificador: " + str(ident7) +" Nom: "+ " " + nom7 + " " + prmer_cognom7 + " " + segon_cognom7
    # Creem l'espai entre les frases
    b1=str(b1) + "\n" + a1 + "\n"
    # Posem la frase en mode string, és a dir, com a text
    c1=str(b1)

# Repetim el procés però ara amb l'informació dels professors
connexio.execute("SELECT * FROM INFORMACIO2")
informacio2=connexio.fetchall()
# Informació professors
b2=" "
for persona in informacio2:
    ident8=persona[0]
    nom8=persona[1]
    prmer_cognom8=persona[2]
    segon_cognom8=persona[3]
    a2="Identificador: " + str(ident8) +" Nom: "+ " " + nom8 + " " + prmer_cognom8 + " " + segon_cognom8
    b2=str(b2) + "\n" + a2 + "\n"
    c2=str(b2)

# Repetim el procés però ara amb l'informació dels TRs
connexio.execute("SELECT * FROM INFORMACIO3")
informacio3=connexio.fetchall()
# Informació TRs
b3=" "
for persona in informacio3:
    ident9=persona[0]
    nom9=persona[2]
    a3="Identificador: " + str(ident9) +" Nom: "+ " " + nom9
    b3=str(b3) + "\n" + a3 + "\n"
    c3=str(b3)

### Començem amb la creació de la GUI de l'aplicació ###

## Primer de tot vull explicar l'estructura que tindrà l'app
## L'app començarà amb l'utilització de la funció "finestra1", que serà la finestra principal del programa, aquesta trucada a la funció ha d'estar a sota del tot del programa per a què es puguin llegir
# totes les funcions i poder-les utilitzar.
## Començem amb la primer funció que és la creació de la primer GUI que es veurà. Dins d'aquest tindrà 4 botons, un per a tancar el programa, un per anar a la finestra d'alumnes, altre de professors i de TRs.
## Al entrar al apartat d'alumnes, hi ha un cercador on quan busquem s'activa la funció "identalumnes" on farà un filtratge, en cas de que l'identificador estigui bè pasarem a la funció "cercaalumnes"
# on es farà el filtratge de tota la informació de l'alumne, on hi haurà un botó amb el nom del tutor. Al donar-li s'executarà la funció "alumneprofessor,2o3", on asignarà l'identificador del professor i
# seguidament, s'executarà la funció "finestraalumnesprofessors", que simplement crea la finestra de cercador de professors i la torna a tancar per a què en cas de que la persona vulgui anar al cercador
# de professors no surti buida. Ja creada i tancada, s'executa la fuinció de "cercaprofessors" on surt la informació filtrada del professor.
## Si prenem el segon botó,s'executa el cercador dels professors(funció finestraprofessors), d'aquí al cercar, pasem a la funció "identprofessors", que decideix si està bé l'dentificador i pasa a la funció
# "cercaprofessors" on es veu l'informació filtrada. Aquí podem veure entre 1 i 3 botons sobre els 3 alumnes que el professor farà de tribunal. Depenent qui botó donem, farà la funció "professoralumne 1,2,3"
# per aconseguir l'dentificador de l'alumne seleccionat i s'activa la funció "finestratrsalumnes" que fa la mateixa funció que "finestraalumnesprofessors" però amb l'alumne. AL fer aquesta acció s'activa
# la funció "cercaalumnes"
## Per últim, trobem l'últim botó on s'executa la funció "finestratrs", que segueix la mateixa metodologia que els altres dos però té un botó que el relaciona amb l'alumne mitjançant les funcions "trsnom" i
# "finestratrsalumnes".


# Assignem el color verd i el tema amb colors clars al programa
customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("light")

# Funció de la finestra principal
def finestra1():
    
    # Creació de la primera finestra
    # Asignem la variable finestra1 (nom de la finestra) com a global
    global finestra1
    finestra1=customtkinter.CTk()
    # Assignem les medides de la finestra
    finestra1.geometry('550x700')
    # Assignem el títol de la finestra
    finestra1.title("Finestra Principal")
    # Assignem l'icona de la finestra
    finestra1.iconbitmap('iesmartidot.ico')
    
    # Funció per a tancar el programa a partir de la 1 finestra
    def tancarprograma1():
        finestra1.destroy()
        quit()

    # Creació dels botons de la primera finestra
    # Botó per a tancar el programa a partir de la 1 finestra
    # Assignem les característiques del botó
        # Possem finestra1 perquè és la finestra a la que el vokmen assignar
        # Possem el text del botó que en aquesta ocasió és Tancar
        # El command és la funció que volem utilitzar, en aquest cas és la de tancar l'app
        # El height és l'altura del botó
        # El width és l'amplada del botó
    bototancarprograma1=customtkinter.CTkButton(finestra1,text="Tancar",command=tancarprograma1, height = 30, width = 110)
    # Empaquetem el botó i el coloquem
        # El row significa la fila que estarà, ja que divideixo la finestra en diferents files i columnes, aquest estarà a la fila 3
        # El column significa a quina columna està asignada, en aquesta ocasió en la 0
        # El padx significa a cuants pixels està separat per l'esquerra i la dreta de les vores
        # El pady significa a cuants pixels està separat d'adalt y d'abaix de les voreres
        # El sticky significa a quin costat estarà dins del recuadre assignat. Es divideix en n (nord), s (sud), e (est), w (oest). Aquí està al sud est, és a dir, abaix a la dreta.
    bototancarprograma1.grid(row=3, column=0, padx=40, pady=110, sticky="se")

    # Botó per a accedir a la funció de la creació de la finestra del cercador d'alumnes
    botoalumnes=customtkinter.CTkButton(finestra1,text="Alumnes",command=finestraalumnes, height = 40, width = 160)
    botoalumnes.grid(row=0, column=0, padx=200, pady=70)

    # Botó per a accedir a la funció de la creació de la finestra del cercador de professors
    botoprofessors=customtkinter.CTkButton(finestra1,text="Professors",command=finestraprofessors, height = 40, width = 160)
    botoprofessors.grid(row=1, column=0, padx=0, pady=0)

    # Botó per a accedir a la funció de la creació de la finestra del cercador de TRs
    bototrs=customtkinter.CTkButton(finestra1,text="Treballs de recerca",command=finestratrs, height = 40, width = 160)
    bototrs.grid(row=2, column=0, padx=0, pady=70, sticky="n")

    #Etiqueta amb el nom del creador
    etiquetanom=customtkinter.CTkLabel(finestra1, text= "Adrián Valverde Ambrosio", height = 1, width = 20)
    etiquetanom.grid(row=4, column=0, padx=40, pady=0, sticky="nw")

    # El mainloop fa que el programa no es tanqui i esperi a rebre indicacions de l'usuari
    finestra1.mainloop()


# Funció que s'activa al pulsar el botó d'alumnes
def finestraalumnes():
    
    # Tancar la 1 finestra
    finestra1.withdraw()
    # Assignem l'dentificador que possarem com a global per poder utilitzar-lo en altres funcions
    global identificadorescollita_alumne
    # Crear variable tipus String que anirà variant cada vegada que s'utilitzi el cercador
    identificadorescollita_alumne=tk.StringVar()
    # Crear una nova finestra per a la creació de la del cercador dels alumnes
    # Assignem la finestra com a global per a poder utilitzar-lo en altres funcions
    global finestraalumnes
    finestraalumnes=customtkinter.CTkToplevel()
    finestraalumnes.geometry('550x700')
    finestraalumnes.title("Cercador d'Alumnes")
    finestraalumnes.iconbitmap('iesmartidot.ico')
    # Crear un tipus de font per a la lletra utilitzada
    font1 = Font(family="Arial", size=12)
    # Creació d'un Widget de text
    textalumnes=tk.Text(finestraalumnes, font=font1, width=57)
    # Posar propietats al Widget de text
    textalumnes.grid(row=0, column=0, sticky='e', padx=5)
    # Insertar el text aconseguit a la línea 22
    textalumnes.insert(tk.END,c1)
    # Deshabilitem l'opció d'editar el text
    textalumnes['state'] = 'disabled'
    # Creació de Scrollbar vertical i configuració d'aquest
    # Amb el command posem el yview(verticalment) del text
    scrollbar1 = customtkinter.CTkScrollbar(finestraalumnes, command=textalumnes.yview)
    scrollbar1.grid(row=0, column=1, sticky='ns', padx=5)
    # Assignem el command
    textalumnes.config(yscrollcommand=scrollbar1.set)

    # Funció tornar a la 1 finestra
    def tornarventanaalumne():
        # Tornar a obrir la 1 finestra
        finestra1.deiconify()
        # Tancar la finestra del cercador dels alumnes
        finestraalumnes.withdraw()

    # Assignem tots els widgets d'aquesta finestra
        # Configurem l'entry
            # Justifiquem el text introduït al entry a l'esquerra
            # Assignem l'escrit com a la variable "identificadorescollita_alumne"
    entry1=customtkinter.CTkEntry(finestraalumnes,justify=tk.LEFT, width = 57, textvariable=identificadorescollita_alumne, text_font='Arial 12')
    entry1.grid(row=1, column=0, padx=0, pady=0, sticky="")    
    botocercaalumnes=customtkinter.CTkButton(finestraalumnes,text="Cercar",command=identalumnes, height = 8, width = 26, text_font='Arial 12')
    botocercaalumnes.grid(row=1, column=0, padx=0, pady=0, sticky="e") 
    bototornar1=customtkinter.CTkButton(finestraalumnes,text="Tornar",command=tornarventanaalumne, height = 30, width = 60, text_font='Arial 12')
    bototornar1.grid(row=2, column=0, pady=160, sticky="e")
    etiqueta1=customtkinter.CTkLabel(finestraalumnes, text= "Escriu l'identificador:", height = 1, width = 20, text_font='Arial 12')    
    etiqueta1.grid(row=1, column=0, padx=50, pady=20, sticky="w")
    
    finestraalumnes.mainloop()



#Error identificador d'alumnes
def identalumnes():
    # Utiltzar les dues variables com a global
    global identificadorescollita_alumne
    global identificadorescollit_alumne
    # Agafar el entry possat i passar-lo a Integer amb el .get
    identificadorescollit_alumne=identificadorescollita_alumne.get()
    # Fem la recerca per a comprobar que existeix un alumne amb un valor a la columne del tema del TR, en cas que no existeixi, ens darà None
    connexio.execute("SELECT Tema FROM INFORMACIO WHERE Ident = ?",(identificadorescollit_alumne,))
    # Assignem a la variable temaalumne el resultat de la recerca
    temaalumne = connexio.fetchone()
    # Passem a String el resultat, és a dir, com a text
    temaalumnef = str(temaalumne)
    # Fem el filtratge si existeix o no
    # Si la variable és diferent a None:
    if temaalumne!=None:
        # Tanquem la finestra
        finestraalumnes.withdraw()
        # Executem la funció per a donar la informació filtrada de l'alumne
        cercaalumnes()
    # Si la variable és None:
    else:
        # Surti un text amb el missatge d'error i que doni l'opció de tornar a possar l'identificador
        messagebox.showwarning("Warning", "Selecciona un identificador correcte")


# Funció amb la informació filtrada de l'alumne        
def cercaalumnes():
    global finestracercaalumnes1
    finestracercaalumnes1=customtkinter.CTkToplevel()
    finestracercaalumnes1.geometry('550x700')
    finestracercaalumnes1.title("Informació Filtrada de l'Alumne")
    finestracercaalumnes1.iconbitmap('iesmartidot.ico')

    # Dins de la finestra del filtre realitzat, una funció per a tornar a la finestra del cercador d'alumnes    
    def tornarventanacercaralumne():
        finestraalumnes.deiconify()
        finestracercaalumnes1.withdraw()
    # Filtrem l'informació de l'alumne
    connexio.execute("SELECT Nom FROM INFORMACIO WHERE Ident = ?",(identificadorescollit_alumne,))
    nom = connexio.fetchall()
    nomf = str(nom)
    connexio.execute("SELECT Primer_Cognom FROM INFORMACIO WHERE Ident = ?",(identificadorescollit_alumne,))
    primer_cognom = connexio.fetchall() 
    primer_cognomf = str(primer_cognom)
    connexio.execute("SELECT Segon_Cognom FROM INFORMACIO WHERE Ident = ?",(identificadorescollit_alumne,))
    segon_cognom = connexio.fetchall()
    segon_cognomf = str(segon_cognom)

    
    connexio.execute("SELECT Hora FROM INFORMACIO WHERE Ident = ?",(identificadorescollit_alumne,))
    hora = connexio.fetchall()
    horaf = str(hora)
    hora = horaf[3:-4]
    if hora!="":
        pass
    else:
        hora=None 
    if hora!=None:
        connexio.execute("SELECT Data FROM INFORMACIO WHERE Ident = ?",(identificadorescollit_alumne,))
        data = connexio.fetchall()
        dataf = str(data)
        connexio.execute("SELECT Nom FROM INFORMACIO3 WHERE Ident = ?",(identificadorescollit_alumne,))
        tema = connexio.fetchall()
        temaf = str(tema)
        connexio.execute("SELECT Aula FROM INFORMACIO WHERE Ident = ?",(identificadorescollit_alumne,))
        aula = connexio.fetchall()
        aulaf = str(aula)
        etiquetadata1=customtkinter.CTkLabel(finestracercaalumnes1, text= "Data i lloc: ", height = 1, width = 20, text_font='Arial 10')
        etiquetadata1.grid(row=2, column=0, padx=10, pady=0, sticky="w")
        etiquetadata1def=customtkinter.CTkLabel(finestracercaalumnes1, text= hora + " el dia " + dataf[3:-4] + " a l'aula " + aulaf[3:-4], height = 1, width = 20, text_font='Arial 10')
        etiquetadata1def.grid(row=2, column=1, padx=50, pady=20, sticky="w")
        etiquetatr1=customtkinter.CTkLabel(finestracercaalumnes1, text= "Tema TR: ", height = 1, width = 20, text_font='Arial 10')
        etiquetatr1.grid(row=1, column=0, padx=10, pady=0, sticky="w")
        etiquetatr1def=customtkinter.CTkLabel(finestracercaalumnes1, text= temaf[3:-4], height = 1, width = 20, text_font='Arial 10', wraplengt=320, justify=tk.LEFT)
        etiquetatr1def.grid(row=1, column=1, padx=50, pady=20, sticky="w")        
        connexio.execute("SELECT Tutor FROM INFORMACIO WHERE Ident = ?",(identificadorescollit_alumne,))
        tutorf = connexio.fetchall()
        tutor = str(tutorf)
        tutorf = tutor[3:-4]
        tutor = int(tutorf)
        connexio.execute("SELECT Nom FROM INFORMACIO2 WHERE Ident = ?",(tutor,))
        nom_prof = connexio.fetchall()
        nom_proff = str(nom_prof)
        connexio.execute("SELECT Primer_Cognom FROM INFORMACIO2 WHERE Ident = ?",(tutor,))
        primer_cognom_prof = connexio.fetchall()
        primer_cognom_proff = str(primer_cognom_prof)
        connexio.execute("SELECT Segon_Cognom FROM INFORMACIO2 WHERE Ident = ?",(tutor,))
        segon_cognom_prof = connexio.fetchall()
        segon_cognom_proff = str(segon_cognom_prof)
        etiquetatutor1=customtkinter.CTkLabel(finestracercaalumnes1, text= "Tutor: ", height = 1, width = 20, text_font='Arial 10')
        etiquetatutor1.grid(row=3, column=0, padx=10, pady=0, sticky="w")
        etiquetatutor1def=customtkinter.CTkButton(finestracercaalumnes1, text= nom_proff[3:-4] + " " + primer_cognom_proff[3:-4] + " " + segon_cognom_proff[3:-4] , height = 1, width = 20, text_font='Arial 10', command=alumneprofessor)
        etiquetatutor1def.grid(row=3, column=1, padx=50, pady=20, sticky="w")
        
    else:
        etiquetatr1=customtkinter.CTkLabel(finestracercaalumnes1, text= "Tema TR: ", height = 1, width = 20, text_font='Arial 10')
        etiquetatr1.grid(row=1, column=0, padx=10, pady=0, sticky="w")
        etiquetatr1def=customtkinter.CTkLabel(finestracercaalumnes1, text= "No ho presenta", height = 1, width = 20, text_font='Arial 10', wraplengt=320, justify=tk.LEFT)
        etiquetatr1def.grid(row=1, column=1, padx=50, pady=20, sticky="w")

    connexio.execute("SELECT Tribunal1 FROM INFORMACIO WHERE Ident = ?",(identificadorescollit_alumne,))
    nom_prof_tribunal1 = connexio.fetchone()
    nom_prof_tribunal1f = str(nom_prof_tribunal1)
    nom_prof_tribunal1 = nom_prof_tribunal1f[2:-3]
    if nom_prof_tribunal1!="":
        pass
    else:
        nom_prof_tribunal1=None
    if nom_prof_tribunal1!=None:
        connexio.execute("SELECT Nom FROM INFORMACIO2 WHERE Ident = ?",(nom_prof_tribunal1,))
        nom_proftribunal = connexio.fetchall()
        nom_proftribunalf = str(nom_proftribunal)
        connexio.execute("SELECT Primer_Cognom FROM INFORMACIO2 WHERE Ident = ?",(nom_prof_tribunal1,))
        primer_cognom_proftribunal = connexio.fetchall()
        primer_cognom_proftribunalf = str(primer_cognom_proftribunal)
        connexio.execute("SELECT Segon_Cognom FROM INFORMACIO2 WHERE Ident = ?",(nom_prof_tribunal1,))
        segon_cognom_proftribunal = connexio.fetchall()
        segon_cognom_proftribunalf = str(segon_cognom_proftribunal)
        etiquetatribunal1=customtkinter.CTkLabel(finestracercaalumnes1, text= "Tribunal: ", height = 1, width = 20, text_font='Arial 10')
        etiquetatribunal1.grid(row=4, column=0, padx=10, pady=0, sticky="w")
        etiquetatribunal1def=customtkinter.CTkButton(finestracercaalumnes1, text= nom_proftribunalf[3:-4] + " " + primer_cognom_proftribunalf[3:-4] + " " + segon_cognom_proftribunalf[3:-4] , height = 1, width = 20, text_font='Arial 10', command=alumnetribunal1)
        etiquetatribunal1def.grid(row=4, column=1, padx=50, pady=20, sticky="w")
        
    else:
        pass

    connexio.execute("SELECT Tribunal2 FROM INFORMACIO WHERE Ident = ?",(identificadorescollit_alumne,))
    nom_prof_tribunal2 = connexio.fetchone()
    nom_prof_tribunal2f = str(nom_prof_tribunal2)
    nom_prof_tribunal2 = nom_prof_tribunal2f[2:-3]
    if nom_prof_tribunal2!="":
        pass
    else:
        nom_prof_tribunal2=None
        
    if nom_prof_tribunal2!=None:
        connexio.execute("SELECT Nom FROM INFORMACIO2 WHERE Ident = ?",(nom_prof_tribunal2,))
        nom_proftribunal = connexio.fetchall()
        nom_proftribunalf = str(nom_proftribunal)
        connexio.execute("SELECT Primer_Cognom FROM INFORMACIO2 WHERE Ident = ?",(nom_prof_tribunal2,))
        primer_cognom_proftribunal = connexio.fetchall()
        primer_cognom_proftribunalf = str(primer_cognom_proftribunal)
        connexio.execute("SELECT Segon_Cognom FROM INFORMACIO2 WHERE Ident = ?",(nom_prof_tribunal2,))
        segon_cognom_proftribunal = connexio.fetchall()
        segon_cognom_proftribunalf = str(segon_cognom_proftribunal)
        etiquetatribunal1=customtkinter.CTkLabel(finestracercaalumnes1, text= "Tribunal: ", height = 1, width = 20, text_font='Arial 10')
        etiquetatribunal1.grid(row=5, column=0, padx=10, pady=0, sticky="w")
        etiquetatribunal1def=customtkinter.CTkButton(finestracercaalumnes1, text= nom_proftribunalf[3:-4] + " " + primer_cognom_proftribunalf[3:-4] + " " + segon_cognom_proftribunalf[3:-4] , height = 1, width = 20, text_font='Arial 10', command=alumnetribunal2)
        etiquetatribunal1def.grid(row=5, column=1, padx=50, pady=20, sticky="w")
        
    else:
        pass

    connexio.execute("SELECT Tribunal3 FROM INFORMACIO WHERE Ident = ?",(identificadorescollit_alumne,))
    nom_prof_tribunal3 = connexio.fetchone()
    nom_prof_tribunal3f = str(nom_prof_tribunal3)
    nom_prof_tribunal3 = nom_prof_tribunal3f[2:-3]
    if nom_prof_tribunal3!="":
        pass
    else:
        nom_prof_tribunal3=None
        
    if nom_prof_tribunal3!=None:
        connexio.execute("SELECT Nom FROM INFORMACIO2 WHERE Ident = ?",(nom_prof_tribunal3,))
        nom_proftribunal = connexio.fetchall()
        nom_proftribunalf = str(nom_proftribunal)
        connexio.execute("SELECT Primer_Cognom FROM INFORMACIO2 WHERE Ident = ?",(nom_prof_tribunal3,))
        primer_cognom_proftribunal = connexio.fetchall()
        primer_cognom_proftribunalf = str(primer_cognom_proftribunal)
        connexio.execute("SELECT Segon_Cognom FROM INFORMACIO2 WHERE Ident = ?",(nom_prof_tribunal3,))
        segon_cognom_proftribunal = connexio.fetchall()
        segon_cognom_proftribunalf = str(segon_cognom_proftribunal)
        etiquetatribunal1=customtkinter.CTkLabel(finestracercaalumnes1, text= "Tribunal: ", height = 1, width = 20, text_font='Arial 10')
        etiquetatribunal1.grid(row=6, column=0, padx=10, pady=0, sticky="w")
        etiquetatribunal1def=customtkinter.CTkButton(finestracercaalumnes1, text= nom_proftribunalf[3:-4] + " " + primer_cognom_proftribunalf[3:-4] + " " + segon_cognom_proftribunalf[3:-4] , height = 1, width = 20, text_font='Arial 10', command=alumnetribunal3)
        etiquetatribunal1def.grid(row=6, column=1, padx=50, pady=20, sticky="w")
        
    else:
        pass
    
    # Creació del text on anirà la informació filtrada
    etiquetanom1=customtkinter.CTkLabel(finestracercaalumnes1, text= "Nom: ", height = 1, width = 20, text_font='Arial 10')
    etiquetanom1.grid(row=0, column=0, padx=10, pady=0, sticky="w")
    # Al possar les variables posem [3:-4] per a recortar els signes que surten al agafar l'informaciò i que no surtin
    etiquetanom1def=customtkinter.CTkLabel(finestracercaalumnes1, text= nomf[3:-4] + " " + primer_cognomf[3:-4] + " " + segon_cognomf[3:-4], height = 1, width = 20, text_font='Arial 10')
    etiquetanom1def.grid(row=0, column=1, padx=50, pady=20, sticky="w")
    bototornar2=customtkinter.CTkButton(finestracercaalumnes1,text="Tornar",command=tornarventanacercaralumne, height = 2, width = 10)
    bototornar2.grid(row=8, column=0, padx=50, pady=150, sticky="")
    # Funció tancar el programa des de la finestra amb els resultats filtrats
    def tancarprograma4():
        finestracercaalumnes1.destroy()
        quit()

    # Botó amb funció per a tancar el programa
    bototancarprograma4=customtkinter.CTkButton(finestracercaalumnes1,text="Tancar",command=tancarprograma4)
    bototancarprograma4.grid(row=8, column=1, padx=50, pady=20, sticky="e")

    finestracercaalumnes1.mainloop()




#Pasar d'Alumne a Professor
def alumneprofessor():
    finestracercaalumnes1.withdraw()
    # Agafem el valor global de l'identificador
    global identificadorescollit_alumne
    # Pasem l'identificador com a integer, número
    identificadorescollit_alumnef=int(identificadorescollit_alumne)
    identificadorescollit_alumne=identificadorescollit_alumnef
    connexio.execute("SELECT Ident FROM INFORMACIO2 WHERE Alumne_TR1 = ?",(identificadorescollit_alumne,))
    professor4 = connexio.fetchone()
    
    if professor4!=None:
        professor4f = str(professor4)
        professor4 = professor4f[1:-2]
        global identificadorescollit_professor
        identificadorescollit_professor=professor4
        # Executem la funció de "finestraalumnesprofessors"
        finestraalumnesprofessors()
    else:
        connexio.execute("SELECT Ident FROM INFORMACIO2 WHERE Alumne_TR2 = ?",(identificadorescollit_alumne,))
        professor4 = connexio.fetchone()
        if professor4!=None:
            professor4f = str(professor4)
            professor4 = professor4f[1:-2]
            identificadorescollit_professor=professor4
            # Executem la funció de "finestraalumnesprofessors"
            finestraalumnesprofessors()
        else:
            connexio.execute("SELECT Ident FROM INFORMACIO2 WHERE Alumne_TR3 = ?",(identificadorescollit_alumne,))
            professor4 = connexio.fetchone()
            if professor4!=None:
                professor4f = str(professor4)
                professor4 = professor4f[1:-2]
                identificadorescollit_professor=professor4
                # Executem la funció de "finestraalumnesprofessors"
                finestraalumnesprofessors()
            else:
                pass

#Pasar d'Alumne a Tribunal
def alumnetribunal1():
    finestracercaalumnes1.withdraw()
    # Agafem el valor global de l'identificador
    global identificadorescollit_alumne
    # Pasem l'identificador com a integer, número
    identificadorescollit_alumnef=int(identificadorescollit_alumne)
    identificadorescollit_alumne=identificadorescollit_alumnef
    connexio.execute("SELECT Tribunal1 FROM INFORMACIO WHERE Ident = ?",(identificadorescollit_alumne,))
    tribunal1 = connexio.fetchone()
    tribunal1f = str(tribunal1)
    tribunal1 = tribunal1f[2:-3]
    global identificadorescollit_professor
    identificadorescollit_professor=tribunal1
    # Executem la funció de "finestraalumnesprofessors"
    finestraalumnesprofessors()

def alumnetribunal2():
    finestracercaalumnes1.withdraw()
    # Agafem el valor global de l'identificador
    global identificadorescollit_alumne
    # Pasem l'identificador com a integer, número
    identificadorescollit_alumnef=int(identificadorescollit_alumne)
    identificadorescollit_alumne=identificadorescollit_alumnef
    connexio.execute("SELECT Tribunal2 FROM INFORMACIO WHERE Ident = ?",(identificadorescollit_alumne,))
    tribunal2 = connexio.fetchone()
    tribunal2f = str(tribunal2)
    tribunal2 = tribunal2f[2:-3]
    global identificadorescollit_professor
    identificadorescollit_professor=tribunal2
    # Executem la funció de "finestraalumnesprofessors"
    finestraalumnesprofessors()

def alumnetribunal3():
    finestracercaalumnes1.withdraw()
    # Agafem el valor global de l'identificador
    global identificadorescollit_alumne
    # Pasem l'identificador com a integer, número
    identificadorescollit_alumnef=int(identificadorescollit_alumne)
    identificadorescollit_alumne=identificadorescollit_alumnef
    connexio.execute("SELECT Tribunal3 FROM INFORMACIO WHERE Ident = ?",(identificadorescollit_alumne,))
    tribunal3 = connexio.fetchone()
    tribunal3f = str(tribunal3)
    tribunal3 = tribunal3f[2:-3]
    global identificadorescollit_professor
    identificadorescollit_professor=tribunal3
    # Executem la funció de "finestraalumnesprofessors"
    finestraalumnesprofessors()
    
# Funció per a crear la finestra de cercador de professors i després es tanca per a quan vulguem accedir ahí a partir dels alumnes, no surti en blanc
def finestraalumnesprofessors():
    def tornarventanaprofessors():
        finestra1.deiconify()
        finestraprofessors.withdraw()
    global finestraprofessors
    global identificadorescollit_professor
    global identificadorescollita_professor
    finestraprofessors=customtkinter.CTkToplevel()
    identificadorescollita_professor=tk.StringVar()
    finestraprofessors.geometry('550x700')
    finestraprofessors.title("Cercador de Professors")
    finestraprofessors.iconbitmap('iesmartidot.ico')
    font2 = Font(family="Arial", size=12)
    textprofessors=tk.Text(finestraprofessors, font=font2, width=57)
    textprofessors.grid(row=0, column=0, sticky='e', padx=5)
    textprofessors.insert(tk.END,c2)
    textprofessors['state'] = 'disabled'
    scrollbar2 = customtkinter.CTkScrollbar(finestraprofessors, command=textprofessors.yview)
    scrollbar2.grid(row=0, column=1, sticky='ns', padx=5)
    textprofessors.config(yscrollcommand=scrollbar2.set)

    # Assignem i configurem els widgets
    botocercaprofessors=customtkinter.CTkButton(finestraprofessors,text="Cercar",command=identprofessors, height = 8, width = 26, text_font='Arial 12')
    botocercaprofessors.grid(row=1, column=0, padx=0, pady=0, sticky="e")
    entry3=customtkinter.CTkEntry(finestraprofessors,justify=tk.LEFT, width=57, textvariable=identificadorescollita_professor, text_font='Arial 12')
    entry3.grid(row=1, column=0, padx=0, pady=0, sticky="")
    etiqueta3=customtkinter.CTkLabel(finestraprofessors, text= "Escriu l'identificador:", height = 1, width = 20, text_font='Arial 12')    
    etiqueta3.grid(row=1, column=0, padx=50, pady=20, sticky="w")
    bototornar3=customtkinter.CTkButton(finestraprofessors,text="Tornar",command=tornarventanaprofessors, height = 30, width = 60, text_font='Arial 12')
    bototornar3.grid(row=2, column=0, pady=160, sticky="e")

    # Al acabar, tanquem la finestra
    finestraprofessors.withdraw()
    # Executem la finestra amb la informació filtrada del professor
    cercaprofessors()

    
# Funció per a la creació de la finestra de professors    
def finestraprofessors():
    
    finestra1.withdraw()
    def tornarventanaprofessors():
        finestra1.deiconify()
        finestraprofessors.withdraw()
    global finestraprofessors
    finestraprofessors=customtkinter.CTkToplevel()
    global identificadorescollita_professor
    identificadorescollita_professor=tk.StringVar()
    finestraprofessors.geometry('550x700')
    finestraprofessors.title("Cercador de Professors")
    finestraprofessors.iconbitmap('iesmartidot.ico')
    font2 = Font(family="Arial", size=12)
    textprofessors=tk.Text(finestraprofessors, font=font2, width=57)
    textprofessors.grid(row=0, column=0, sticky='e', padx=5)
    textprofessors.insert(tk.END,c2)
    textprofessors['state'] = 'disabled'
    scrollbar2 = customtkinter.CTkScrollbar(finestraprofessors, command=textprofessors.yview)
    scrollbar2.grid(row=0, column=1, sticky='ns', padx=5)
    textprofessors.config(yscrollcommand=scrollbar2.set)

    # Assignem i configurem els widgets com els botons, l'entry i l'etiqueta
    botocercaprofessors=customtkinter.CTkButton(finestraprofessors,text="Cercar",command=identprofessors, height = 8, width = 26, text_font='Arial 12')
    botocercaprofessors.grid(row=1, column=0, padx=0, pady=0, sticky="e")
    entry3=customtkinter.CTkEntry(finestraprofessors,justify=tk.LEFT, width=57, textvariable=identificadorescollita_professor, text_font='Arial 12')
    entry3.grid(row=1, column=0, padx=0, pady=0, sticky="")
    etiqueta3=customtkinter.CTkLabel(finestraprofessors, text= "Escriu l'identificador:", height = 1, width = 20, text_font='Arial 12')    
    etiqueta3.grid(row=1, column=0, padx=50, pady=20, sticky="w")
    bototornar3=customtkinter.CTkButton(finestraprofessors,text="Tornar",command=tornarventanaprofessors, height = 30, width = 60, text_font='Arial 12')
    bototornar3.grid(row=2, column=0, pady=160, sticky="e")
    
    finestraprofessors.mainloop()



#Error identificador de professors
def identprofessors():
    # Agafar el entry possat i passar-lo a Integer
    global identificadorescollita_professor
    global identificadorescollit_professor
    identificadorescollit_professor=identificadorescollita_professor.get()
    connexio.execute("SELECT Nom FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    nomprofessor = connexio.fetchone()       
    if nomprofessor!=None:
        finestraprofessors.withdraw()
        cercaprofessors()
    else:
        messagebox.showwarning("Warning", "Selecciona un identificador correcte")


# Finestra amb l'informació filtrada del professor        
def cercaprofessors():
    global finestraprofessors
    finestraprofessors.withdraw()
    global finestracercaprofessors
    global identificadorescollit_professor
    finestracercaprofessors=customtkinter.CTkToplevel()
    finestracercaprofessors.geometry('550x700')
    finestracercaprofessors.title("Informació Filtrada del Professor")
    finestracercaprofessors.iconbitmap('iesmartidot.ico')
    connexio.execute("SELECT Nom FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    nom2 = connexio.fetchall()
    nomf2 = str(nom2)
    connexio.execute("SELECT Primer_Cognom FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    primer_cognom2 = connexio.fetchall()
    primer_cognomf2 = str(primer_cognom2)
    connexio.execute("SELECT Segon_Cognom FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    segon_cognom2 = connexio.fetchall()
    segon_cognomf2 = str(segon_cognom2)

    connexio.execute("SELECT Alumne_TR1 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    Alumne_TR1 = connexio.fetchall()
    identificadorescollitf2 = str(Alumne_TR1)
    Alumne_TR1=identificadorescollitf2[3:-4]
    identificadorescollit2 = int(Alumne_TR1)
    if identificadorescollit2 <= 51 and identificadorescollit2 >= 1:
        connexio.execute("SELECT Nom FROM INFORMACIO WHERE Ident = ?",(identificadorescollit2,))
        nom = connexio.fetchall()
        nomf = str(nom)
        connexio.execute("SELECT Primer_Cognom FROM INFORMACIO WHERE Ident = ?",(identificadorescollit2,))
        primer_cognom = connexio.fetchall()
        primer_cognomf = str(primer_cognom)
        connexio.execute("SELECT Segon_Cognom FROM INFORMACIO WHERE Ident = ?",(identificadorescollit2,))
        segon_cognom = connexio.fetchall()
        segon_cognomf = str(segon_cognom)
        connexio.execute("SELECT Hora FROM INFORMACIO WHERE Ident = ?",(identificadorescollit2,))
        hora = connexio.fetchall()
        horaf = str(hora)
        connexio.execute("SELECT Data FROM INFORMACIO WHERE Ident = ?",(identificadorescollit2,))
        data = connexio.fetchall()
        dataf = str(data)
        connexio.execute("SELECT Nom FROM INFORMACIO3 WHERE Ident = ?",(identificadorescollit2,))
        tema = connexio.fetchall()
        temaf = str(tema)

        etiquetaalumne2=customtkinter.CTkLabel(finestracercaprofessors, text= "Alumne TR: ", height = 1, width = 20, text_font='Arial 10')
        etiquetaalumne2.grid(row=1, column=0, padx=10, pady=0, sticky="w")
        etiquetaalumne2def=customtkinter.CTkLabel(finestracercaprofessors, text= nomf[3:-4] + " " + primer_cognomf[3:-4] + " " + segon_cognomf[3:-4], height = 1, width = 20, text_font='Arial 10')
        etiquetaalumne2def.grid(row=1, column=1, padx=50, pady=20, sticky="w") 
        
    # Si la variable és None:
    else:
        pass

    connexio.execute("SELECT Alumne_TR2 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    Alumne_TR2 = connexio.fetchone()
    identificadorescollitf3 = str(Alumne_TR2)
    Alumne_TR2=identificadorescollitf3[2:-3]
    identificadorescollit3 = int(Alumne_TR2)
    if identificadorescollit3 <= 51 and identificadorescollit3 >= 1:
        connexio.execute("SELECT Nom FROM INFORMACIO WHERE Ident = ?",(identificadorescollit3,))
        nom4 = connexio.fetchall()
        nomf4 = str(nom4)
        connexio.execute("SELECT Primer_Cognom FROM INFORMACIO WHERE Ident = ?",(identificadorescollit3,))
        primer_cognom4 = connexio.fetchall()
        primer_cognomf4 = str(primer_cognom4)
        connexio.execute("SELECT Segon_Cognom FROM INFORMACIO WHERE Ident = ?",(identificadorescollit3,))
        segon_cognom4 = connexio.fetchall()
        segon_cognomf4 = str(segon_cognom4)
        connexio.execute("SELECT Hora FROM INFORMACIO WHERE Ident = ?",(identificadorescollit3,))
        hora4 = connexio.fetchall()
        horaf4 = str(hora4)
        connexio.execute("SELECT Data FROM INFORMACIO WHERE Ident = ?",(identificadorescollit3,))
        data4 = connexio.fetchall()
        dataf4 = str(data4)
        connexio.execute("SELECT Nom FROM INFORMACIO3 WHERE Ident = ?",(identificadorescollit3,))
        tema4 = connexio.fetchall()
        temaf4 = str(tema4)

        etiquetaalumne2=customtkinter.CTkLabel(finestracercaprofessors, text= "Alumne TR: ", height = 1, width = 20, text_font='Arial 10')
        etiquetaalumne2.grid(row=2, column=0, padx=10, pady=0, sticky="w")
        etiquetaalumne2def=customtkinter.CTkLabel(finestracercaprofessors, text= nomf4[3:-4] + " " + primer_cognomf4[3:-4] + " " + segon_cognomf4[3:-4], height = 1, width = 20, text_font='Arial 10')
        etiquetaalumne2def.grid(row=2, column=1, padx=50, pady=20, sticky="w")
        
    # Si la variable és None:
    else:
        pass

    connexio.execute("SELECT Alumne_TR3 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    Alumne_TR3 = connexio.fetchone()
    identificadorescollitf4 = str(Alumne_TR3)
    Alumne_TR3=identificadorescollitf4[2:-3]
    identificadorescollit4 = int(Alumne_TR3)
    if identificadorescollit4 <= 51 and identificadorescollit4 >= 1:
        connexio.execute("SELECT Nom FROM INFORMACIO WHERE Ident = ?",(identificadorescollit4,))
        nom3 = connexio.fetchall()
        nomf3 = str(nom3)
        connexio.execute("SELECT Primer_Cognom FROM INFORMACIO WHERE Ident = ?",(identificadorescollit4,))
        primer_cognom3 = connexio.fetchall()
        primer_cognomf3 = str(primer_cognom3)
        connexio.execute("SELECT Segon_Cognom FROM INFORMACIO WHERE Ident = ?",(identificadorescollit4,))
        segon_cognom3 = connexio.fetchall()
        segon_cognomf3 = str(segon_cognom3)
        connexio.execute("SELECT Hora FROM INFORMACIO WHERE Ident = ?",(identificadorescollit4,))
        hora3 = connexio.fetchall()
        horaf3 = str(hora3)
        connexio.execute("SELECT Data FROM INFORMACIO WHERE Ident = ?",(identificadorescollit4,))
        data3 = connexio.fetchall()
        dataf3 = str(data3)
        connexio.execute("SELECT Nom FROM INFORMACIO3 WHERE Ident = ?",(identificadorescollit4,))
        tema3 = connexio.fetchall()
        temaf3 = str(tema3)

        etiquetaalumne2=customtkinter.CTkLabel(finestracercaprofessors, text= "Alumne TR: ", height = 1, width = 20, text_font='Arial 10')
        etiquetaalumne2.grid(row=3, column=0, padx=10, pady=0, sticky="w")
        etiquetaalumne2def=customtkinter.CTkLabel(finestracercaprofessors, text= nomf3[3:-4] + " " + primer_cognomf3[3:-4] + " " + segon_cognomf3[3:-4], height = 1, width = 20, text_font='Arial 10')
        etiquetaalumne2def.grid(row=3, column=1, padx=50, pady=20, sticky="w")
        
    # Si la variable és None:
    else:
        pass

    frame_principal = tk.Frame(finestracercaprofessors)
    frame_principal.grid(sticky='news', columnspan=2, row=4, column=0)
    frame_canvas = tk.Frame(frame_principal)
    frame_canvas.grid(row=0, column=0, sticky='nw')
    frame_canvas.grid_rowconfigure(0, weight=1)
    frame_canvas.grid_columnconfigure(0, weight=1)
    # Set grid_propagate to False to allow 5-by-5 buttons resizing later
    frame_canvas.grid_propagate(False)
    canvas = tk.Canvas(frame_canvas)
    canvas.grid(row=0, column=0, sticky="news")
    scrollbar_tribunals = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
    scrollbar_tribunals.grid(row=0, column=1, sticky='ns')
    canvas.configure(yscrollcommand=scrollbar_tribunals.set)
    frametribunals = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frametribunals, anchor='nw')
    
    connexio.execute("SELECT Alumne_TR1ibunal1 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnes_tribunal1 = connexio.fetchall()
    alumnes_tribunalf1 = str(alumnes_tribunal1)
    Alumne_TR1ib1=alumnes_tribunalf1[3:-4]
    alumnes_tribunalf1=int(Alumne_TR1ib1)
        
    if alumnes_tribunalf1 <= 51 and alumnes_tribunalf1 >= 1:
        connexio.execute("SELECT Nom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf1,))
        nom3 = connexio.fetchall()
        nomf3 = str(nom3)
        connexio.execute("SELECT Primer_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf1,))
        primer_cognom3 = connexio.fetchall()
        primer_cognomf3 = str(primer_cognom3)
        connexio.execute("SELECT Segon_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf1,))
        segon_cognom3 = connexio.fetchall()
        segon_cognomf3 = str(segon_cognom3)
        connexio.execute("SELECT Hora FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf1,))
        hora3 = connexio.fetchall()
        horaf3 = str(hora3)
        connexio.execute("SELECT Data FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf1,))
        data3 = connexio.fetchall()
        dataf3 = str(data3)
        connexio.execute("SELECT Nom FROM INFORMACIO3 WHERE Ident = ?",(alumnes_tribunalf1,))
        tema3 = connexio.fetchall()
        temaf3 = str(tema3)

        # S'assigna en mig de la recerca, perquè així en cas de que no existin, no es creen els botons 
        alumnetribunal1=customtkinter.CTkLabel(frametribunals, text= "Tribunal de l'alumne: ", height = 1, width = 20, text_font='Arial 10')
        alumnetribunal1.grid(row=1, column=0, padx=10, pady=0, sticky="w")
        alumnetribunal1def=customtkinter.CTkButton(frametribunals, text= nomf3[3:-4] + " " + primer_cognomf3[3:-4] + " " + segon_cognomf3[3:-4], height = 1, width = 20, text_font='Arial 10', command=professoralumne1)
        alumnetribunal1def.grid(row=1, column=1, padx=50, pady=20, sticky="w")
                
    else:
        pass
        
    connexio.execute("SELECT Alumne_TR1ibunal2 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnes_tribunal2 = connexio.fetchall()
    alumnes_tribunalf2 = str(alumnes_tribunal2)
    Alumne_TR1ib=alumnes_tribunalf2[3:-4]
    alumnes_tribunalf2=int(Alumne_TR1ib)
            
    if alumnes_tribunalf2 <= 51 and alumnes_tribunalf2 >= 1:
        connexio.execute("SELECT Nom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        nom4 = connexio.fetchall()
        nomf4 = str(nom4)
        connexio.execute("SELECT Primer_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        primer_cognom4 = connexio.fetchall()
        primer_cognomf4 = str(primer_cognom4)
        connexio.execute("SELECT Segon_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        segon_cognom4 = connexio.fetchall()
        segon_cognomf4 = str(segon_cognom4)
        connexio.execute("SELECT Hora FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        hora4 = connexio.fetchall()
        horaf4 = str(hora4)
        connexio.execute("SELECT Data FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        data4 = connexio.fetchall()
        dataf4 = str(data4)
        connexio.execute("SELECT Nom FROM INFORMACIO3 WHERE Ident = ?",(alumnes_tribunalf2,))
        tema4 = connexio.fetchall()
        temaf4 = str(tema4)
                
        alumnetribunal2=customtkinter.CTkLabel(frametribunals, text= "Tribunal de l'alumne: ", height = 1, width = 20, text_font='Arial 10')
        alumnetribunal2.grid(row=2, column=0, padx=10, pady=0, sticky="w")
        alumnetribunal2def=customtkinter.CTkButton(frametribunals, text= nomf4[3:-4] + " " + primer_cognomf4[3:-4] + " " + segon_cognomf4[3:-4], height = 1, width = 20, text_font='Arial 10', command=professoralumne2)
        alumnetribunal2def.grid(row=2, column=1, padx=50, pady=20, sticky="w")

    else:
        pass


    connexio.execute("SELECT Alumne_TR1ibunal3 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnes_tribunal2 = connexio.fetchall()
    alumnes_tribunalf2 = str(alumnes_tribunal2)
    Alumne_TR1ib=alumnes_tribunalf2[3:-4]
    alumnes_tribunalf2=int(Alumne_TR1ib)
            
    if alumnes_tribunalf2 <= 51 and alumnes_tribunalf2 >= 1:
        alumnes_tribunalf2=int(Alumne_TR1ib)
        connexio.execute("SELECT Nom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        nom5 = connexio.fetchall()
        nomf5 = str(nom5)
        connexio.execute("SELECT Primer_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        primer_cognom5 = connexio.fetchall()
        primer_cognomf5 = str(primer_cognom5)
        connexio.execute("SELECT Segon_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        segon_cognom5 = connexio.fetchall()
        segon_cognomf5 = str(segon_cognom5)
        connexio.execute("SELECT Hora FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        hora5 = connexio.fetchall()
        horaf5 = str(hora5)
        connexio.execute("SELECT Data FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        data5 = connexio.fetchall()
        dataf5 = str(data5)
        connexio.execute("SELECT Nom FROM INFORMACIO3 WHERE Ident = ?",(alumnes_tribunalf2,))
        tema5 = connexio.fetchall()
        temaf5 = str(tema5)            

        alumnetribunal3=customtkinter.CTkLabel(frametribunals, text= "Tribunal de l'alumne: ", height = 1, width = 20, text_font='Arial 10')
        alumnetribunal3.grid(row=3, column=0, padx=10, pady=0, sticky="w")
        alumnetribunal3def=customtkinter.CTkButton(frametribunals, text= nomf5[3:-4] + " " + primer_cognomf5[3:-4] + " " + segon_cognomf5[3:-4], height = 1, width = 20, text_font='Arial 10', command=professoralumne3)
        alumnetribunal3def.grid(row=3, column=1, padx=50, pady=20, sticky="w")
    else:
        pass

    connexio.execute("SELECT Alumne_TR1ibunal4 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnes_tribunal2 = connexio.fetchall()
    alumnes_tribunalf2 = str(alumnes_tribunal2)
    Alumne_TR1ib=alumnes_tribunalf2[3:-4]
    alumnes_tribunalf2=int(Alumne_TR1ib)
            
    if alumnes_tribunalf2 <= 51 and alumnes_tribunalf2 >= 1:
        alumnes_tribunalf2=int(Alumne_TR1ib)
        connexio.execute("SELECT Nom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        nom5 = connexio.fetchall()
        nomf5 = str(nom5)
        connexio.execute("SELECT Primer_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        primer_cognom5 = connexio.fetchall()
        primer_cognomf5 = str(primer_cognom5)
        connexio.execute("SELECT Segon_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        segon_cognom5 = connexio.fetchall()
        segon_cognomf5 = str(segon_cognom5)
        connexio.execute("SELECT Hora FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        hora5 = connexio.fetchall()
        horaf5 = str(hora5)
        connexio.execute("SELECT Data FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        data5 = connexio.fetchall()
        dataf5 = str(data5)
        connexio.execute("SELECT Nom FROM INFORMACIO3 WHERE Ident = ?",(alumnes_tribunalf2,))
        tema5 = connexio.fetchall()
        temaf5 = str(tema5)            

        alumnetribunal4=customtkinter.CTkLabel(frametribunals, text= "Tribunal de l'alumne: ", height = 1, width = 20, text_font='Arial 10')
        alumnetribunal4.grid(row=4, column=0, padx=10, pady=0, sticky="w")
        alumnetribunal4def=customtkinter.CTkButton(frametribunals, text= nomf5[3:-4] + " " + primer_cognomf5[3:-4] + " " + segon_cognomf5[3:-4], height = 1, width = 20, text_font='Arial 10', command=professoralumne4)
        alumnetribunal4def.grid(row=4, column=1, padx=50, pady=20, sticky="w")
    else:
        pass

    connexio.execute("SELECT Alumne_TR1ibunal5 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnes_tribunal2 = connexio.fetchall()
    alumnes_tribunalf2 = str(alumnes_tribunal2)
    Alumne_TR1ib=alumnes_tribunalf2[3:-4]
    alumnes_tribunalf2=int(Alumne_TR1ib)
            
    if alumnes_tribunalf2 <= 51 and alumnes_tribunalf2 >= 1:
        alumnes_tribunalf2=int(Alumne_TR1ib)
        connexio.execute("SELECT Nom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        nom5 = connexio.fetchall()
        nomf5 = str(nom5)
        connexio.execute("SELECT Primer_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        primer_cognom5 = connexio.fetchall()
        primer_cognomf5 = str(primer_cognom5)
        connexio.execute("SELECT Segon_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        segon_cognom5 = connexio.fetchall()
        segon_cognomf5 = str(segon_cognom5)
        connexio.execute("SELECT Hora FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        hora5 = connexio.fetchall()
        horaf5 = str(hora5)
        connexio.execute("SELECT Data FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        data5 = connexio.fetchall()
        dataf5 = str(data5)
        connexio.execute("SELECT Nom FROM INFORMACIO3 WHERE Ident = ?",(alumnes_tribunalf2,))
        tema5 = connexio.fetchall()
        temaf5 = str(tema5)            

        alumnetribunal5=customtkinter.CTkLabel(frametribunals, text= "Tribunal de l'alumne: ", height = 1, width = 20, text_font='Arial 10')
        alumnetribunal5.grid(row=5, column=0, padx=10, pady=0, sticky="w")
        alumnetribunal5def=customtkinter.CTkButton(frametribunals, text= nomf5[3:-4] + " " + primer_cognomf5[3:-4] + " " + segon_cognomf5[3:-4], height = 1, width = 20, text_font='Arial 10', command=professoralumne5)
        alumnetribunal5def.grid(row=5, column=1, padx=50, pady=20, sticky="w")
    else:
        pass

    connexio.execute("SELECT Alumne_TR1ibunal6 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnes_tribunal2 = connexio.fetchall()
    alumnes_tribunalf2 = str(alumnes_tribunal2)
    Alumne_TR1ib=alumnes_tribunalf2[3:-4]
    alumnes_tribunalf2=int(Alumne_TR1ib)
            
    if alumnes_tribunalf2 <= 51 and alumnes_tribunalf2 >= 1:
        alumnes_tribunalf2=int(Alumne_TR1ib)
        connexio.execute("SELECT Nom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        nom5 = connexio.fetchall()
        nomf5 = str(nom5)
        connexio.execute("SELECT Primer_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        primer_cognom5 = connexio.fetchall()
        primer_cognomf5 = str(primer_cognom5)
        connexio.execute("SELECT Segon_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        segon_cognom5 = connexio.fetchall()
        segon_cognomf5 = str(segon_cognom5)
        connexio.execute("SELECT Hora FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        hora5 = connexio.fetchall()
        horaf5 = str(hora5)
        connexio.execute("SELECT Data FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        data5 = connexio.fetchall()
        dataf5 = str(data5)
        connexio.execute("SELECT Nom FROM INFORMACIO3 WHERE Ident = ?",(alumnes_tribunalf2,))
        tema5 = connexio.fetchall()
        temaf5 = str(tema5)            

        alumnetribunal6=customtkinter.CTkLabel(frametribunals, text= "Tribunal de l'alumne: ", height = 1, width = 20, text_font='Arial 10')
        alumnetribunal6.grid(row=6, column=0, padx=10, pady=0, sticky="w")
        alumnetribunal6def=customtkinter.CTkButton(frametribunals, text= nomf5[3:-4] + " " + primer_cognomf5[3:-4] + " " + segon_cognomf5[3:-4], height = 1, width = 20, text_font='Arial 10', command=professoralumne6)
        alumnetribunal6def.grid(row=6, column=1, padx=50, pady=20, sticky="w")
    else:
        pass
    connexio.execute("SELECT Alumne_TR1ibunal7 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnes_tribunal2 = connexio.fetchall()
    alumnes_tribunalf2 = str(alumnes_tribunal2)
    Alumne_TR1ib=alumnes_tribunalf2[3:-4]
    alumnes_tribunalf2=int(Alumne_TR1ib)
            
    if alumnes_tribunalf2 <= 51 and alumnes_tribunalf2 >= 1:
        alumnes_tribunalf2=int(Alumne_TR1ib)
        connexio.execute("SELECT Nom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        nom5 = connexio.fetchall()
        nomf5 = str(nom5)
        connexio.execute("SELECT Primer_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        primer_cognom5 = connexio.fetchall()
        primer_cognomf5 = str(primer_cognom5)
        connexio.execute("SELECT Segon_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        segon_cognom5 = connexio.fetchall()
        segon_cognomf5 = str(segon_cognom5)
        connexio.execute("SELECT Hora FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        hora5 = connexio.fetchall()
        horaf5 = str(hora5)
        connexio.execute("SELECT Data FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        data5 = connexio.fetchall()
        dataf5 = str(data5)
        connexio.execute("SELECT Nom FROM INFORMACIO3 WHERE Ident = ?",(alumnes_tribunalf2,))
        tema5 = connexio.fetchall()
        temaf5 = str(tema5)            

        alumnetribunal7=customtkinter.CTkLabel(frametribunals, text= "Tribunal de l'alumne: ", height = 1, width = 20, text_font='Arial 10')
        alumnetribunal7.grid(row=7, column=0, padx=10, pady=0, sticky="w")
        alumnetribunal7def=customtkinter.CTkButton(frametribunals, text= nomf5[3:-4] + " " + primer_cognomf5[3:-4] + " " + segon_cognomf5[3:-4], height = 1, width = 20, text_font='Arial 10', command=professoralumne7)
        alumnetribunal7def.grid(row=7, column=1, padx=50, pady=20, sticky="w")
    else:
        pass
    connexio.execute("SELECT Alumne_TR1ibunal8 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnes_tribunal2 = connexio.fetchall()
    alumnes_tribunalf2 = str(alumnes_tribunal2)
    Alumne_TR1ib=alumnes_tribunalf2[3:-4]
    alumnes_tribunalf2=int(Alumne_TR1ib)
            
    if alumnes_tribunalf2 <= 51 and alumnes_tribunalf2 >= 1:
        alumnes_tribunalf2=int(Alumne_TR1ib)
        connexio.execute("SELECT Nom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        nom5 = connexio.fetchall()
        nomf5 = str(nom5)
        connexio.execute("SELECT Primer_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        primer_cognom5 = connexio.fetchall()
        primer_cognomf5 = str(primer_cognom5)
        connexio.execute("SELECT Segon_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        segon_cognom5 = connexio.fetchall()
        segon_cognomf5 = str(segon_cognom5)
        connexio.execute("SELECT Hora FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        hora5 = connexio.fetchall()
        horaf5 = str(hora5)
        connexio.execute("SELECT Data FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        data5 = connexio.fetchall()
        dataf5 = str(data5)
        connexio.execute("SELECT Nom FROM INFORMACIO3 WHERE Ident = ?",(alumnes_tribunalf2,))
        tema5 = connexio.fetchall()
        temaf5 = str(tema5)            

        alumnetribunal8=customtkinter.CTkLabel(frametribunals, text= "Tribunal de l'alumne: ", height = 1, width = 20, text_font='Arial 10')
        alumnetribunal8.grid(row=8, column=0, padx=10, pady=0, sticky="w")
        alumnetribunal8def=customtkinter.CTkButton(frametribunals, text= nomf5[3:-4] + " " + primer_cognomf5[3:-4] + " " + segon_cognomf5[3:-4], height = 1, width = 20, text_font='Arial 10', command=professoralumne8)
        alumnetribunal8def.grid(row=8, column=1, padx=50, pady=20, sticky="w")
    else:
        pass
    connexio.execute("SELECT Alumne_TR1ibunal9 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnes_tribunal2 = connexio.fetchall()
    alumnes_tribunalf2 = str(alumnes_tribunal2)
    Alumne_TR1ib=alumnes_tribunalf2[3:-4]
    alumnes_tribunalf2=int(Alumne_TR1ib)
            
    if alumnes_tribunalf2 <= 51 and alumnes_tribunalf2 >= 1:
        alumnes_tribunalf2=int(Alumne_TR1ib)
        connexio.execute("SELECT Nom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        nom5 = connexio.fetchall()
        nomf5 = str(nom5)
        connexio.execute("SELECT Primer_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        primer_cognom5 = connexio.fetchall()
        primer_cognomf5 = str(primer_cognom5)
        connexio.execute("SELECT Segon_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        segon_cognom5 = connexio.fetchall()
        segon_cognomf5 = str(segon_cognom5)
        connexio.execute("SELECT Hora FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        hora5 = connexio.fetchall()
        horaf5 = str(hora5)
        connexio.execute("SELECT Data FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        data5 = connexio.fetchall()
        dataf5 = str(data5)
        connexio.execute("SELECT Nom FROM INFORMACIO3 WHERE Ident = ?",(alumnes_tribunalf2,))
        tema5 = connexio.fetchall()
        temaf5 = str(tema5)            

        alumnetribunal9=customtkinter.CTkLabel(frametribunals, text= "Tribunal de l'alumne: ", height = 1, width = 20, text_font='Arial 10')
        alumnetribunal9.grid(row=9, column=0, padx=10, pady=0, sticky="w")
        alumnetribunal9def=customtkinter.CTkButton(frametribunals, text= nomf5[3:-4] + " " + primer_cognomf5[3:-4] + " " + segon_cognomf5[3:-4], height = 1, width = 20, text_font='Arial 10', command=professoralumne9)
        alumnetribunal9def.grid(row=9, column=1, padx=50, pady=20, sticky="w")
    else:
        pass
    
    connexio.execute("SELECT Alumne_TR1ibunal10 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnes_tribunal2 = connexio.fetchall()
    alumnes_tribunalf2 = str(alumnes_tribunal2)
    Alumne_TR1ib=alumnes_tribunalf2[3:-4]
    alumnes_tribunalf2=int(Alumne_TR1ib)
            
    if alumnes_tribunalf2 <= 51 and alumnes_tribunalf2 >= 1:
        alumnes_tribunalf2=int(Alumne_TR1ib)
        connexio.execute("SELECT Nom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        nom5 = connexio.fetchall()
        nomf5 = str(nom5)
        connexio.execute("SELECT Primer_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        primer_cognom5 = connexio.fetchall()
        primer_cognomf5 = str(primer_cognom5)
        connexio.execute("SELECT Segon_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        segon_cognom5 = connexio.fetchall()
        segon_cognomf5 = str(segon_cognom5)
        connexio.execute("SELECT Hora FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        hora5 = connexio.fetchall()
        horaf5 = str(hora5)
        connexio.execute("SELECT Data FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        data5 = connexio.fetchall()
        dataf5 = str(data5)
        connexio.execute("SELECT Nom FROM INFORMACIO3 WHERE Ident = ?",(alumnes_tribunalf2,))
        tema5 = connexio.fetchall()
        temaf5 = str(tema5)            

        alumnetribunal10=customtkinter.CTkLabel(frametribunals, text= "Tribunal de l'alumne: ", height = 1, width = 20, text_font='Arial 10')
        alumnetribunal10.grid(row=10, column=0, padx=10, pady=0, sticky="w")
        alumnetribunal10def=customtkinter.CTkButton(frametribunals, text= nomf5[3:-4] + " " + primer_cognomf5[3:-4] + " " + segon_cognomf5[3:-4], height = 1, width = 20, text_font='Arial 10', command=professoralumne10)
        alumnetribunal10def.grid(row=10, column=1, padx=50, pady=20, sticky="w")
    else:
        pass
    
    connexio.execute("SELECT Alumne_TR1ibunal11 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnes_tribunal2 = connexio.fetchall()
    alumnes_tribunalf2 = str(alumnes_tribunal2)
    Alumne_TR1ib=alumnes_tribunalf2[3:-4]
    alumnes_tribunalf2=int(Alumne_TR1ib)
            
    if alumnes_tribunalf2 <= 51 and alumnes_tribunalf2 >= 1:
        alumnes_tribunalf2=int(Alumne_TR1ib)
        connexio.execute("SELECT Nom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        nom5 = connexio.fetchall()
        nomf5 = str(nom5)
        connexio.execute("SELECT Primer_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        primer_cognom5 = connexio.fetchall()
        primer_cognomf5 = str(primer_cognom5)
        connexio.execute("SELECT Segon_Cognom FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        segon_cognom5 = connexio.fetchall()
        segon_cognomf5 = str(segon_cognom5)
        connexio.execute("SELECT Hora FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        hora5 = connexio.fetchall()
        horaf5 = str(hora5)
        connexio.execute("SELECT Data FROM INFORMACIO WHERE Ident = ?",(alumnes_tribunalf2,))
        data5 = connexio.fetchall()
        dataf5 = str(data5)
        connexio.execute("SELECT Nom FROM INFORMACIO3 WHERE Ident = ?",(alumnes_tribunalf2,))
        tema5 = connexio.fetchall()
        temaf5 = str(tema5)            

        alumnetribunal11=customtkinter.CTkLabel(frametribunals, text= "Tribunal de l'alumne: ", height = 1, width = 20, text_font='Arial 10')
        alumnetribunal11.grid(row=11, column=0, padx=10, pady=0, sticky="w")
        alumnetribunal11def=customtkinter.CTkButton(frametribunals, text= nomf5[3:-4] + " " + primer_cognomf5[3:-4] + " " + segon_cognomf5[3:-4], height = 1, width = 20, text_font='Arial 10', command=professoralumne11)
        alumnetribunal11def.grid(row=11, column=1, padx=50, pady=20, sticky="w")
    else:
        pass

    # Creació de la GUI del resultat del filtrat

    # Funció per a tornar a la finestra del cercador de professors   
    def tornarventanacercarprofessor():
        finestraprofessors.deiconify()
        finestracercaprofessors.withdraw()

    # Funció per a tancar el programa
    def tancarprograma3():
        finestracercaprofessors.destroy()
        quit()

    # Definim els widgets restants de la finestra
    etiquetanom2=customtkinter.CTkLabel(finestracercaprofessors, text= "Nom: ", height = 1, width = 20, text_font='Arial 10')
    etiquetanom2.grid(row=0, column=0, padx=10, pady=0, sticky="w")
    etiquetanom2def=customtkinter.CTkLabel(finestracercaprofessors, text= nomf2[3:-4] + " " + primer_cognomf2[3:-4] + " " + segon_cognomf2[3:-4], height = 1, width = 20, text_font='Arial 10')
    etiquetanom2def.grid(row=0, column=1, padx=50, pady=20, sticky="w")
    
    bototornar4=customtkinter.CTkButton(finestracercaprofessors,text="Tornar",command=tornarventanacercarprofessor,  height = 1, width = 20, text_font='Arial 10')
    bototornar4.grid(row=7, column=0, padx=50, pady=150, sticky="")
    bototancarprograma3=customtkinter.CTkButton(finestracercaprofessors,text="Tancar",command=tancarprograma3)
    bototancarprograma3.grid(row=7, column=1, padx=50, pady=20, sticky="e")
    frametribunals.update_idletasks()
    
    frame_canvas.config(width=380, height=200)
    canvas.config(scrollregion=canvas.bbox("all"))


#Pasar de Professor a Alumne 1
def professoralumne1():
    finestracercaprofessors.withdraw()
    global identificadorescollit_professor
    connexio.execute("SELECT Alumne_TR1ibunal1 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnetribunal1 = connexio.fetchall()
    alumnetribunal1f = str(alumnetribunal1)
    alumnetribunal1 = alumnetribunal1f[3:-4]
    global identificadorescollit_alumne
    identificadorescollit_alumne=int(alumnetribunal1)
    # Executem la funció per a fer posible anar a la recerca d'alumnes
    finestratrsalumnes()

#Pasar de Professor a Alumne 2
def professoralumne2():
    finestracercaprofessors.withdraw()
    global identificadorescollit_professor
    connexio.execute("SELECT Alumne_TR1ibunal2 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnetribunal2 = connexio.fetchall()
    alumnetribunal2f = str(alumnetribunal2)
    alumnetribunal2 = alumnetribunal2f[3:-4]
    global identificadorescollit_alumne
    identificadorescollit_alumne=int(alumnetribunal2)
    finestratrsalumnes()

#Pasar de Professor a Alumne 3
def professoralumne3():
    finestracercaprofessors.withdraw()
    global identificadorescollit_professor
    connexio.execute("SELECT Alumne_TR1ibunal3 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnetribunal3 = connexio.fetchall()
    alumnetribunal3f = str(alumnetribunal3)
    alumnetribunal3 = alumnetribunal3f[3:-4]
    global identificadorescollit_alumne
    identificadorescollit_alumne=int(alumnetribunal3)
    finestratrsalumnes()
    
def professoralumne4():
    finestracercaprofessors.withdraw()
    global identificadorescollit_professor
    connexio.execute("SELECT Alumne_TR1ibunal4 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnetribunal4 = connexio.fetchall()
    alumnetribunal4f = str(alumnetribunal4)
    alumnetribunal4 = alumnetribunal4f[3:-4]
    global identificadorescollit_alumne
    identificadorescollit_alumne=int(alumnetribunal4)
    finestratrsalumnes()

def professoralumne5():
    finestracercaprofessors.withdraw()
    global identificadorescollit_professor
    connexio.execute("SELECT Alumne_TR1ibunal5 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnetribunal5 = connexio.fetchall()
    alumnetribunal5f = str(alumnetribunal5)
    alumnetribunal5 = alumnetribunal5f[3:-4]
    global identificadorescollit_alumne
    identificadorescollit_alumne=int(alumnetribunal5)
    finestratrsalumnes()

def professoralumne6():
    finestracercaprofessors.withdraw()
    global identificadorescollit_professor
    connexio.execute("SELECT Alumne_TR1ibunal6 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnetribunal6 = connexio.fetchall()
    alumnetribunal6f = str(alumnetribunal6)
    alumnetribunal6 = alumnetribunal6f[3:-4]
    global identificadorescollit_alumne
    identificadorescollit_alumne=int(alumnetribunal6)
    finestratrsalumnes()

def professoralumne7():
    finestracercaprofessors.withdraw()
    global identificadorescollit_professor
    connexio.execute("SELECT Alumne_TR1ibunal7 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnetribunal7 = connexio.fetchall()
    alumnetribunal7f = str(alumnetribunal7)
    alumnetribunal7 = alumnetribunal7f[3:-4]
    global identificadorescollit_alumne
    identificadorescollit_alumne=int(alumnetribunal7)
    finestratrsalumnes()

def professoralumne8():
    finestracercaprofessors.withdraw()
    global identificadorescollit_professor
    connexio.execute("SELECT Alumne_TR1ibunal8 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnetribunal8 = connexio.fetchall()
    alumnetribunal8f = str(alumnetribunal8)
    alumnetribunal8 = alumnetribunal8f[3:-4]
    global identificadorescollit_alumne
    identificadorescollit_alumne=int(alumnetribunal8)
    finestratrsalumnes()

def professoralumne9():
    finestracercaprofessors.withdraw()
    global identificadorescollit_professor
    connexio.execute("SELECT Alumne_TR1ibunal9 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnetribunal9 = connexio.fetchall()
    alumnetribunal9f = str(alumnetribunal9)
    alumnetribunal9 = alumnetribunal9f[3:-4]
    global identificadorescollit_alumne
    identificadorescollit_alumne=int(alumnetribunal9)
    finestratrsalumnes()

def professoralumne10():
    finestracercaprofessors.withdraw()
    global identificadorescollit_professor
    connexio.execute("SELECT Alumne_TR1ibunal10 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnetribunal10 = connexio.fetchall()
    alumnetribunal10f = str(alumnetribunal10)
    alumnetribunal10 = alumnetribunal10f[3:-4]
    global identificadorescollit_alumne
    identificadorescollit_alumne=int(alumnetribunal10)
    finestratrsalumnes()

def professoralumne11():
    finestracercaprofessors.withdraw()
    global identificadorescollit_professor
    connexio.execute("SELECT Alumne_TR1ibunal11 FROM INFORMACIO2 WHERE Ident = ?",(identificadorescollit_professor,))
    alumnetribunal11 = connexio.fetchall()
    alumnetribunal11f = str(alumnetribunal11)
    alumnetribunal11 = alumnetribunal11f[3:-4]
    global identificadorescollit_alumne
    identificadorescollit_alumne=int(alumnetribunal11)
    finestratrsalumnes()


# Funció per a crear la finestra de cercador d'alumnes i després es tanca per a quan vulguem accedir ahí a partir dels professors, no surti en blanc    
def finestratrsalumnes():
    # Crear variable tipus String que anirà variant cada vegada que s'utilitzi el cercador
    global identificadorescollita_alumne
    identificadorescollita_alumne=tk.StringVar()
    # Dins de la finestra del filtre realitzat, una funció per a tornar a la finestra del cercador d'alumnes    
    def tornarventanacercaralumne():
        finestraalumnes.deiconify()
        finestracercaalumnes1.withdraw()
    # Crear una nova finestra per a la creació de la del cercador dels alumnes
    global finestraalumnes
    finestraalumnes=customtkinter.CTkToplevel()
    # Assignar resolució de la finestra creada
    finestraalumnes.geometry('550x700')
    finestraalumnes.title("Cercador d'Alumnes")
    finestraalumnes.iconbitmap('iesmartidot.ico')
    # Crear un tipus de font per a la lletra utilitzada
    font1 = Font(family="Arial", size=12)
    # Creació d'un Widget de text
    textalumnes=tk.Text(finestraalumnes, font=font1, width=57)
    # Posar propietats al Widget de text
    textalumnes.grid(row=0, column=0, sticky='e', padx=5)
    # Insertar el text aconseguit a la línea 183
    textalumnes.insert(tk.END,c1)
    textalumnes['state'] = 'disabled'
    # Creació de Scrollbar vertical i configuració d'aquest
    scrollbar1 = customtkinter.CTkScrollbar(finestraalumnes, command=textalumnes.yview)
    scrollbar1.grid(row=0, column=1, sticky='ns', padx=5)
    textalumnes.config(yscrollcommand=scrollbar1.set)

    # Funció tornar a la 1 finestra
    def tornarventanaalumne():
        # Tornar a obrir la 1 finestra
        finestra1.deiconify()
        # Tancar la finestra del cercador dels alumnes
        global finestraalumnes
        finestraalumnes.withdraw()

    # Assignem els widgets   
    entry1=customtkinter.CTkEntry(finestraalumnes,justify=tk.LEFT, width = 57, textvariable=identificadorescollita_alumne, text_font='Arial 12')
    entry1.grid(row=1, column=0, padx=0, pady=0, sticky="")    
    botocercaalumnes=customtkinter.CTkButton(finestraalumnes,text="Cercar",command=identalumnes, height = 8, width = 26, text_font='Arial 12')
    botocercaalumnes.grid(row=1, column=0, padx=0, pady=0, sticky="e") 
    bototornar1=customtkinter.CTkButton(finestraalumnes,text="Tornar",command=tornarventanaalumne, height = 30, width = 60, text_font='Arial 12')
    bototornar1.grid(row=2, column=0, pady=160, sticky="e")
    etiqueta1=customtkinter.CTkLabel(finestraalumnes, text= "Escriu l'identificador:", height = 1, width = 20, text_font='Arial 12')    
    etiqueta1.grid(row=1, column=0, padx=50, pady=20, sticky="w")
    finestraalumnes.withdraw()
    cercaalumnes()


# Funció per a la creació de la finestra amb el cercador de TRs          
def finestratrs():
    
    finestra1.withdraw()
    def tornarventanatrs():
        finestra1.deiconify()
        finestratrs.withdraw()
    global finestratrs
    finestratrs=customtkinter.CTkToplevel()
    finestratrs.geometry('550x700')
    finestratrs.title("Cercador de TRs")
    finestratrs.iconbitmap('iesmartidot.ico')
    identificadorescollita_trs=StringVar()
    font3 = Font(family="Arial", size=12)
    texttrs=tk.Text(finestratrs, font=font3, width=57)
    texttrs.grid(row=0, column=0, sticky='e', padx=5)
    texttrs.insert(tk.END,c3)
    texttrs['state'] = 'disabled'
    scrollbar3 = customtkinter.CTkScrollbar(finestratrs, command=texttrs.yview)
    scrollbar3.grid(row=0, column=1, sticky='ns', padx=5)
    texttrs.config(yscrollcommand=scrollbar3.set)    

    # Assignem i configurem els widgets
    fontwidgets3 = Font(family="Arial", weight="bold", size=80)
    botocercatrs=customtkinter.CTkButton(finestratrs,text="Cercar",command=identtrs, height = 8, width = 26, text_font='Arial 12')
    botocercatrs.grid(row=1, column=0, padx=0, pady=0, sticky="e")
    global entry_trs
    entry_trs=customtkinter.CTkEntry(finestratrs,justify=tk.LEFT, width=70, textvariable=identificadorescollita_trs, text_font='Arial 12')
    entry_trs.grid(row=1, column=0, padx=0, pady=0, sticky="")
    etiqueta3=customtkinter.CTkLabel(finestratrs, text= "Escriu l'identificador:", height = 1, width = 20, text_font='Arial 12')    
    etiqueta3.grid(row=1, column=0, padx=50, pady=20, sticky="w")
    bototornar5=customtkinter.CTkButton(finestratrs,text="Tornar",command=tornarventanatrs, height = 30, width = 60, text_font='Arial 12')
    bototornar5.grid(row=2, column=0, pady=160, sticky="e")



#Error identificador de trs
def identtrs():
    global identificadorescollit_trs
    identificadorescollit_trs=entry_trs.get()
    connexio.execute("SELECT Nom FROM INFORMACIO3 WHERE Ident_TR = ?",(identificadorescollit_trs,))
    tema6 = connexio.fetchone()       
    tema6f = str(tema6)
    if tema6!=None:
        finestratrs.withdraw()
        cercatrs()
    else:
        messagebox.showwarning("Warning", "Selecciona un identificador correcte. Ha d'estar en majúscules")

        

# Funció per a la creació de la finestra de la informació filtrada dels TRs    
def cercatrs():
    global finestracercatrs
    finestracercatrs=customtkinter.CTkToplevel()
    finestracercatrs.geometry('550x700')
    finestracercatrs.title("Informació Filtrada del TR")
    finestracercatrs.iconbitmap('iesmartidot.ico')
    finestracercatrs.grid_propagate(False)
    global identificadorescollit_trs
    
    connexio.execute("SELECT Ident FROM INFORMACIO3 WHERE Ident_TR = ?",(identificadorescollit_trs,))
    alumne3 = connexio.fetchall()
    alumne3f = str(alumne3)
    alumne3 = alumne3f[2:-3]
    identificadorescollit_alumne=int(alumne3)
    connexio.execute("SELECT Nom FROM INFORMACIO WHERE Ident = ?",(identificadorescollit_alumne,))
    nom6 = connexio.fetchall()
    nom6f = str(nom6)
    connexio.execute("SELECT Primer_Cognom FROM INFORMACIO WHERE Ident = ?",(identificadorescollit_alumne,))
    primer_cognom6 = connexio.fetchall()
    primer_cognom6f = str(primer_cognom6)
    connexio.execute("SELECT Segon_Cognom FROM INFORMACIO WHERE Ident = ?",(identificadorescollit_alumne,))
    segon_cognom6 = connexio.fetchall()
    segon_cognom6f = str(segon_cognom6)
    connexio.execute("SELECT Nom FROM INFORMACIO3 WHERE Ident_TR = ?",(identificadorescollit_trs,))
    tema6 = connexio.fetchone()       
    tema6f = str(tema6)

    def tornarventanacercatrs():
        finestratrs.deiconify()
        finestracercatrs.withdraw()
    
    etiquetanom3=customtkinter.CTkLabel(finestracercatrs, text= "Nom: ", height = 1, width = 20, text_font='Arial 10')
    etiquetanom3.grid(row=0, column=0, padx=10, pady=0, sticky="w")
    etiquetanom3def=customtkinter.CTkButton(finestracercatrs, text= nom6f[3:-4] + " " + primer_cognom6f[3:-4] + " " + segon_cognom6f[3:-4], height = 1, width = 20, text_font='Arial 10', command=trsnom)
    etiquetanom3def.grid(row=0, column=1, padx=50, pady=20, sticky="w")
    etiquetatr3=customtkinter.CTkLabel(finestracercatrs, text= "Tema TR: ", height = 1, width = 20, text_font='Arial 10')
    etiquetatr3.grid(row=1, column=0, padx=10, pady=0, sticky="w")
    etiquetatr3def=customtkinter.CTkLabel(finestracercatrs, text= tema6f[2:-3], height = 1, width = 20, text_font='Arial 10', wraplengt=320, justify=tk.LEFT)
    etiquetatr3def.grid(row=1, column=1, padx=50, pady=20, sticky="w")

    # Botó per a la funció de tornar    
    bototornar6=customtkinter.CTkButton(finestracercatrs,text="Tornar",command=tornarventanacercatrs, height = 2, width = 10)
    bototornar6.grid(row=7, column=0, padx=50, pady=150, sticky="")

    # Funció per a tancar el programa
    def tancarprograma2():
        finestracercatrs.destroy()
        quit()

    # Botó per a la funció de tancar el programa   
    bototancarprograma2=customtkinter.CTkButton(finestracercatrs,text="Tancar",command=tancarprograma2)
    bototancarprograma2.grid(row=7, column=1, padx=50, pady=20, sticky="e")
            
    finestracercatrs.mainloop()



#Pasar de Trs a Alumne
def trsnom():
    finestracercatrs.withdraw()
    global identificadorescollit_trs
    connexio.execute("SELECT Ident FROM INFORMACIO3 WHERE Ident_TR = ?",(identificadorescollit_trs,))
    alumne3 = connexio.fetchall()
    alumne3f = str(alumne3)
    alumne3 = alumne3f[2:-3]
    global identificadorescollit_alumne
    identificadorescollit_alumne=int(alumne3)
    finestratrsalumnes()   


# Al iniciar el programa, fem que s'executi la funció de la finestra principal 
finestra1()

# Desar canvis base de dades 
basededades.commit()
# Tancar connexió amb la base de dades 
basededades.close()
