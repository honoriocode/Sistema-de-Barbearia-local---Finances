class Login():
    __idlogin:int
    __usuario:str
    __senha:str

    @property
    def idlogin(self):
        return self.__idlogin

    @idlogin.setter
    def idlogin(self, idlogin):
        self.__idlogin = idlogin

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha