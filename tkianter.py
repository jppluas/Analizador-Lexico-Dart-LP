import tkinter as tk

root = tk.Tk()
root.title("Frames Anidados")

# Frame principal
frame_principal = tk.Frame(root, bg="lightblue", width=400, height=300)
frame_principal.pack(fill=tk.BOTH, expand=True)

# Subframe 1 (izquierda)
subframe1 = tk.Frame(frame_principal, bg="lightgreen", width=300, height=300)
subframe1.pack(side=tk.LEFT, fill=tk.Y)

# Subframe 2 (derecha)
subframe2 = tk.Frame(frame_principal, bg="lightcoral", width=300, height=300)
subframe2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

subframe3= tk.Frame(subframe2, bg="red" , width=50, height=50)
subframe3.pack(side=tk.BOTTOM, fill=tk.BOTH)
root.mainloop()