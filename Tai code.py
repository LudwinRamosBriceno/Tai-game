import pygame
from tkinter import *
from PIL import ImageTk, Image
import random
import time
import threading

from pygame.constants import DROPFILE

#Main window
board = Tk()
# Window size and name
board.geometry("1000x700")
board.resizable(height=False, width=False)
board.title("Tai: the little zombie")
board.iconbitmap("zombie.ico")

screen_width = board.winfo_screenwidth()
screen_height = board.winfo_screenheight()

#Screen size
width = 1000
height = 700

x_screen = (screen_width / 2) - (width / 2)
y_screen = (screen_height / 2) - (height / 2)

board.geometry(f'{width}x{height}+{int(x_screen)}+{int(y_screen)}')
board.resizable(False, False)

# "x" to move the airplane for "right and left"
x=10
# "y" to move the airplane for "UP and DOWN"
y=10

# Speeds class for enemies

class Class_enemies:
    def __init__(self):
        self.xpos = random.randint(0, 850)
        self.ypos = -200  #random.randint(0, 700)
        self.xspeed = 0 #random.randint(1, 20)
        self.yspeed = 12 #random.randint(1, 20)

#Transistors from main screen to any level
pasar1=False
pasar2=False
pasar3=False

#Parametros de puntuaciones
Score_final=0
Bono_final=0
Bono1=0
Bono2=0
Bono3=0

# sounds

pygame.mixer.init()
sonido_passlevel= pygame.mixer.Sound("POKEMON Level Up.mp3")
Press_botton=pygame.mixer.Sound("Boton.mp3")
sound_enem=pygame.mixer.Sound("Cartoon Bounce.mp3")
#sound_enem3=pygame.mixer.Sound("Apagando sistema.mp3")
#sound_enem1=pygame.mixer.Sound("Alien Apagado.mp3")

#################################################################################################
"FINAL SCREEN"
#################################################################################################

"Level 3 register function"
def Final_register():
    global puntaje_final,Score
    suma_final= Score + Bono2 + Bono1 + Bono3
    puntaje_final=str(suma_final)

    # save name 
    file_final = open("player.txt", "a")
    file_final.write(Player +"\t"+ puntaje_final + "\n")
    file_final.close()
    final_to_mainscreen()

def final_to_mainscreen():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Ghostly Mansion.mp3")
    pygame.mixer.music.play(100)
    global salir3,Score_final,Bono_final
    Press_botton.play()
    Score_final=0
    Bono_final=0
    salir3=False
    final.destroy()
    main_screen()

def final_screen():
    global final,Level_3,Score_final,Bono_final,Bono1,Bono2,Bono3
    Press_botton.play()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("MELANCHOLI.mp3")
    pygame.mixer.music.play(10)
    Level_3.destroy()
    puntaje_final=0
    Bono_final=0
    Bono_final= Bono1 + Bono2 + Bono3
    puntaje_final= Score + Bono1 + Bono2 + Bono3
    img_final= ImageTk.PhotoImage(Image.open("Final screen.jpg").resize((1000,700)))
    final = Canvas(board,height = height, width = width)
    final.pack()
    img_final3= final.create_image(0,0,anchor=NW, image=img_final)
    table= Label(final,borderwidth=10,relief="sunken",bg="black",anchor=N, 
    text= '¡Enhorabuena! \n\n Puntaje: {} \n\n Bono: {} \n\n Puntaje total: {} \n\n\n Presiona el botón para regresar'.format(Score,Bono_final,puntaje_final),height=12,width=40,fg="white",font=("Courier",13))
    table.place(x=270,y=250)
    img_back_finalbutton= ImageTk.PhotoImage(Image.open("destroy.png").resize((60,60)))
    back_finalbutton=Button(final,image=img_back_finalbutton,bd=5,bg="darkgrey", font=("Franklin Gothic Medium",15 ), command=Final_register)
    back_finalbutton.place(x= 450, y= height/2+190)

    final.mainloop()


#################################################################################################
"LEVEL 3"
#################################################################################################

"Functions to leave and stop game 3"

# Come back from game screen to main screen by press "salir" button
def Screen_Level_3_to_mainscreen():
    Press_botton.play()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Ghostly Mansion.mp3")
    pygame.mixer.music.play(100)
    global Score, Life3, Time3,Marcadores3,salir3
    salir3=False
    Score=0
    Time3=0
    Life3=3
    Marcadores3.config(text="Score: {} \n   Time: {} seg \n Life:{}".format(Score, Time3,Life3))
    Villanos3.isDaemon
    Level_3.unbind_all("<Key>")
    Level_3.destroy()
    main_screen()

#Stop game function to press "pausa" button
def detener3():
    Press_botton.play()
    global pausa3
    pausa3=not pausa3
    if pausa3==False:
        pygame.mixer.music.pause()
    if pausa3==True:
        pygame.mixer.music.unpause()


"Transition functions from level 3 to final screen"

def cambiara_final():
    global pase_nivel3
    if pase_nivel3==False:
        pase_nivel3=True
        Villanos3.isDaemon
        return transiciona_final()
    else:
        board.after(10,cambiara_final)

def transiciona_final():
    pygame.mixer.music.stop()
    sonido_passlevel.play()
    continue_nivel3= Label(Level_3,borderwidth=10,relief="sunken",bg="black",anchor=N, text= "¡FELICIDADES! ¡HAS VENCIDO AL MIEDO!",height=4,width=50,fg="white",font=("Courier",13))
    continue_nivel3.place(x=230,y=300)
    continue_to_level3=Button(continue_nivel3,padx=10,pady=4,bd=5,bg="darkgrey", text = "Continuar", font=("Franklin Gothic Medium",10 ), command=final_screen)
    continue_to_level3.place(x=200 /2+120, y=200 /2-70)

"Level 3 register function"
def Level3_register():
    global puntaje,Score
    suma= Score + Bono2 + Bono1 + Bono3
    puntaje=str(suma)

    # save name 
    file = open("player.txt", "a")
    file.write(Player +"\t"+ puntaje + "\n")
    file.close()
    pantalla_derrota3_inicio()

" Level 3 Defeat Screen"

# Transitory function to pass from defeat screen to main screen
def pantalla_derrota3_inicio():
    Press_botton.play()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Ghostly Mansion.mp3")
    pygame.mixer.music.play(100)
    global Score, Time3,Life3
    Score=0
    Time3=0
    Life3=3
    derrota_canv3.destroy()
    main_screen()

