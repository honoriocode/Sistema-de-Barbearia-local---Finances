import mysql.connector

from finances import Finances

class Finances_DAO():
    __finances = Finances()

    @property
    def finances(self):
        return self.__finances

    @finances.setter
    def finances(self, finances):
        self.__finances = finances

    def conectar(self):
        self.__cnx = mysql.connector.connect(host='127.0.0.1', database='barbearia', user='root', password='**********')
        self.__cursor = self.__cnx.cursor()

    def fecharconexao(self):
        self.__cursor.close()
        self.__cnx.close()

    def inserir(self):
        self.conectar()
        sql = 'insert into finances values(0,%s,%s,%s,now())'
        sqldados = (self.__finances.qtdeserv, self.__finances.valorserv, self.__finances.totalserv)
        self.__cursor.execute(sql, sqldados)
        self.__cnx.commit()
