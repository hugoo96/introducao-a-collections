from functools import total_ordering


@total_ordering
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0.0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

    def deposita(self, valor):
        self._saldo += valor

    @staticmethod
    def extrai_codigo(conta):
        return conta._codigo

    def __str__(self):
        return ">>Código {} Saldo {}<<".format(self._codigo, self._saldo)