# Function to pass from level 3 screen to defeat screen
def cambiar_a_derrota3():
    global transition3,Villanos3
    if not transition3:
        Level_3.destroy()
        Villanos3.isDaemon
        return derrota3()
    else:
        board.after(10,cambiar_a_derrota3)

def derrota3():
    global derrota_canv3,Score
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Candyman Theme.mp3")
    pygame.mixer.music.play(100)
    img_derrota3= ImageTk.PhotoImage(Image.open("Defeat.jpg").resize((1000,700)))
    img_words_derrota3= ImageTk.PhotoImage(Image.open("Derrota words.png").resize((600,250)))
    img_titulo_derrota3= ImageTk.PhotoImage(Image.open("titulo derrota.png").resize((600,300)))
    derrota_canv3= Canvas(board, width=width, height=height)
    derrota_canv3.pack()
    derrota_canv3.create_image(0,0,anchor=NW, image=img_derrota3)
    derrota_canv3.create_image(50,220,anchor=NW, image=img_words_derrota3)
    titulo_derrota3 = derrota_canv3.create_image(50,40,anchor=NW, image=img_titulo_derrota3)
    score_nivel3= Label(derrota_canv3,borderwidth=10,relief="sunken",bg="black",anchor=N, text= "Score: {}".format(Score),height=1,width=15,fg="white",font=("Courier",13))
    score_nivel3.place(x=250,y=400)
    img_volver_button3= ImageTk.PhotoImage(Image.open("destroy.png").resize((75,75)))
    back_botton3=Button(derrota_canv3,image=img_volver_button3,bd=5,bg="darkgrey", font=("Franklin Gothic Medium",15 ), command=Level3_register)
    back_botton3.place(x= 285, y= height/2+150)
    derrota_canv3.mainloop()

" Level 3 collisions"
def collision3(bats,ball):
    global Life3, Marcadores3,transition3,Time3,Life3,punto_choque3,enemigos3_list,enemigo3_object
    choque_bats=Level_3.bbox(bats)
    choque_zombie3= Level_3.bbox(zombie3)

    if choque_zombie3[0] < choque_bats[2] and choque_zombie3[2] > choque_bats[0] and choque_zombie3[1] < choque_bats[3] and choque_zombie3[3] > choque_bats[1] and punto_choque3==True:
        Life3-=1
        Marcadores3.config(text="Score: {} \n   Time: {} seg \n Life:{}".format(Score, Time3,Life3))
        punto_choque3=False
        enemigo3_object.remove(bats)
        enemigos3_list.remove(ball)
        Level_3.delete(bats)

    if Life3<=0:
        Life3=0
        Marcadores3.config(text="Score: {} \n   Time: {} seg \n Life:{}".format(Score, Time3,Life3))
        enemigos3_list=[]
        enemigo3_object=[]
        transition3=False
        
# Function to move the objects (bats)
def mover_enemigos3():
    global Time3,Score,Bono3,Marcadores3,pausa3,salir3,enemigos3_list,punto_choque3,enemigo3_object,transition3,pase_nivel3,Life3
    pase_nivel3=True
    transition3=True
    punto_choque3=True
    esperar3=0
    cont3=0
    segundos=0
    pausa3=True
    salir3=True
    x_enemigos3=random.choice(range(2,9))
    enemigos3_list=[]   # keeps track of objects
    enemigo3_object = []      # keeps track of objects representation on the Canvas
    image_enemigos3= ImageTk.PhotoImage(Image.open("enemy3.png").resize((125,100)))
    for i in range(5):
        enemigo3_var = Class_enemies()
        enemigos3_list+=[enemigo3_var]
        enemigo3_object+=[Level_3.create_image(enemigo3_var.xpos,enemigo3_var.ypos,anchor=NW, image=image_enemigos3)]
    while transition3 and pase_nivel3 and salir3:
        if pausa3:
            
            for b, ball in zip(enemigo3_object, enemigos3_list):
                
                Level_3.move(b,ball.xspeed,ball.yspeed)
                
                x_enemigos3, y_enemigos3 =Level_3.coords(b)
                
                if cont3>=1:
                    if y_enemigos3 >= height-120:
                        sound_enem.play()
                        ball.yspeed = random.randint(-14,-1)
                        ball.xspeed = random.randint(-14,14)
                        
                    if y_enemigos3 <= 0:
                        sound_enem.play()
                        ball.yspeed = random.randint(1,14)
                        ball.xspeed = random.randint(-14,14)
                        
                    if x_enemigos3 >= 850:
                        sound_enem.play()
                        ball.xspeed = random.randint(-14,-1)
                        ball.yspeed = random.randint(-14,14)
                        
                    if x_enemigos3 <= 0:
                        sound_enem.play()
                        ball.xspeed = random.randint(1,14)
                        ball.yspeed = random.randint(-14,14)
                    
                    collision3(b,ball)

                if y_enemigos3 >= height-120 and cont3==0:
                    cont3+=1
            board.update()
            time.sleep(0.03)
            segundos+=1
            if punto_choque3 ==False:
                    esperar3+=1    
            if esperar3>=16:
                esperar3=0
                punto_choque3=True
            if segundos==1000:
                segundos=100
            if segundos%32==0:
                Time3+=1
                Score+=5
                Marcadores3.config(text="Score: {} \n   Time: {} seg \n Life:{}".format(Score, Time3,Life3))
                if Life3==3 and Time3==20 or Time3==50:
                    Bono3+=20
                
            if Time3>=60:
                enemigos3_list=[]
                enemigo3_object=[]
                Life3=0
                pase_nivel3=False
                
        else:
            time.sleep(0.01)
    
    if Time3>=60:
        Level_3.unbind_all("<Key>")
    elif Life3<=0:
        transition3=False
        Level_3.unbind_all("<Key>")
        

