from tkinter import *
raiz = Tk()
raiz.title('Heladeria')
#raiz.iconbitmap("helado.ico")


# Medidas de la ventana
raiz.geometry("1280x800")

# Frame
miFrame = Frame()
miFrame.pack()
miFrame.config(width = '1280',height='800')
miFrame.config(bd = "10")
miFrame.config(relief= 'ridge')
miFrame.config(cursor="heart")

# Labels


# Bucle de ejecucion
raiz.mainloop()
