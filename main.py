import tkinter as tk
from tela_barbearia_cadastrar import Tela_barbearia_cadastrar
window = tk.Tk()
window.title('Sistema Barbearia')
window.withdraw()
telacad = Tela_barbearia_cadastrar(window)
window.mainloop()