def Screen_Level_3():
    global Level_3, zombie3,enemigos3,Villanos3,marcador_puntaje3,marcador_nombre_canv3,Marcadores3,Time3,Life3,Score,Bono3,pasar3
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Midnight Wood.mp3")
    pygame.mixer.music.play(100)
    if pasar3:
        background.destroy()
        pasar3=False
    else:
        Press_botton.play()
        Level_2.destroy()

    #Scoreboards of Level 3
    Bono3=0
    Score = 0
    Time3 = 0
    Life3 = 3
    
    # Level 3 Canvas creation
    imagen3 = ImageTk.PhotoImage(Image.open("graveyard.png"))
    Level_3= Canvas(board, width=width, height=height)
    Level_3.pack()
    Level_3.create_image(0,0,anchor=NW, image=imagen3)

    # Level 3 Scoreboard 
    marcador_nombre_img3 = ImageTk.PhotoImage(Image.open("cartel nombre.png").resize((350,150)))
    marcador_puntaje_img3 = ImageTk.PhotoImage(Image.open("Marcadores.png").resize((300,150)))
    marcador_nombre_canv3= Level_3.create_image(200,-10,anchor=NW, image=marcador_nombre_img3)
    marcador_puntaje3= Level_3.create_image(-20,-20,anchor=NW, image=marcador_puntaje_img3)
    Marcadores3= Label(Level_3,bg="black",fg="White", text="Score: {}\n   Time: {} seg \n Life:{}".format(Score, Time3,Life3),font=("Courier",11))
    Marcadores3.place(x=50,y=45)
    Marcador_nombre3= Label(Level_3,bg="black",fg="White", text="{}".format(Player),font=("Courier",11))
    Marcador_nombre3.place(x=280,y=55)
    # Stop and exit buttons
    salir_boton3=Button(Level_3,bd=5,bg="lightGoldenrod3", text = "   ¡salir!   ", font=("Franklin Gothic Medium",10 ), command=Screen_Level_3_to_mainscreen)
    salir_boton3.place(x= 530, y= 30)
    detener_boton3=Button(Level_3,bd=5,bg="lightGoldenrod3", text = "   ¡Pausa!   ", font=("Franklin Gothic Medium",8 ), command=detener3)
    detener_boton3.place(x= 530, y= 70)
    # Player's airplane 
    zombie_img3 = ImageTk.PhotoImage(Image.open("player.png").resize((70,100)))
    zombie3= Level_3.create_image(400,450,anchor=NW, image=zombie_img3)
    #caracter del enemigo
    #image_enemigos1= ImageTk.PhotoImage(Image.open("enemy1.png"))#.resize((150,125)))
    #enemigos1= Level_1.create_image(200,0,anchor=NW, image=image_enemigos1,tags="enemigos1")
    
    #move user airplane 
    Level_3.bind_all("<Key>",mover3)
    
    #move enemies of level 3
    Villanos3= threading.Thread(target=mover_enemigos3)
    Villanos3.start()

    #Functions to change to the different screens from level 3 
    cambiar_a_derrota3()
    cambiara_final()

    Level_3.mainloop()


"GAME CONTROLS of level 3"
#Control to move the user airplane
#<>
def mover3(event):
    x1, y1= Level_3.coords(zombie3)
    if event.keysym=='Left' and pausa3:
        if x1<=10:
            x1=10
            Level_3.coords(zombie3, x1,y1)
        Level_3.coords(zombie3, x1-x,y1)
    elif event.keysym=="Right" and pausa3:
        if x1 >= 916:
            x1=916
            Level_3.coords(zombie3, x1,y1)
        Level_3.coords(zombie3, x1+x,y1)
    elif event.keysym=="Up" and pausa3:
        if y1<=10:
            y1=10
            Level_3.coords(zombie3, x1,y1)
        Level_3.coords(zombie3, x1,y1-y)
    elif event.keysym=="Down" and pausa3:
        if y1 >= height-110:
            y1=height-110
            Level_3.coords(zombie3, x1,y1)
        Level_3.coords(zombie3, x1,y1+y)



#################################################################################################
"LEVEL 2"
#################################################################################################

"Functions to leave and stop game 2"

# Come back from game screen to main screen by press "salir" button
def Screen_Level_2_to_mainscreen():
    Press_botton.play()
    global Score, Life2, Time2,Marcadores2,salir2
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Ghostly Mansion.mp3")
    pygame.mixer.music.play(100)
    salir2=False
    Score=0
    Time2=0
    Life2=3
    Marcadores2.config(text="Score: {} \n   Time: {} seg \n Life:{}".format(Score, Time2,Life2))
    Villanos2.isDaemon
    Level_2.unbind_all("<Key>")
    Level_2.destroy()
    main_screen()

#Stop game function to press "pausa" button
def detener2():
    Press_botton.play()
    global pausa2
    pausa2=not pausa2
    if pausa2==False:
        pygame.mixer.music.pause()
    if pausa2==True:
        pygame.mixer.music.unpause()


"Transition functions from level 2 to level 3"

def cambiara_nivel2():
    global pase_nivel2
    if pase_nivel2==False:
        pase_nivel2=True
        Villanos2.isDaemon
        return transiciona_nivel2()
    else:
        board.after(10,cambiara_nivel2)

def transiciona_nivel2():
    pygame.mixer.music.stop()
    sonido_passlevel.play()
    continue_nivel2= Label(Level_2,borderwidth=10,relief="sunken",bg="black",anchor=N, text= "¡FELICIDADES! ¿Listo para el siguiente reto?",height=4,width=50,fg="white",font=("Courier",13))
    continue_nivel2.place(x=230,y=300)
    continue_to_level2=Button(continue_nivel2,padx=10,pady=4,bd=5,bg="darkgrey", text = "Continuar", font=("Franklin Gothic Medium",10) , command=Screen_Level_3)
    continue_to_level2.place(x=200 /2+120, y=200 /2-70)

"Level 2 register function"
def Level2_register():
    global puntaje,Score
    suma= Score + Bono2 + Bono1
    puntaje=str(suma)

    # save name 
    file = open("player.txt","a")
    file.write(Player +"\t"+ puntaje + "\n")
    file.close()
    pantalla_derrota2_inicio()

" Level 1 Defeat Screen"

# Transitory function to pass from defeat screen to main screen
def pantalla_derrota2_inicio():
    Press_botton.play()
    global Score, Time2,Life2
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Ghostly Mansion.mp3") 
    pygame.mixer.music.play(100)
    Score=0
    Time2=0
    Life2=3
    derrota_canv2.destroy()
    main_screen()

# Function to pass from level 2 screen to defeat screen
def cambiar_a_derrota2():
    global transition2,Villanos2
    if not transition2:
        Level_2.destroy()
        Villanos2.isDaemon
        return derrota2()
    else:
        board.after(10,cambiar_a_derrota2)

