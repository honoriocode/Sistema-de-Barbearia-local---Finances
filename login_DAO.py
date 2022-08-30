import mysql.connector

from login import Login

class Login_DAO():
    __login = Login()

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        self.__login = login

    def conectar(self):
        self.__cnx = mysql.connector.connect(host='127.0.0.1', database='barbearia', user='root', password='***************')
        self.__cursor = self.__cnx.cursor()

    def fecharconexao(self):
        self.__cursor.close()
        self.__cnx.close()

    def inserir(self):
        self.conectar()
        sql = 'insert into login values(0,%s,%s)'
        sqldados = (self.__login.usuario, self.__login.senha)
        self.__cursor.execute(sql, sqldados)
        self.__cnx.commit()

    def verificar_login(self):
        self.conectar()
        sql = 'SELECT * from login where usuario = %s and senha = %s'
        sqldados = (self.__login.usuario, self.__login.senha)
        self.__cursor.execute(sql, sqldados)
        respbd = self.__cursor.fetchone()
        if respbd == None:
            return False
        else:
            return True
