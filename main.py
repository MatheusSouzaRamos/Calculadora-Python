from tkinter import *
from tkinter import ttk

caracteres = ''

def limpar():
	global caracteres
	caracteres = ""
	texto.set(caracteres)

def digitar(c):
	global caracteres
	caracteres = caracteres + str(c)
	texto.set(caracteres)
	
def pot():
	calcular()
	n = pow(float(caracteres),2)
	n = str(n)
	limpar()
	digitar(n)
	texto.set(n)

def zeros(st):
	if st[0] == '0' and len(st) > 1:
		st = st[1:]
		#st = str(st)
		return st
	else:
		return st
	

def calcular():
	
	global caracteres
	caracteres = zeros(caracteres)
	

	resultado = eval(caracteres)
	limpar()
	digitar(resultado)
	texto.set(resultado)
	
	print(resultado)

#cores

coulor1 = "#000000" #preto
coulor2 = "#e6570f" #laranja
coulor3 = "#404040" #cinza
coulor4 = "#28c84b" #verde
coulor5 = "#d1e123" #amarelo
coulor6 = "#3777e6" #azul
coulor7 = "#ffffff"

#telas

window = Tk()
#window.iconbitmap("icone.ico")
window.title("Calculadora - Python")
window.config(bg=coulor1)
window.geometry("269x300")
window.resizable(width=False, height=False)

visor = Frame(window, width=269, height=60, bg = coulor3)
visor.grid(row=0,column=0)

body = Frame(window, width=269, height = 240, bg = coulor1)
body.grid(row = 1, column = 0)

#botoes

"""
C	%	/	*
7	8	9	+
4	5	6	-
1	2	3	=
	0	²	
"""

bclear = Button(body, text="C", width=5,height=2, bg = coulor5, command = lambda: limpar())
bmodulo = Button(body, text="%", width=5, height=2, bg = coulor6, command = lambda: digitar('%'))
bdivide = Button(body, text="/", width = 5, height = 2, bg = coulor6, command = lambda: digitar('/'))

bmult = Button(body, text="*", width = 5, height = 2, bg = coulor6, command = lambda: digitar('*'))
bmais = Button(body, text="+", width = 5, height = 2, bg = coulor6, command = lambda: digitar('+'))
bmenos = Button(body, text="-", width = 5, height = 2, bg = coulor6, command = lambda: digitar('-'))

bigual = Button(body, text="=", width = 5, height = 5, bg = coulor4, command = lambda: calcular())

b1 = Button(body, text="1", width = 5, height = 2, bg = coulor2, command = lambda: digitar('1'))
b2 = Button(body, text="2", width = 5, height = 2, bg = coulor2, command = lambda: digitar('2'))
b3 = Button(body, text="3", width = 5, height = 2, bg = coulor2, command = lambda: digitar('3'))

b4 = Button(body, text="4", width = 5, height = 2, bg = coulor2, command = lambda: digitar('4'))
b5 = Button(body, text="5", width = 5, height = 2, bg = coulor2, command = lambda: digitar('5'))
b6 = Button(body, text="6", width = 5, height = 2, bg = coulor2, command = lambda: digitar('6'))

b7 = Button(body, text="7", width = 5, height = 2, bg = coulor2, command = lambda: digitar('7'))
b8 = Button(body, text="8", width = 5, height = 2, bg = coulor2, command = lambda: digitar('8'))
b9 = Button(body, text="9", width = 5, height = 2, bg = coulor2, command = lambda: digitar('9'))

b0 = Button(body, text = "0", width = 5, height = 2, bg = coulor2, command = lambda: digitar('0'))

bdot = Button(body, text = ",", width = 5, height = 2, bg = coulor5, command = lambda: digitar('.'))
bpow = Button(body, text = "²", width = 5, height = 2, bg = coulor6, command = lambda: pot())

bclear.place(x = 0,y = 0)
bmodulo.place(x = 67, y= 0)
bdivide.place(x = 134, y = 0)
bmult.place(x = 201, y = 0)

b7.place(x = 0, y = 48)
b8.place(x = 67, y = 48)
b9.place(x = 134, y = 48)
bmais.place(x = 201, y = 48)

b4.place(x = 0, y = 96)
b5.place(x = 67, y = 96)
b6.place(x = 134, y = 96)
bmenos.place(x = 201, y = 96)

b1.place(x = 0, y = 144)
b2.place(x = 67, y = 144)
b3.place(x = 134, y = 144)
bigual.place(x = 201, y = 142 )

b0.place(x = 0, y = 192)
bdot.place(x = 67, y = 192)
bpow.place(x = 134, y = 192)

#resultado

texto = StringVar()

mostrar = Label(visor, textvariable = texto, width = 20, height = 2, fg = coulor7, padx = 5, justify = RIGHT, anchor = "e", font='Arial 18', bg = coulor3)
mostrar.place(x = 0, y = 0)

window.mainloop()
