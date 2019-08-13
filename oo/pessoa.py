class Pessoa:
    def __init__(self, *filhos, nome=None, idade=50):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    maria = Pessoa
    maria.nome = 'Mariazinha'
    print(maria.nome)
    lucas = Pessoa(nome='Lucas')
    marcos = Pessoa(nome='Marcos')
    joao = Pessoa(lucas, marcos, nome='João Batista')

    print(Pessoa.cumprimentar(joao))
    print(id(lucas))
    print(joao.cumprimentar(),'\n')

    print(joao.nome)
    print(joao.idade)
    joao.sobrenome = 'Braga'
    print('Sobrenome do João:', joao.sobrenome)
    for filho in joao.filhos:
        print(filho.nome)

    del joao.filhos
    print(joao.__dict__)
    print(lucas.__dict__)