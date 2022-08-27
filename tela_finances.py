import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
from finances_DAO import Finances_DAO

class Tela_Finances():
    def __init__(self, janela):
        self.__finDAO = Finances_DAO()
        janela = tk.Toplevel()
        janela.title('Tela Principal')
        #Título
        self.__frame1 = ttk.Frame(janela, relief=tk.RAISED, borderwidth=2)
        self.__frame1.pack(padx=5,pady=5)

        ttk.Label(self.__frame1, text = "Barber Shop - Finanças", font = ('Calibri',18)).pack()

        self.__frame2 = ttk.Frame(janela, relief=tk.RAISED, borderwidth=2)
        self.__frame2.pack(padx=5, pady=5)

        ttk.Label(self.__frame2, text='Digite a quantidade de serviços: ').grid(row=0,column=0,sticky=tk.W)
        self.__en_qtdeserv = tk.Entry(self.__frame2)
        self.__en_qtdeserv.grid(row=0,column=1,sticky=tk.W, padx=5, pady=5)

        ttk.Label(self.__frame2, text='Valor dos serviços: ').grid(row=1, column=0, sticky=tk.W)
        self.__en_valorserv = tk.Entry(self.__frame2)
        self.__en_valorserv.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        #Button Calcular
        self.__bt_calcular = tk.Button(self.__frame2, text='Calcular Serviços', command=self.calculartotal)
        self.__bt_calcular.grid(row=2, columnspan=2, sticky=tk.S, padx=5, pady=5)

        ttk.Label(self.__frame2, text='Valor total de serviços realizados: ').grid(row=3, column=0, sticky=tk.W)
        self.__total = tk.StringVar()
        self.__en_totalserv = tk.Entry(self.__frame2, state=tk.DISABLED, textvariable=self.__total)
        self.__en_totalserv.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

        self.__bt_savefinances = tk.Button(self.__frame2, text='Salvar Finanças', command=self.inserir)
        self.__bt_savefinances.grid(row=4, columnspan=2, sticky=tk.S, padx=5, pady=5)

    def calculartotal(self):
        qtdeserv = float(self.__en_qtdeserv.get())
        valorserv = float(self.__en_valorserv.get())
        totalserv = qtdeserv * valorserv
        self.__total.set(str(totalserv))

    def inserir(self):
        try:
            self.__finDAO.finances.qtdeserv = self.__en_qtdeserv.get()
            self.__finDAO.finances.valorserv = self.__en_valorserv.get()
            self.__finDAO.finances.totalserv = self.__en_totalserv.get()
            self.__finDAO.inserir()
            messagebox.showerror('Barbearia', 'Finanças Cadastradas com Sucesso')

        except:
            messagebox.showerror('Erro', 'Por favor verifique as informações')