def derrota2():
    global derrota_canv2,Score
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Candyman Theme.mp3")
    pygame.mixer.music.play(100)
    img_derrota2= ImageTk.PhotoImage(Image.open("Defeat.jpg").resize((1000,700)))
    img_words_derrota2= ImageTk.PhotoImage(Image.open("Derrota words.png").resize((600,250)))
    img_titulo_derrota2= ImageTk.PhotoImage(Image.open("titulo derrota.png").resize((600,300)))
    derrota_canv2= Canvas(board, width=width, height=height)
    derrota_canv2.pack()
    derrota_canv2.create_image(0,0,anchor=NW, image=img_derrota2)
    derrota_canv2.create_image(50,220,anchor=NW, image=img_words_derrota2)
    titulo_derrota2 = derrota_canv2.create_image(50,40,anchor=NW, image=img_titulo_derrota2)
    score_nivel2= Label(derrota_canv2,borderwidth=10,relief="sunken",bg="black",anchor=N, text= "Score: {}".format(Score),height=1,width=15,fg="white",font=("Courier",13))
    score_nivel2.place(x=250,y=400)
    img_volver_button2= ImageTk.PhotoImage(Image.open("destroy.png").resize((75,75)))
    back_botton2=Button(derrota_canv2,image=img_volver_button2,bd=5,bg="darkgrey", font=("Franklin Gothic Medium",15 ), command=Level2_register)
    back_botton2.place(x= 285, y= height/2+150)
    derrota_canv2.mainloop()

" Level 2 collisions"
def collision2(fantasmas,ball):
    global Life2, Marcadores2,transition2,Time2,Life2,punto_choque2,enemigos2_list,enemigo2_object
    choque_fantasmas=Level_2.bbox(fantasmas)
    choque_zombie2= Level_2.bbox(zombie2)

    if choque_zombie2[0] < choque_fantasmas[2] and choque_zombie2[2] > choque_fantasmas[0] and choque_zombie2[1] < choque_fantasmas[3] and choque_zombie2[3] > choque_fantasmas[1] and punto_choque2==True:
        Life2-=1
        Marcadores2.config(text="Score: {} \n   Time: {} seg \n Life:{}".format(Score, Time2,Life2))
        punto_choque2=False
        enemigo2_object.remove(fantasmas)
        enemigos2_list.remove(ball)
        Level_2.delete(fantasmas)

    if Life2<=0:
        Life2=0
        Marcadores2.config(text="Score: {} \n   Time: {} seg \n Life:{}".format(Score, Time2,Life2))
        enemigos2_list=[]
        enemigo2_object=[]
        transition2=False
        
# Function to move the objects (Ghosts)
def mover_enemigos2():
    global Time2,Score,Bono2,Marcadores2,pausa2,salir2,enemigos2_list,punto_choque2,enemigo2_object,transition2,pase_nivel2,Life2
    pase_nivel2=True
    transition2=True
    punto_choque2=True
    esperar2=0
    cont2=0
    segundos=0
    pausa2=True
    salir2=True
    x_enemigos2=random.choice(range(2,9))
    enemigos2_list=[]   # keeps track of objects
    enemigo2_object = []      # keeps track of objects representation on the Canvas
    image_enemigos2= ImageTk.PhotoImage(Image.open("enemy2.png").resize((125,100)))
    for i in range(4):
        enemigo2_var = Class_enemies()
        enemigos2_list+=[enemigo2_var]
        enemigo2_object+=[Level_2.create_image(enemigo2_var.xpos,enemigo2_var.ypos,anchor=NW, image=image_enemigos2)]
    while transition2 and pase_nivel2 and salir2:
        if pausa2:
            
            for b, ball in zip(enemigo2_object, enemigos2_list):
                
                Level_2.move(b,ball.xspeed,ball.yspeed)
                
                x_enemigos2, y_enemigos2 =Level_2.coords(b)
                
                if cont2>=1:
                    if y_enemigos2 >= height-120:
                        sound_enem.play()
                        ball.yspeed = random.randint(-14,-1)
                        ball.xspeed = random.randint(-14,14)
                        
                    if y_enemigos2 <= 0:
                        sound_enem.play()
                        ball.yspeed = random.randint(1,14)
                        ball.xspeed = random.randint(-14,14)
                        
                    if x_enemigos2 >= 850:
                        sound_enem.play()
                        ball.xspeed = random.randint(-14,-1)
                        ball.yspeed = random.randint(-14,14)
                        
                    if x_enemigos2 <= 0:
                        sound_enem.play()
                        ball.xspeed = random.randint(1,14)
                        ball.yspeed = random.randint(-14,14)
                    
                    collision2(b,ball)

                if y_enemigos2 >= height-120 and cont2==0:
                    cont2+=1
            board.update()
            time.sleep(0.03)
            segundos+=1
            if punto_choque2 ==False:
                    esperar2+=1    
            if esperar2>=16:
                esperar2=0
                punto_choque2=True
            if segundos==1000:
                segundos=100
            if segundos%32==0:
                Time2+=1
                Score+=3
                Marcadores2.config(text="Score: {} \n   Time: {} seg \n Life:{}".format(Score, Time2,Life2))
                if Life2==3 and Time2==20 or Time2==50:
                    Bono2+=20
                
            if Time2>=60:
                enemigos2_list=[]
                enemigo2_object=[]
                Life2=0
                pase_nivel2=False
                
        else:
            time.sleep(0.01)
    
    if Time2>=60:
        Level_2.unbind_all("<Key>")
    elif Life2<=0:
        transition2=False
        Level_2.unbind_all("<Key>")
        

