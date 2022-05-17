from tkinter import *
import random
top = Tk()
top.config(bg = "Black")
# Code to add widgets will go here...
top.title("Rock Paper Scissor")
top.geometry("600x600")

frm1 = Frame(top,height = 20,bg = "black")
frm1.pack()

frm2 = Frame(top,height = 50,bg = "black")
frm2.pack()

frm3 = Frame(top,height = 20,bg = "black")
frm3.pack()

frm4 = Frame(top,height = 40,bg = "black")
frm4.pack()

frm5 = Frame(top,height = 20,bg = "black")
frm5.pack()

frm6 = Frame(top,height = 20,bg = "black")
frm6.pack()

frm7 = Frame(top,height = 20,bg = "black")
frm7.pack()

frm8 = Frame(top,height = 50,bg = "black")
frm8.pack()

frm9 = Frame(top,height = 20,bg = "black")
frm9.pack()

frm10 = Frame(top,height = 40,bg = "black")
frm10.pack()

frm11 = Frame(top,height = 20,bg = "black")
frm11.pack()

frm12 = Frame(top,height = 30,bg = "black")
frm12.pack()

frm13 = Frame(top,height = 20,bg = "black")
frm13.pack()

frm14 = Frame(top,height = 30,bg = "black")
frm14.pack()

frm15 = Frame(top,height = 20,bg = "black")
frm15.pack()

global src
src = 0

def r():
	pl.config(text = "ROCK",font = ("Helvetica",25),bg = "black",fg = "cyan")
	p.config(text = "ROCK  ",font = ("Helvetica",20),fg = "orange",bg = "black")
	val = int(random.randint(1,3))
	if (val == 1):
		comp.config(text = "ROCK",font = ("Helvetica",25),bg = "black",fg = "cyan")
		c.config(text = "  ROCK",font = ("Helvetica",20),fg = "orange",bg = "black")
		fin.config(text = "TIED",font = ("Helvetica",20),bg = "black",fg = "blue")
	elif (val == 2):
		comp.config(text = "PAPER",font = ("Helvetica",25),bg = "black",fg = "cyan")
		c.config(text = "  PAPER",font = ("Helvetica",20),fg = "orange",bg = "black")
		fin.config(text = "COMPUTER WON",font = ("Helvetica",20),bg = "black",fg = "red")
		global src
		src-=1
		score.config(text = src)
	else:
		comp.config(text = "SCISSOR",font = ("Helvetica",25),bg = "black",fg = "cyan")
		c.config(text = "  SCISSOR",font = ("Helvetica",20),fg = "orange",bg = "black")
		fin.config(text = "YOU WON",font = ("Helvetica",20),bg = "black",fg = "lime")
		
		src+=1
		score.config(text = src)
	rock.config(state = "disable")
	ppr.config(state = "disable")
	sci.config(state = "disable")



def pa():
	pl.config(text = "PAPER",font = ("Helvetica",25),bg = "black",fg = "cyan")
	p.config(text = "PAPER  ",font = ("Helvetica",20),fg = "orange",bg = "black")
	val = int(random.randint(1,3))
	if (val == 1):
		comp.config(text = "ROCK",font = ("Helvetica",25),bg = "black",fg = "cyan")
		c.config(text = "  ROCK",font = ("Helvetica",20),fg = "orange",bg = "black")
		fin.config(text = "YOU WON",font = ("Helvetica",20),bg = "black",fg = "lime")
		global src
		src+=1
		score.config(text = src)
	elif (val == 2):
		comp.config(text = "PAPER",font = ("Helvetica",25),bg = "black",fg = "cyan")
		c.config(text = "  PAPER",font = ("Helvetica",20),fg = "orange",bg = "black")
		fin.config(text = "TIED",font = ("Helvetica",20),bg = "black",fg = "blue")
	else:
		comp.config(text = "SCISSOR",font = ("Helvetica",25),bg = "black",fg = "cyan")
		c.config(text = "  SCISSOR",font = ("Helvetica",20),fg = "orange",bg = "black")
		fin.config(text = "COMPUTER WON",font = ("Helvetica",20),bg = "black",fg = "red")
		
		src-=1
		score.config(text = src)
	rock.config(state = "disable")
	ppr.config(state = "disable")
	sci.config(state = "disable")



