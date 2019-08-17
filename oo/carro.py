"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

    1.Motor
    2.Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

    1.Atributo de dado velocidade
    2.Método acelerar, que deverá incremetar a velocidade de uma unidade
    3.Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:

    1.Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
    2.Método girar_a_direita
    3.Método girar_a_esquerda


       N
    O     L
       S

Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
 """


class Carro:
    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao


class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1


    def frear(self):
        self.velocidade -= 2


class Direcao:
    direcao = ['Norte', ]
    def __init__(self, valor):
        self.valor = valor



    def girar_a_direita(self):
        self.valor = 'Leste'

    def girar_a_esquerda(self):
        pass