def Screen_Level_2():
    global Level_2, zombie2,enemigos2,Villanos2,marcador_puntaje2,marcador_nombre_canv2,Marcadores2,Time2,Life2,Score,Bono2,pasar2
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Halloween Music Witch.mp3")
    pygame.mixer.music.play(100)
    if pasar2:
        Bono2=0
        background.destroy()
        pasar2=False
    else:
        Press_botton.play()
        Level_1.destroy()

    #Scoreboards of Level 2
    Bono2=0
    Score = 0
    Time2 = 0
    Life2 = 3
    
    # Level 2 Canvas creation
    imagen2 = ImageTk.PhotoImage(Image.open("house.png"))
    Level_2= Canvas(board, width=width, height=height)
    Level_2.pack()
    Level_2.create_image(0,0,anchor=NW, image=imagen2)

    # Level 2 Scoreboard 
    marcador_nombre_img2 = ImageTk.PhotoImage(Image.open("cartel nombre.png").resize((350,150)))
    marcador_puntaje_img2 = ImageTk.PhotoImage(Image.open("Marcadores.png").resize((300,150)))
    marcador_nombre_canv2= Level_2.create_image(200,-10,anchor=NW, image=marcador_nombre_img2)
    marcador_puntaje2= Level_2.create_image(-20,-20,anchor=NW, image=marcador_puntaje_img2)
    Marcadores2= Label(Level_2,bg="black",fg="White", text="Score: {}\n   Time: {} seg \n Life:{}".format(Score, Time2,Life2),font=("Courier",11))
    Marcadores2.place(x=50,y=45)
    Marcador_nombre2= Label(Level_2,bg="black",fg="White", text="{}".format(Player),font=("Courier",11))
    Marcador_nombre2.place(x=280,y=55)
    # Stop and exit buttons
    salir_boton2=Button(Level_2,bd=5,bg="lightGoldenrod3", text = "   ¡salir!   ", font=("Franklin Gothic Medium",10 ), command=Screen_Level_2_to_mainscreen)
    salir_boton2.place(x= 530, y= 30)
    detener_boton2=Button(Level_2,bd=5,bg="lightGoldenrod3", text = "   ¡Pausa!   ", font=("Franklin Gothic Medium",8 ), command=detener2)
    detener_boton2.place(x= 530, y= 70)
    # Player's airplane 
    zombie_img2 = ImageTk.PhotoImage(Image.open("player.png").resize((70,100)))
    zombie2= Level_2.create_image(400,450,anchor=NW, image=zombie_img2)
    
    #move user airplane 
    Level_2.bind_all("<Key>",mover2)
    
    #move enemies of level 2
    Villanos2= threading.Thread(target=mover_enemigos2)
    Villanos2.start()

    #Functions to change to the different screens from level 2 
    cambiar_a_derrota2()
    cambiara_nivel2()

    Level_2.mainloop()


"GAME CONTROLS of level 2"
#Control to move the user airplane
#<>
def mover2(event):
    x1, y1= Level_2.coords(zombie2)
    if event.keysym=='Left' and pausa2:
        if x1<=10:
            x1=10
            Level_2.coords(zombie2, x1,y1)
        Level_2.coords(zombie2, x1-x,y1)
    elif event.keysym=="Right" and pausa2:
        if x1 >= 916:
            x1=916
            Level_2.coords(zombie2, x1,y1)
        Level_2.coords(zombie2, x1+x,y1)
    elif event.keysym=="Up" and pausa2:
        if y1<=10:
            y1=10
            Level_2.coords(zombie2, x1,y1)
        Level_2.coords(zombie2, x1,y1-y)
    elif event.keysym=="Down" and pausa2:
        if y1 >= height-110:
            y1=height-110
            Level_2.coords(zombie2, x1,y1)
        Level_2.coords(zombie2, x1,y1+y)



#################################################################################################
"LEVEL 1"
#################################################################################################

"Functions to leave and stop game 1"

# Come back from game screen to main screen by press "salir" button
def Screen_Level_1_to_mainscreen():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Ghostly Mansion.mp3") 
    pygame.mixer.music.play(100)
    Press_botton.play()
    global Score, Life1, Time1,Marcadores1,salir1
    salir1=False
    Score=0
    Time1=0
    Life1=3
    Marcadores1.config(text="Score: {} \n   Time: {} seg \n Life:{}".format(Score, Time1,Life1))
    Villanos1.isDaemon
    Level_1.unbind_all("<Key>")
    Level_1.destroy()
    main_screen()

#Stop game function to press "pausa"
def detener1():
    Press_botton.play()
    global pausa1
    pausa1=not pausa1
    if pausa1==False:
        pygame.mixer.music.pause()
    if pausa1==True:
        pygame.mixer.music.unpause()


"Transition from level 1 to level 2"

def cambiara_nivel1():
    global pase_nivel1
    if pase_nivel1==False:
        pase_nivel1=True
        Villanos1.isDaemon
        return transicion_nivel1()
    else:
        board.after(10,cambiara_nivel1)

def transicion_nivel1():
    pygame.mixer.music.stop()
    sonido_passlevel.play()
    continue_nivel= Label(Level_1,borderwidth=10,relief="sunken",bg="black",anchor=N, text= "¡FELICIDADES! ¿Listo para el siguiente reto?",height=4,width=50,fg="white",font=("Courier",13))
    continue_nivel.place(x=230,y=300)
    continue_to_level=Button(continue_nivel,padx=10,pady=4,bd=5,bg="darkgrey", text = "Continuar", font=("Franklin Gothic Medium",10 ), command=Screen_Level_2)
    continue_to_level.place(x=200 /2+120, y=200 /2-70)

"Level 1 register function"
def Level1_register():
    global puntaje,Score
    suma= Score + Bono1
    puntaje=str(suma)

    # save name 
    file = open("player.txt", "a")
    file.write(Player +"\t"+ puntaje + "\n")
    file.close()
    pantalla_derrota1_inicio()

" Level 1 Defeat Screen"

# Transitory function to pass from defeat screen to main screen
def pantalla_derrota1_inicio():
    Press_botton.play()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Ghostly Mansion.mp3") 
    pygame.mixer.music.play(100)
    global Score, Time1,Life1
    Score=0
    Time1=0
    Life1=3
    derrota_canv1.destroy()
    main_screen()

# Function to pass from level 1 screen to defeat screen
def cambiar_a_derrota1():
    global transition1,Villanos1
    if not transition1:
        Level_1.destroy()
        Villanos1.isDaemon
        return derrota1()
    else:
        board.after(10,cambiar_a_derrota1)

