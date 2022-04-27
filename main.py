import numpy as np

from conta import Conta
from conta_corrente import ContaCorrente
from conta_investimento import ContaInvestimento
from conta_poupanca import ContaPoupanca
from conta_salario import ContaSalario
from operator import attrgetter

idades = [15, 87, 65, 56, 32, 49, 37]

usuarios = [
    ("Hugo", 1994, 28),
    ("Henrique", 2000, 21),
    ("Rita", 1973, 49),
]

conta_do_hugo = ContaSalario(7)
conta_do_hugo.deposita(100.0)

conta_do_henrique = ContaSalario(4)
conta_do_henrique.deposita(100.0)

conta_do_juliano = ContaSalario(13)
conta_do_juliano.deposita(50.0)

contas = [conta_do_hugo, conta_do_juliano, conta_do_henrique]
#
# for conta in sorted(contas, key=attrgetter("_codigo")):
#     print(conta)

print(conta_do_hugo <= conta_do_juliano)
















