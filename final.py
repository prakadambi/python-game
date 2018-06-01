from tkinter import *
from PIL import ImageTk,Image
from random import choice,randint
from tkinter import messagebox
import winsound
import sys
#import ttk

globcount=2.0
move=0
score=1000
                                        #generates a number randomly
def gen_num(level):
            global globcount
            globcount=2.0
            list=[0,1,2,3,4,5,6,7,8,9]
            n1=(randint(1,9))
            list.remove(n1)
            num=str(n1)
            for i in range(0,level-1):
                
                i=(choice(list))
                list.remove(i)
                num+=str(i)
            
            return num
                                        #functions for start win and cheatcode music
def stmusic_play():
    winsound.PlaySound('startmusic.wav', winsound.SND_ASYNC|winsound.SND_LOOP)
def wmusic_play():
    winsound.PlaySound('windmusic.wav', winsound.SND_ASYNC|winsound.SND_LOOP)
def smusic_play():
    winsound.PlaySound('serenity.wav', winsound.SND_ASYNC|winsound.SND_LOOP)
    

def callbackgo(level,top,frame1,frame2,frame3,frame4,namevar,num,tkimage):
    global globcount,move,score
    
    
    if(move<21):
        move+=1
        try:
            
            n=namevar.get()
            n=str(n)
            if(int(n)!=999 and int(n)!=666):
                for i in n:
                    if(n.count(i)>1):
                        
                        raise IOError
                        
                if(len(n)!=level):
                    
                    raise IOError
                    
                if(n[0]==0):
                    
                    raise IOError
                    
        except IOError:
            messagebox.showerror('Alert!','Invalid input! Please try again!')
            namevar.set(0)
        except ValueError:
            messagebox.showerror('Alert!','Invalid input! Please try again!')
            namevar.set(0)
            
        else:
            globcount+=.5
            namevar.set(0)
            if int(n)==999:
                winsound.PlaySound(None,winsound.SND_ASYNC)
                wmusic_play()
                frame5=Frame(top)
                frame5.grid(column=0,row=0)
                pl= Image.open('origami.jpg')
                pl1= pl.resize((600,600), Image.ANTIALIAS)
                im=ImageTk.PhotoImage(pl1)
                Label(frame5,image=im,text=('The correct\n ans is\n'+num),font=("Purisa",25,'bold'),compound=CENTER).pack()
                frame3.grid_forget()
                frame4.grid_forget()

            if int(n)==666:
                winsound.PlaySound(None,winsound.SND_ASYNC)
                smusic_play()
                frame5=Frame(top)
                frame5.grid(column=0,row=0)
                pl= Image.open('image3.jpg')
                pl1= pl.resize((600,600), Image.ANTIALIAS)
                im=ImageTk.PhotoImage(pl1)
                Label(frame5,image=im,text=('You found our secret--\nWe are the coders\n behind mastermind!\nInvincible and all-powerful!\n Now shoo! Go away!'),font=("Purisa",25,'bold'),compound=CENTER).pack()
                frame3.grid_forget()
                frame4.grid_forget()

                
                
            elif num!=n:
                
                p=0
                c=0   
                for i in range(0,level):
                    if n[i]==num[i]:
                        p=p+1
                      
                for j in n:
                    if j in num:
                        c=c+1
                Label(frame3,font=("Purisa",10,'bold'),fg="blue",background="white",text=("\t"+n+"\t\t"+str(c)+"\t\t"+str(p)+"\t")).place(anchor=N,relx=0.5,rely=0.10*globcount)
            
            
            if int(n)==int(num):
                winsound.PlaySound(None,winsound.SND_ASYNC)
                wmusic_play()
                frame5=Frame(top)
                frame5.grid(column=0,row=0)
                pl= Image.open('star.jpg')
                pl1= pl.resize((600,600), Image.ANTIALIAS)
                im=ImageTk.PhotoImage(pl1)
                score/=move
                
                Label(frame5,image=im,fg="white",text=('CONGRATULATIONS!!\n YOU ARE THE ULTIMATE MASTER \nOF ALL MINDS!!!\n Number of moves:'+str(move)+'\nYour score is:'+str(score)),font=("Purisa",25,'bold'),compound=CENTER).pack()
                b13=Button(frame5,font=("Purisa",10,'bold'),background="white", text='MENU', command=lambda:callback(frame1,top))
                b13.place(relx=.83, rely=0.93, anchor=CENTER)
                if(move<=7):
                    
                    tkMessageBox.showinfo('Game Over!','Outstanding job! You guessed it within 7 moves!')
                    
                elif(move<=12):
                    tkMessageBox.showinfo('Game Over!','Great job! You guessed it within 12 moves!')
                    
                elif(move<=20):
                    tkMessageBox.showinfo('Game Over!','Good job! You guessed it within 20 moves!')
                    
                frame3.grid_forget()
                frame4.grid_forget()
            
    else:
        tkMessageBox.showinfo('OOOPS!!','Sorry! restart the game and try again!')

    
    top.mainloop()
                                                        #the function that creates the play window    
