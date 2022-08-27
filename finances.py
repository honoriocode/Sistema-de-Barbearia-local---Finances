from datetime import datetime

class Finances():
    __idfinances: int
    __qtdeserv: int
    __valorserv: float
    __totalserv: float
    __dataserv: datetime
#
    @property
    def idfinances(self):
        return self.__finances

    @idfinances.setter
    def idfinances(self, idfinances):
        self.__finances = idfinances
#
    @property
    def qtdeserv(self):
        return self.__qtdeserv

    @qtdeserv.setter
    def qtdeserv(self, qtdeserv):
        self.__qtdeserv = qtdeserv
#
    @property
    def valorserv(self):
        return self.__valorserv

    @valorserv.setter
    def valorserv(self, valorserv):
        self.__valorserv = valorserv
#
    @property
    def totalserv(self):
        return self.__totalserv

    @totalserv.setter
    def totalserv(self, totalserv):
        self.__totalserv = totalserv
#
    @property
    def dataserv(self):
        return self.__dataserv

    @dataserv.setter
    def dataserv(self, dataserv):
        self.__dataserv = dataserv
