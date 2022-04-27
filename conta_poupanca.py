from conta import Conta


class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3.0
