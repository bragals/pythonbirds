class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=50):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'


    @staticmethod
    def metodo_estatico():
        return 42


    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    lucas.olhos = 1
    del lucas.olhos
    print(joao.__dict__)
    print(lucas.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(lucas.olhos)
    print(joao.olhos)
    print(id(Pessoa.olhos), id(lucas.olhos), id(joao.olhos))
    print(Pessoa.metodo_estatico(), lucas.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), lucas.nome_e_atributos_de_classe())

