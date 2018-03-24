##################################################
##################################################
################ D E M I N E U R #################
##################################################
##################################################
######## CHOI Céline et LE LOUET Etienne #########
##################################################
##################################################

import time
from random import randint
import random
from tkinter import*
from tkinter.messagebox import *


##################################################
############### VARIABLES GLOBALES ###############
##################################################





grillemines=[[0 for i in range(0,11)]for j in range(0,11)]
grillejeu=[["*" for i in range(0,11)]for j in range(0,11)]

lignemines=[0 for i in range (0,10)]
colonemines=[0 for i in range (0,10)]
lignedrapeau=[0 for i in range (0,10)]
colonedrapeau=[0 for i in range (0,10)]

compteur = 10


##################################################
################ FONCTIONS MINES #################
##################################################


def mines(t):

    r = 0
    while r < 10 :
        x=random.randint(1,9)
        y=random.randint(1,9)
        if not t[x][y]=="M":  
            t[x][y]="M"
            r +=1
    return t


def nombredemines(x,y,grille):
    k = 0
    for i in range(x-1,x+2):
         for j in range(y-1,y+2):
              if(grille[i][j] == 'M'):
                   k += 1
    return k



def remplirgrille(grille):
     for i in range(1,10):
          for j in range(1,10):
               if(not grille[i][j] == 'M'):
                    grille[i][j] = nombredemines(i,j,grille)



grillemines = mines(grillemines)
remplirgrille(grillemines)

#################### CREUSER #####################



def creuser(event):
    global grillemines 
    x = event.x//50 +1 
    y = event.y//50 +1
    
    if grillejeu[x][y]=="!":
        nbmines.configure(text="Vous ne pouvez pas creuser ici")
        
    elif grillemines[x][y]=="M":
        can.create_image((x-1)*50 +7, (y-1)*50 +7, anchor=NW, image=mine)
        fenetredefaite()
    else :
        casemines(x,y)
        
        
def casemines(X,Y):
    grillejeu[X][Y] = grillemines[X][Y]
    can.create_rectangle((X-1)*50, (Y-1)*50, X*50, Y*50, fill='white')
    if grillejeu[X][Y]==1:
        can.create_image((X-1)*50 +7, (Y-1)*50 +4, anchor=NW,image=un)
    elif grillejeu[X][Y]==2:
        can.create_image((X-1)*50 +7, (Y-1)*50 +4, anchor=NW,image=deux)
    elif grillejeu[X][Y]==3:
        can.create_image((X-1)*50 +7, (Y-1)*50 +4, anchor=NW,image=trois)
    elif grillejeu[X][Y]==4:
        can.create_image((X-1)*50 +7, (Y-1)*50 +4, anchor=NW,image=quatre)
    elif grillejeu[X][Y]==5:
        can.create_image((X-1)*50 +7, (Y-1)*50 +4, anchor=NW,image=cinq)
    elif grillejeu[X][Y]==6:
        can.create_image((X-1)*50 +7, (Y-1)*50 +4, anchor=NW,image=six)
    elif grillejeu[X][Y]==7:
        can.create_image((X-1)*50 +7, (Y-1)*50 +1, anchor=NW,image=sept)
    elif grillejeu[X][Y]==8:
        can.create_image((X-1)*50 +9, (Y-1)*50 +4, anchor=NW,image=huit)

    for i in range(X-1,X+2):
          for j in range(Y-1,Y+2):
               if(grillejeu[i][j] == '*' and i in range(1,10) and j in range(1,10) and grillemines[X][Y] == 0):
                    casemines(i,j)
    else:
         return None 
    




#################### DRAPEAU #####################



def drapeau (event) :
    global grillemines
    global compteur
    x = event.x//50 +1 
    y = event.y//50 +1
    if grillejeu[x][y]=="*":
         grillejeu[x][y]="!"
         can.create_image((x-1)*50 +7, (y-1)*50 +7, anchor=NW, image=drapeauimage)#on ajuste la position de l'image en fonction de sa taille
         
         compteur -= 1
         
    
    elif grillejeu[x][y]=="!":
         grillejeu[x][y]="*"
         can.create_rectangle((x-1)*50, (y-1)*50, x*50, y*50, fill='grey')
         compteur += 1
         

    else:
        nbmines.configure(text="Nous ne pouvez pas poser de drapeau sur cette case")
        
    nbmines.configure(text="Il reste "+str(compteur)+" mines")

    endgame(grillemines)
    

def endgame (t):

    if compteur==0:
    
        for i in range(1,10):
            for j in range(1,10):
                if grillejeu[i][j]=="!":
                    lignedrapeau[i]=i
                    colonedrapeau[j]=j
                    

        for i in range(1,10):
            for j in range(1,10):
                if grillemines[i][j]=="M":
                    lignemines[i]=i
                    colonemines[j]=j

        confirm(grillemines)


def confirm(t):
    if lignedrapeau==lignemines and colonedrapeau==colonemines:
        fenetrevictoire()
    else:
        nbmines.configure(text="Les drapeaux ne sont pas placés au bon endroit, réessayez !")
          
          
    
##################################################
############# PROGRAMME PRINCIPAL ################
##################################################




def fenetredefaite ():
    fen.destroy()
    fenetredefaite = Tk()
    textedefaite = Label(fenetredefaite, text="Vous avez perdu !")
    textedefaite.pack()
    boutonquitter = Button(fenetredefaite, text="quitter", command=fenetredefaite.destroy)
    boutonquitter.pack()
    fenetredefaite.mainloop()
    
    
def fenetrevictoire ():
    fen.destroy()
    fenetrevictoire = Tk()
    textevictoire = Label (fenetrevictoire, text="Vous avez gagné ! Félicitations !")
    textevictoire.pack()
    boutonquitterv = Button(fenetrevictoire, text="quitter", command=fenetrevictoire.destroy)
    boutonquitterv.pack()
    fenetrevictoire.mainloop()
    
    
    


##################################################
##################### GUI ########################
##################################################

fen = Tk()
fen.title("Démineur ")
can = Canvas (fen,width = 450, height = 450, bg = 'grey') #Canevas de 1800*1800
for i in range (0,9):
    for j in range (0,9):
        can.create_rectangle(i*50, j*50, (i+1)*50, (j+1)*50) #Creation de la grille, rectangles de 200*200

mine = PhotoImage(file="mine.gif")
drapeauimage = PhotoImage(file="drapeau.gif")
un = PhotoImage(file="un.gif")
deux = PhotoImage(file="deux.gif")
trois = PhotoImage(file="trois.gif")
quatre = PhotoImage(file="quatre.gif")
cinq = PhotoImage(file="cinq.gif")
six = PhotoImage(file="six.gif")
sept = PhotoImage(file="sept.gif")
huit = PhotoImage(file="huit.gif")

can.bind("<Button-1>",creuser) #on associe le clic gauche "bind.button-1" a la fonction creuser
can.bind("<Button-3>",drapeau) #on associe le clic gauche "bind.button-3" a la fonction drapeau
can.pack()

nbmines = Label(fen)

nbmines.pack()


fen.mainloop()