def derrota1():
    global derrota_canv1,Score
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Candyman Theme.mp3")
    pygame.mixer.music.play(100)
    img_derrota= ImageTk.PhotoImage(Image.open("Defeat.jpg").resize((1000,700)))
    img_words_derrota= ImageTk.PhotoImage(Image.open("Derrota words.png").resize((600,250)))
    img_titulo_derrota= ImageTk.PhotoImage(Image.open("titulo derrota.png").resize((600,300)))
    derrota_canv1= Canvas(board, width=width, height=height)
    derrota_canv1.pack()
    derrota_canv1.create_image(0,0,anchor=NW, image=img_derrota)
    derrota_canv1.create_image(50,220,anchor=NW, image=img_words_derrota)
    titulo_derrota = derrota_canv1.create_image(50,40,anchor=NW, image=img_titulo_derrota)
    score_nivel1= Label(derrota_canv1,borderwidth=10,relief="sunken",bg="black",anchor=N, text= "Score: {}".format(Score),height=1,width=15,fg="white",font=("Courier",13))
    score_nivel1.place(x=250,y=400)
    img_volver_button= ImageTk.PhotoImage(Image.open("destroy.png").resize((75,75)))
    back_botton1=Button(derrota_canv1,image=img_volver_button,bd=5,bg="darkgrey", font=("Franklin Gothic Medium",15 ), command=Level1_register)
    back_botton1.place(x= 285, y= height/2+150)
    derrota_canv1.mainloop()

" Level 1 collisions"
def collision1(calabazas,ball):
    global Life1, Marcadores1,transition1,Time1,Life1,punto_choque1,enemigos1_list,enemigo1_object
    choque_calabazas=Level_1.bbox(calabazas)
    choque_zombie= Level_1.bbox(zombie1)

    if choque_zombie[0] < choque_calabazas[2] and choque_zombie[2] > choque_calabazas[0] and choque_zombie[1] < choque_calabazas[3] and choque_zombie[3] > choque_calabazas[1] and punto_choque1==True:
        Life1-=1
        Marcadores1.config(text="Score: {} \n   Time: {} seg \n Life:{}".format(Score, Time1,Life1))
        punto_choque1=False
        enemigo1_object.remove(calabazas)
        enemigos1_list.remove(ball)
        Level_1.delete(calabazas)

    if Life1<=0:
        Life1=0
        Marcadores1.config(text="Score: {} \n   Time: {} seg \n Life:{}".format(Score, Time1,Life1))
        enemigos1_list=[]
        enemigo1_object=[]
        transition1=False
        
# Function to move the objects (pumpkins)
def mover_enemigos1():
    global Time1,Score,Bono1,Marcadores1,pausa1,salir1,enemigos1_list,punto_choque1,enemigo1_object,transition1,pase_nivel1,Life1
    pase_nivel1=True
    transition1=True
    punto_choque1=True
    esperar1=0
    cont1=0
    segundos=0
    pausa1=True
    salir1=True
    x_enemigos1=random.choice(range(2,9))
    enemigos1_list=[]   # keeps track of objects
    enemigo1_object = []      # keeps track of objects representation on the Canvas
    image_enemigos1= ImageTk.PhotoImage(Image.open("enemy1.png").resize((150,125)))
    for i in range(3):
        enemigo1_var = Class_enemies()
        enemigos1_list+=[enemigo1_var]
        enemigo1_object+=[Level_1.create_image(enemigo1_var.xpos,enemigo1_var.ypos,anchor=NW, image=image_enemigos1)]
    while transition1 and pase_nivel1 and salir1:
        if pausa1:
            #print(enemigo1_object)
            for b, ball in zip(enemigo1_object, enemigos1_list):
                #box_enemigos1=Level_1.bbox(b)
                Level_1.move(b,ball.xspeed,ball.yspeed)
                
                x_enemigos1, y_enemigos1 =Level_1.coords(b)
                
                if cont1>=1:
                    if y_enemigos1 >= height-120:
                        sound_enem.play()
                        ball.yspeed = random.randint(-14,-1)
                        ball.xspeed = random.randint(-14,14)
                        
                    if y_enemigos1 <= 0:
                        sound_enem.play()
                        ball.yspeed = random.randint(1,14)
                        ball.xspeed = random.randint(-14,14)
                        
                    if x_enemigos1 >= 850:
                        sound_enem.play()
                        ball.xspeed = random.randint(-14,-1)
                        ball.yspeed = random.randint(-14,14)
                        
                    if x_enemigos1 <= 0:
                        sound_enem.play()
                        ball.xspeed = random.randint(1,14)
                        ball.yspeed = random.randint(-14,14)
                    
                    collision1(b,ball)

                if y_enemigos1 >= height-120 and cont1==0:
                    cont1+=1
            board.update()
            time.sleep(0.03)
            segundos+=1
            if punto_choque1 ==False:
                    esperar1+=1    
            if esperar1>=16:
                esperar1=0
                punto_choque1=True
            if segundos==1000:
                segundos=100
            if segundos%32==0:
                Time1+=1
                Score+=1
                Marcadores1.config(text="Score: {} \n   Time: {} seg \n Life:{}".format(Score, Time1,Life1))
                if Life1==3 and Time1==20 or Time1==50:
                    Bono1+=20
                
            if Time1>=5:
                enemigos1_list=[]
                enemigo1_object=[]
                Life1=0
                pase_nivel1=False
                
        else:
            time.sleep(0.01)
    
    if Time1>=5:
        Level_1.unbind_all("<Key>")
    elif Life1<=0:
        transition1=False
        Level_1.unbind_all("<Key>")
        
