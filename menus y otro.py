from tkinter import*
#from tkinter import ttk

raiz=Tk()
raiz.title("Longitud maxima de un condcutor para una Caida de Tension")
raiz.resizable(1,1)

miframe = Frame(raiz)
miframe.pack()
miframe.config(bg="silver")
miframe.config(width=480,height=320)
miframe.config(relief="sunken")
miframe.config(border=5)
miframe.grid(row=0, column=0)

#menu plegable

def entradas():
    if opciones_menu_reactancia[0]:
        variable_menu_reactancia.set(4)
    return entradas


def menu_plegable(numero1,numero2):
      
    numero1=variable_menu_resistencia.get()
    
    numero2=variable_menu_reactancia.get()
    if opciones_menu_reactancia[0]=="1" and opciones_menu_resistencia[0]=="1":
        numero2=5
        numero1=1






variable_menu_resistencia=StringVar()
variable_menu_resistencia.set("")
opciones_menu_resistencia=["1"]


menu_resistencia=OptionMenu(miframe,variable_menu_resistencia,*opciones_menu_resistencia,command=menu_plegable)
menu_resistencia.grid(row=0, column=3, padx=50, pady=5, columnspan=1 )

variable_menu_reactancia=StringVar()
variable_menu_reactancia.set("")
opciones_menu_reactancia=["1"]
menu_reactancia=OptionMenu(miframe,variable_menu_reactancia,*opciones_menu_reactancia,command=menu_plegable)
menu_reactancia.grid(row=1, column=3, padx=50, pady=5, columnspan=1 )
        
#-----------------------------------------------------------------------------------------------------------------#
# label 
Label(miframe, text="Resistencia del conductor (Ω/km)", font=("arial",10, "bold"), bg="silver").grid(row=0, column=1, padx=10, pady=10, columnspan=2)
Label(miframe, text="Reactancia del conductor (Ω/km)", font=("arial",10, "bold"), bg="silver").grid(row=1, column=1, padx=10, pady=10, columnspan=2)
resistencia_conductor=Entry(miframe,justify=RIGHT, textvariable=variable_menu_resistencia)
resistencia_conductor.grid(row=0, column=5, padx=5, pady=5, columnspan=1)
resistencia_conductor.bind("<return>", entradas)
reactancia_conductor=Entry(miframe,justify=RIGHT, textvariable=variable_menu_reactancia)
reactancia_conductor.grid(row=1, column=5, padx=5, pady=5, columnspan=1)

raiz.mainloop()