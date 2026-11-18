from musica import Musica
class Catalogo:
    def __init__(self):
        self.musicas =[]
        self.musica_atual = None #SEM INFORMAÇÃO ATUALMENTE
        self.reproducoes = {} #LISTA VAZIA DE REPRODUÇÕES
        self.favoritos = [] #LISTA VAZIA DE FAVORITOS

    def adicionar_musica(self, musica):
        #validação
        if not isinstance(musica,Musica):
            raise TypeError('É necessário informar um objeto da classe Musica')
        self.musicas.append(musica)
        self.reproducoes[musica]=0 # personalizar
        # chamar um método de favorito
        print({f'A musica {musica.nome} foi adicionada ao catálogo de músicas'})