def b4play(level,top,frame1,frame2,frame3,tkimage):
    num=gen_num(level)
    
    frame4=Frame(top)
    frame4.grid(column=0,row=0,sticky=N)
    Label(frame4,font=("Purisa",18,'bold'),fg="dark violet",background="white",text="GUESS THE NUMBER!").grid(row=0)
    namevar = IntVar()
    name = Entry(frame4, width=30, textvariable=namevar).grid(row=1)
    b8=Button(frame4, font=("Purisa",10,'bold'),background="white",text='Done', fg="dark violet",command=lambda:callbackgo(level,top,frame1,frame2,frame3,frame4,namevar,num,tkimage))
    b8.grid(row=2)
    Label(frame3,font=("Purisa",10,'bold'),background="white",fg="blue",text="YOUR ENTRY\tNUMBER\t\tPOSITION").place(anchor=N,relx=0.5,rely=.17)
    b10=Button(frame3, font=("Purisa",10,'bold'),background="white",text='RESTART', command=lambda:callback1(top,frame1,frame2))
    b10.place(relx=.50, rely=0.95, anchor=CENTER)
    b11=Button(frame3, font=("Purisa",10,'bold'),background="white",text='MENU', command=lambda:callback(frame1,top))
    b11.place(relx=.65, rely=0.95, anchor=CENTER)
                                                        #the function which displays demo onclick    
def callback7(top,frame2,frame1):
    
    frame7 = Frame(top)
    frame7.grid(column=0,row=0)
    men = Image.open('demo.jpg')
    men1= men.resize((600,600), Image.ANTIALIAS)
    tkima= ImageTk.PhotoImage(men1)
    Label(frame7,image=tkima).pack()
    b12=Button(frame7,font=("Purisa",10,'bold'),background="white", text='MENU', command=lambda:callback(frame1,top))
    b12.place(relx=.83, rely=0.93, anchor=CENTER)
    top.mainloop()
musicv=1
                                                        #function for music on/off
def callback10(top):
    global musicv
    musicv+=1
    if(musicv%2==0):
        winsound.PlaySound(None,winsound.SND_ASYNC)
    else:
         winsound.PlaySound('music1.wav', winsound.SND_ASYNC|winsound.SND_LOOP)  
                                                      #function for exit
def callback5(top):
    top.destroy()
    top.mainloop()
    winsound.PlaySound(None,winsound.SND_ASYNC)
                                                      #function called on click of levels 1 and 2 respectively
def callback3(b6,b7,l,top,frame1,frame2,frame3,tkimage):
    b6.destroy()
    b7.destroy()
    b4play(l,top,frame1,frame2,frame3,tkimage)
    top.mainloop()
def callback4(b6,b7,l,top,frame1,frame2,frame3,tkimage):
    b6.destroy()
    b7.destroy()
    b4play(l,top,frame1,frame2,frame3,tkimage)
    top.mainloop()
                                                        #function that creates the level buttons on click of play
def callback1(top,frame1,frame2):
    global move,score
    move=0
    score=1000
    top.title("PLAY!")
    frame3 = Frame(top)
    frame3.grid(column=0,row=0)
    play = Image.open('playy.jpg')
    play1= play.resize((600,600), Image.ANTIALIAS)
    tkimage= ImageTk.PhotoImage(play1)
    Label(frame3,image = tkimage).pack()
    frame2.grid_forget() 
    b6=Button(frame3, background="plum",text='LEVEL 1',font=("Purisa",30,'bold'), command=lambda:callback3(b6,b7,3,top,frame1,frame2,frame3,tkimage))
    b6.place(relx=0.5, rely=0.30, anchor=CENTER)
    b7=Button(frame3, background="pale turquoise",text='LEVEL 2',font=("Purisa",30,'bold'), command=lambda:callback4(b6,b7,4,top,frame1,frame2,frame3,tkimage))
    b7.place(relx=0.5, rely=0.50, anchor=CENTER)
    top.mainloop()
                                                        #function that displays rules,on click of rules
