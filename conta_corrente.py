from conta import Conta


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2.0
