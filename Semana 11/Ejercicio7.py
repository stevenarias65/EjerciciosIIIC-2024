import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Prueba")
root.geometry("800x800")

c = tk.Canvas(root,bg="red",width=800,height=800)
c.pack()



# Iniciar el bucle principal de la aplicación
root.mainloop()