def callback2(top,frame1):
    frame6 = Frame(top)
    frame6.grid(column=0,row=0)
    menu = Image.open('play.jpg')
    menu1= menu.resize((600,600), Image.ANTIALIAS)
    tkimag= ImageTk.PhotoImage(menu1)
    Label(frame6,image=tkimag,text='\t\tMASTERMIND\n\n       Mastermind is a code breaking number game in which\n the player uses his own logic to guess a number within 20 chances.\n\n*The player can choose either of these levels:\n\nLEVEL1: Guess a three-digit number.\nLEVEL2: Guess a four -digit number.\n\n*The player can guess the number \nwith the help of the clues given after every  guess.\n*After every move  NUMBER  and POSITION\nclues appear on the screen.\n\nNUMBER: It indicates the total number \nof the digits you got right!!\n\nPOSITION: It indicates the total number of digits\n in the right position!!\n\n*The player has to keep in mind that the number \nhas to be unique with no repetition of digits\nand should not begin with a zero.\n\n*However,a zero can be included elsewhere in the number.\nFinally, the objective of the game is to guess the number\nwith all its digits in the correct position!!!\nALL THE BEST!!!\nHAPPY GUESSING!!!!',justify=LEFT,font=("Purisa",14,'bold'),compound=CENTER).pack()
    b11=Button(frame6, font=("Purisa",10,'bold'),background="white",text='MENU', command=lambda:callback(frame1,top))
    b11.place(relx=.68, rely=0.93, anchor=CENTER)
    top.mainloop()
                                                        #the menu function,on click of start
def callback(frame1,top):
    winsound.PlaySound(None,winsound.SND_ASYNC)
    music_play()
    frame2 = Frame(top)
    frame2.grid(column=0,row=0)
    menu = Image.open('menu.png')
    menu1= menu.resize((600,600), Image.ANTIALIAS)
    tkimage= ImageTk.PhotoImage(menu1)
    Label(frame2,image = tkimage).pack()
    frame1.grid_forget()    
    b1=Button(frame2,background="white", text='PLAY',font=("Purisa",20,'bold'),fg="orange", command=lambda:callback1(top,frame1,frame2))
    b1.place(relx=0.45, rely=0.26, anchor=CENTER)
    b2=Button(frame2,background="white", text='RULES',font=("Purisa",20,'bold'), fg="gold",command=lambda:callback2(top,frame1))
    b2.place(relx=0.45,rely=0.42, anchor=CENTER)
    b3=Button(frame2,background="white", text='MUSIC ON/OFF',font=("Purisa",20,'bold'), fg="green", command=lambda:callback10(top))
    b3.place(relx=0.45,rely=0.58, anchor=CENTER)
    b4=Button(frame2,background="white", text='DEMO',font=("Purisa",20,'bold'), fg="blue", command=lambda:callback7(top,frame2,frame1))
    b4.place(relx=0.45, rely=0.73, anchor=CENTER)
    b5=Button(frame2,background="white", text='EXIT', font=("Purisa",20,'bold'), fg="purple",command=lambda:callback5(top))
    b5.place(relx=0.45, rely=0.90, anchor=CENTER)
    top.mainloop()
                                                        #the play music
def music_play():
    winsound.PlaySound('music1.wav', winsound.SND_ASYNC|winsound.SND_LOOP)
                                                        #the main loop which links everything    
def game_begin():
    stmusic_play()
    top = Tk()
    top.title("MASTERMIND!!!")
    
    frame1 = Frame(top)
    frame1.grid(column=0, row=0)
    im = Image.open('cover.jpg')
    im2 = im.resize((600,600), Image.ANTIALIAS)
    tkimage = ImageTk.PhotoImage(im2)
    Label(frame1,image = tkimage).pack()
    b1=Button(frame1,background="white",text='START',font=("Purisa",20,'italic'), command=lambda:callback(frame1,top))
    b1.pack(side=LEFT)
    b1.place(relx=0.46, rely=0.93, anchor=CENTER)
    
    top.mainloop()

game_begin()
