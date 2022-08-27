import tkinter
from tkinter import messagebox

from login_DAO import Login_DAO
from tkinter import *

from tela_barbearia_login import Tela_barbearia_login

class Tela_barbearia_cadastrar():
    def __init__(self, window):
        self.__loginDAO = Login_DAO()
        self.__anterior = window
        self.__master = tkinter.Toplevel()
        self.__master.wm_protocol("WM_DELETE_WINDOW", self.fecharJanela)
        self.__master.title('Sistema de Log In e Contabilidade - Barber Shop')
        self.__master.geometry('600x600+610+153')
        self.__master.resizable(width=1, height=1)

        #variaveis globais

        self.__esconda_senha = StringVar()

        #importar imagens

        self.__img_fundo = PhotoImage(file="fundo_sistema_barber.png")
        self.__img_botao = PhotoImage(file="Cadastrar.png")
        self.__img_botaolog = PhotoImage(file="icones/Login.png")

        #Criar Labels

        self.__lab_fundo = Label(self.__master, image=self.__img_fundo)
        self.__lab_fundo.pack()

        #Criação de Caixas de Entrada

        self.__en_user = Entry(self.__master, bd=2, font=('Calibri', 15), justify=CENTER)
        self.__en_user.place(width=470, height=40, x=62, y=150)

        self.__en_senha = Entry(self.__master, textvariable=self.__esconda_senha, show='*', bd=2, font=('Calibri', 15), justify=CENTER)
        self.__en_senha.place(width=470, height=40, x=62, y=256)

        #criação de botões

        self.__bt_cadastrar = Button(self.__master, bd=0, image=self.__img_botao,command=self.cadastrar)
        self.__bt_cadastrar.place(width=118, height=64, x=240, y=400)
        self.__bt_login = Button(self.__master, bd=0, image=self.__img_botaolog, command=self.logar)
        self.__bt_login.place(width=118, height=64, x=240, y=500)


    def cadastrar(self):
        self.__loginDAO.login.usuario = self.__en_user.get()
        self.__loginDAO.login.senha = self.__en_senha.get()
        self.__loginDAO.inserir()
        messagebox.showinfo('Barbearia', 'Cadastro Realizado com sucesso')
        self.__en_user.delete(0,END)
        self.__en_senha.delete(0,END)

    def logar(self):
        self.__master.withdraw()
        self.__telalogin = Tela_barbearia_login()

    def fecharJanela(self):
        self.__anterior.destroy()


