from abc import abstractmethod
from typing import List
from abc import ABCMeta, abstractmethod


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0.0

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

    def deposita(self, valor):
        self._saldo += valor

    @staticmethod
    def deposita_para_todas(contas: List):
        for conta in contas:
            conta.deposita(100)

    @abstractmethod
    def passa_o_mes(self):
        pass





