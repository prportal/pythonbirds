class Pessoa:
    eyes = 2
    hands = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    bruno = Pessoa(nome='Bruno Portal', idade=22)
    paulo = Pessoa(bruno, nome='Paulo Portal')
    ##print(Pessoa.cumprimentar(p))
    ##print(id(p))
    ##print(Pessoa.cumprimentar(p), p.nome, p.idade)

    for filho in paulo.filhos:
        bnome = filho.nome
        bidade = filho.idade
        print(filho.nome, filho.idade)
    paulo.olhos = 2
    print(paulo.__dict__)
    print(bruno.__dict__)
    print(Pessoa.__dict__)
