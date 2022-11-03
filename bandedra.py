from tkinter import * 
ventana_principal=Tk()
ventana_principal.title("Sistemas UIS")
ventana_principal.geometry("800x500")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="black")

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="red", width=800 , height=800)
frame_entrada.place(x=0 ,y=0)
frame_resultado=Frame(ventana_principal)
frame_resultado.config(bg="white", width=150, height=500)
frame_resultado.place(x=227 ,y=0)

frame_resultado=Frame(ventana_principal)
frame_resultado.config(bg="white", width=800 , height=150)
frame_resultado.place(x=0 ,y=150)

frame_operaciones=Frame(ventana_principal)
frame_operaciones.config(bg="blue", width=95 , height=800)
frame_operaciones.place(x=255 ,y=0)

frame_operaciones2=Frame(ventana_principal)
frame_operaciones2.config(bg="blue", width=800 , height=75)
frame_operaciones2.place(x=0 ,y=190)


ventana_principal.mainloop()