def Screen_Level_1():
    global Level_1, zombie1,enemigos1,Villanos1,marcador_puntaje1,marcador_nombre_canv1,Marcadores1,Time1,Life1,Score,Bono1
    pygame.mixer.music.stop()
    pygame.mixer.music.load("halloween.mp3")
    pygame.mixer.music.play(100)
    background.destroy()

    #Scoreboards
    Bono1=0
    Score = 0
    Time1 = 0
    Life1 = 3
    
    # Level 1 Canvas creation
    imagen1 = ImageTk.PhotoImage(Image.open("room.png"))
    Level_1= Canvas(board, width=width, height=height)
    Level_1.pack()
    Level_1.create_image(0,0,anchor=NW, image=imagen1)

    # Level 1 Scoreboard 
    marcador_nombre_img1 = ImageTk.PhotoImage(Image.open("cartel nombre.png").resize((350,150)))
    marcador_puntaje_img1 = ImageTk.PhotoImage(Image.open("Marcadores.png").resize((300,150)))
    marcador_nombre_canv1= Level_1.create_image(200,-10,anchor=NW, image=marcador_nombre_img1)
    marcador_puntaje1= Level_1.create_image(-20,-20,anchor=NW, image=marcador_puntaje_img1)
    Marcadores1= Label(Level_1,bg="black",fg="White", text="Score: {}\n   Time: {} seg \n Life:{}".format(Score, Time1,Life1),font=("Courier",11))
    Marcadores1.place(x=50,y=45)
    Marcador_nombre1= Label(Level_1,bg="black",fg="White", text="{}".format(Player),font=("Courier",11))
    Marcador_nombre1.place(x=280,y=55)
    # Stop and exit buttons
    salir_boton1=Button(Level_1,bd=5,bg="lightGoldenrod3", text = "   ¡salir!   ", font=("Franklin Gothic Medium",10 ), command=Screen_Level_1_to_mainscreen)
    salir_boton1.place(x= 530, y= 30)
    detener_boton1=Button(Level_1,bd=5,bg="lightGoldenrod3", text = "   ¡Pausa!   ", font=("Franklin Gothic Medium",8 ), command=detener1)
    detener_boton1.place(x= 530, y= 70)
    # Player's airplane 
    zombie_img1 = ImageTk.PhotoImage(Image.open("player.png").resize((70,100)))
    zombie1= Level_1.create_image(400,450,anchor=NW, image=zombie_img1)
    
    #move user airplane 
    Level_1.bind_all("<Key>",mover1)
    
    #move enemy
    Villanos1= threading.Thread(target=mover_enemigos1)
    Villanos1.start()

    #Functions to change to the different screens 
    cambiar_a_derrota1()
    cambiara_nivel1()

    Level_1.mainloop()


"GAME CONTROLS"
#Control to move the user airplane
#<>
def mover1(event):
    global verificar_disparo1
    x1, y1= Level_1.coords(zombie1)
    if event.keysym=='Left' and pausa1:
        if x1<=10:
            x1=10
            Level_1.coords(zombie1, x1,y1)
        Level_1.coords(zombie1, x1-x,y1)
    elif event.keysym=="Right" and pausa1:
        if x1 >= 916:
            x1=916
            Level_1.coords(zombie1, x1,y1)
        Level_1.coords(zombie1, x1+x,y1)
    elif event.keysym=="Up" and pausa1:
        if y1<=10:
            y1=10
            Level_1.coords(zombie1, x1,y1)
        Level_1.coords(zombie1, x1,y1-y)
    elif event.keysym=="Down" and pausa1:
        if y1 >= height-110:
            y1=height-110
            Level_1.coords(zombie1, x1,y1)
        Level_1.coords(zombie1, x1,y1+y)

"TRANSITORY FUNCTIONS FROM MAIN SCREEN TO EVERY LEVEL"

def nombre_vacío(Nombre):
    Press_botton.play()
    global Player
    Player=Nombre
    if Nombre=="" or len(Nombre)>18:
        return ""
    elif Nombre[0]==" ":
        return nombre_vacío(Nombre[1:])   
    Screen_Level_1()

def nombre_vacío2(Nombre):
    Press_botton.play()
    global Player,pasar2
    Player=Nombre
    if Nombre=="" or len(Nombre)>18:
        return ""
    elif Nombre[0]==" ":
        return nombre_vacío2(Nombre[1:])
    pasar2=True   
    Screen_Level_2()

def nombre_vacío3(Nombre):
    Press_botton.play()
    global Player,pasar3
    Player=Nombre
    if Nombre=="" or len(Nombre)>18:
        return ""
    elif Nombre[0]==" ":
        return nombre_vacío3(Nombre[1:])
    pasar3=True   
    Screen_Level_3()
    
"MAIN SCREEN"

def main_screen():
    global background,Score
    Score=0

    # canvas creation
    imagenmenu = ImageTk.PhotoImage(Image.open("mainwindow.png"))
    background = Canvas(board,height = height, width = width)
    background.pack()
    img_fondo= background.create_image(0,0,anchor=NW, image=imagenmenu)
    #Ornaments images
    telaraña1_img= ImageTk.PhotoImage(Image.open("telaraña1.png").resize((300,300)))
    telaraña2_img= ImageTk.PhotoImage(Image.open("telaraña2.png").resize((250,250)))
    characters_name = ImageTk.PhotoImage(Image.open("Nombre max.png").resize((260,160)))
    #Ornaments
    telaraña1= background.create_image(-36,height-260,anchor=NW, image=telaraña1_img)
    telaraña2= background.create_image(width-208,-17,anchor=NW, image=telaraña2_img)
    max_name= background.create_image(350,30,anchor=NW, image=characters_name)
    # Entry
    Jugador = Entry(background,bd=8,bg="white",fg="black",width=26,font=("Franklin Gothic Medium",17 ))
    Jugador.place(x= width/2 - Jugador.winfo_reqwidth()/2/1.5, y= height/2-300,width=240, height=50)
    #Buttons images
    imageButton_easy = ImageTk.PhotoImage(Image.open("easy.png").resize((80,45)))
    imageButton_normal = ImageTk.PhotoImage(Image.open("normal.png").resize((90,52)))
    imageButton_hard = ImageTk.PhotoImage(Image.open("hard.png").resize((80,45)))
    imageButton_exit = ImageTk.PhotoImage(Image.open("exit.jpg"))
    imageButton_about = ImageTk.PhotoImage(Image.open("button2.png"))
    imageButton_scores = ImageTk.PhotoImage(Image.open("button1.png"))
    imageButton_infoImage = ImageTk.PhotoImage(Image.open("button3.png"))
    imageButton_book = ImageTk.PhotoImage(Image.open("book.jpg"))
    imageButton_register = ImageTk.PhotoImage(Image.open("button4.png"))

    #Buttons
    "Levels"
    easyButton = Button(background, image = imageButton_easy,borderwidth= 10, bg = 'black', command= lambda: nombre_vacío(Jugador.get()))
    easyButton.place(x = 275, y = 575)
    normalButton = Button(background, image = imageButton_normal,borderwidth= 10, bg = 'black', command= lambda: nombre_vacío2(Jugador.get()))
    normalButton.place(x = 450, y = 575)
    hardButton = Button(background, image = imageButton_hard,borderwidth= 10, bg = 'black', command= lambda: nombre_vacío3(Jugador.get()))
    hardButton.place(x = 625, y = 575)
    "Complementary Buttons"
    # Exit of the game
    exitButton = Button(background,bd=6,image=imageButton_exit, text = " Salir ", font=("Franklin Gothic Medium",8),padx=12,pady=2, command= quit)
    exitButton.place(x = 940, y = 10)
    # open about window button
    Boton_about = Button(background,image=imageButton_about,bd=6,bg="darkgrey",command= screen_about)
    Boton_about.place(x = 30, y = 110)
    # open scores window button
    Boton_scores = Button(background,image=imageButton_scores,bd=6,bg="darkgrey", command= insert_lista)
    Boton_scores.place(x = 30, y = 30)
    # open history window
    bookButton = Button(background, image= imageButton_book, bg = 'white', borderwidth=5,command= historyGame)
    bookButton.place(x=90, y= 540)

    Jugador.focus()
    background.mainloop()