def s():
	pl.config(text = "SCISSOR",font = ("Helvetica",25),bg = "black",fg = "cyan")
	p.config(text = "SCISSOR  ",font = ("Helvetica",20),fg = "orange",bg = "black")
	val = int(random.randint(1,3))
	if (val == 1):
		comp.config(text = "ROCK",font = ("Helvetica",25),bg = "black",fg = "cyan")
		c.config(text = "  ROCK",font = ("Helvetica",20),fg = "orange",bg = "black")
		fin.config(text = "COMPUTER WON",font = ("Helvetica",20),bg = "black",fg = "red")
		global src
		src-=1
		score.config(text = src)
	elif (val == 2):
		comp.config(text = "PAPER",font = ("Helvetica",25),bg = "black",fg = "cyan")
		c.config(text = "  PAPER",font = ("Helvetica",20),fg = "orange",bg = "black")
		fin.config(text = "YOU WON",font = ("Helvetica",20),bg = "black",fg = "lime")
		
		src+=1
		score.config(text = src)
	else:
		comp.config(text = "SCISSOR",font = ("Helvetica",25),bg = "black",fg = "cyan")
		c.config(text = "  SCISSOR",font = ("Helvetica",20),fg = "orange",bg = "black")
		fin.config(text = "TIED",font = ("Helvetica",20),bg = "black",fg = "blue")
	rock.config(state = "disable")
	ppr.config(state = "disable")
	sci.config(state = "disable")

def res():
	pl.config(text = "")
	p.config(text = "")
	comp.config(text = "")
	c.config(text = "")
	fin.config(text = "")
	rock["state"] = "normal"
	ppr["state"] = "normal"
	sci["state"] = "normal"

tit = Label(frm1,text = "Rock Paper Scissor",font = ("Helvetica",25,"bold","italic"),fg = "yellow",bg = "black")
tit.pack()

rock = Button(frm3,text = "ROCK",font = "Helvetica,bold,200",padx = 10,fg = "#003153",command = r)
rock.pack(side = "left")

rp = Label(frm3,bg = "black",padx = 15)
rp.pack(side = "left")

ppr = Button(frm3,text = "PAPER",font = "Helvetica,bold",padx = 10,fg = "#003153",command = pa)
ppr.pack(side = "left")

ps = Label(frm3,bg = "black",padx = 15)
ps.pack(side = "left")

sci = Button(frm3,text = "SCISSOR",font = "Helvetica,bold",padx = 10,fg = "#003153",command = s)
sci.pack(side = "left")

complbl = Label(frm5,text = "Computer : ",bg = "black",fg = "White",font = ("Helvetica",25))
complbl.pack(side = "left")

comp = Label(frm5)
comp.pack(side = "left")

plbl = Label(frm7,text = "Player : ",bg = "black",fg = "White",font = ("Helvetica",25))
plbl.pack(side = "left")

pl = Label(frm7)
pl.pack(side = "left")

c = Label(frm9)
c.pack(side = "left")

vs = Label(frm9,text = "vs",font = ("Helvetica",20),bg = "black",fg = "white")
vs.pack(side = "left")

p = Label(frm9)
p.pack(side = "left")

fin = Label(frm11)
fin.pack()

resbtn = Button(frm13,text = "Reset",font = ("Helvetica",15),fg = "lavender",bg = "teal",command = res)
resbtn.pack()

scolbl = Label(frm15,text = "Score : ",font = ("Helvetica",20),bg = "black",fg = "White")
scolbl.pack(side = "left")

score = Label(frm15,font = ("Helvetica",20),bg = "black",fg = "white")
score.pack()

top.mainloop()