"SCREENS IN THE MAIN SCREEN"

"History screen"

def pass_historyGame_mainscreen():
    global history_canv
    Press_botton.play()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Ghostly Mansion.mp3") 
    pygame.mixer.music.play(100)
    history_canv.destroy()
    main_screen()

def historyGame():
    Press_botton.play()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Epic Halloween MusicDark Vocal.mp3")
    pygame.mixer.music.play(100)
    global history_canv, background
    background.destroy()
    img_history = ImageTk.PhotoImage(Image.open("historywindow.png"))
    history_canv= Canvas(board,height = height, width = width)
    history_canv.pack()
    history_background= history_canv.create_image(0,0,anchor=NW, image=img_history)

    historyButton_img = ImageTk.PhotoImage(Image.open("destroy.png"))
    historyButton = Button(history_canv, image = historyButton_img,  borderwidth = 6, bg = 'black',command = pass_historyGame_mainscreen)
    historyButton.place(x=5, y=10)
    history_canv.mainloop()

    "Screen about"

def pass_about_mainscreen():
    global about
    Press_botton.play()
    about.destroy()
    main_screen()

def screen_about():
    global background,about
    Press_botton.play()
    background.destroy()
    img_about = ImageTk.PhotoImage(Image.open("aboutwindow.png")) 
    about = Canvas(board,height = height, width = width)
    about.pack()
    about_fondo= about.create_image(0,0,anchor=NW, image=img_about)
    information= Label(about,borderwidth=10,relief="sunken",bg="black",anchor=N, 
    text="About ?\n\n""Producido en Costa Rica \n\n Instituto Tecnológico de Costa Rica \n\n Área Académica de Ingeniería"
    " en Computadores \n\n Curso \n\n Taller de Introducción a la Programación"
    "\n\n Docente a cargo: Leonardo Araya Martínez \n\n Estudiantes Creadores:\n\n Ludwin José Ramos Briceño \n\n Juan Pablo Sánchez Sánchez"
    "\n\n Grupo 03 \n\n Curso I-2021",height=24,width=50,fg="white",font=("Courier",13))
    information.place(x=255,y=60)
    imageButton_comeback_about = ImageTk.PhotoImage(Image.open("destroy.png").resize((60,60)))
    comeback=Button(about,padx=18,pady=5,image=imageButton_comeback_about,bd=5,bg="darkgrey", command=pass_about_mainscreen)
    comeback.place(x=width /2-20, y=580)
    about.mainloop()

" Scores screen"

def pass_scores_to_mainscreen():
    global scores_canv
    Press_botton.play()
    scores_canv.destroy()
    main_screen()

def screen_scores():
    global background,scores_canv
    Press_botton.play()
    background.destroy()
    img_about = ImageTk.PhotoImage(Image.open("levelwindow.jpg")) 
    scores_canv = Canvas(board,height = height, width = width)
    scores_canv.pack()
    scores_fondo= scores_canv.create_image(0,0,anchor=NW, image=img_about)
    img_puntuaciones = ImageTk.PhotoImage(Image.open("text puntuaciones.png"))
    text_puntuaciones= scores_canv.create_image(90,60,anchor=NW, image=img_puntuaciones)
    imageButton_comeback_scores = ImageTk.PhotoImage(Image.open("destroy.png").resize((60,60)))
    comeback=Button(scores_canv,padx=18,pady=5,image=imageButton_comeback_scores,bd=5,bg="darkgrey", command=pass_scores_to_mainscreen)
    comeback.place(x=240, y=500)
    text_window = Text(scores_canv,width=30,height=10,bg="black",fg="white", borderwidth= 8,font = ('Helvetica', 16))
    window_text= scores_canv.create_window(80,180,anchor=NW, window=text_window)
    text_file = open("result.txt", "r+")
    txt = text_file.read()
    text_window.insert(END, txt)
    text_file.close()
    scores_canv.mainloop()

"Arrange scores"

def Update():
    global scores_var,orden_score,puntajes_let,exp1
    exp1=0
    scores_var_temp=[]
    puntajes_let=[]
    puntajes_let=quick_sort(orden_score)
    puntajes_let.reverse()
    file = open('result.txt', 'w')
    for i in puntajes_let:
        
        n=str(i)
        scores_var_temp=[]
        for score2, name in scores_var:

            if n==score2 and exp1<5:
                
                file.write(name +"\t"+ score2 + "\n")
                exp1+=1
            else:
                scores_var_temp+=[[score2,name]]
        scores_var=scores_var_temp
        scores_var.reverse()
        if scores_var_temp==[]:
            break

    file.close()
    screen_scores()

def insert_lista():
    global orden_score,scores_var
    orden_score=[]
    scores_var = []
    with open("player.txt") as f:
        for line in f:
            if not line.strip():
                continue
            else:
                name, score1 = line.split()
                scores_var.append([score1, name])
    for score2, name in scores_var:
        num=int(score2)
        orden_score+=[num]
    Update()

"Quick sort algorithm"

def quick_sort(lista):
    
    length = len(lista)
    
    if length <= 1:
        return lista
    else:
        middle=round(length/2)
        pivot = lista.pop(middle)

    items_greater = []
    items_lower = []
    
    for item in lista:
        if item > pivot:
            items_greater+=[item]

        else:
            items_lower+=[item]
    
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

pygame.mixer.music.load("Ghostly Mansion.mp3") 
pygame.mixer.music.play(100)

main_screen()
board.mainloop()
