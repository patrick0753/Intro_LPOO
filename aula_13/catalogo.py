from musica import Musica
class Catalogo:
    def __init__(self):
        self.musicas =[]
        self.musica_atual = None #SEM INFORMAÇÃO ATUALMENTE
        self.reproducoes = {} #LISTA VAZIA DE REPRODUÇÕES
        self.favoritos = [] #LISTA VAZIA DE FAVORITOS

    @staticmethod # STATICMETHOD: serve para indicar que o método não depende do estado do objeto, ou seja, não utiliza self. Ele pode ser chamado diretamente na classe, sem a necessidade de criar uma instância.
    def _normalizar(texto):
            return texto.strip().lower()
        
    def verificar_duplicidade(self, musica):
        if not isinstance(musica, Musica):
            raise TypeError('É necessário informar um objeto da classe Musica')
 
        for cadastradas in self.musicas:
            if (self._normalizar(cadastradas.nome) == self._normalizar(musica.nome) and
                self._normalizar(cadastradas.cantor) == self._normalizar(musica.cantor) and
                self._normalizar(cadastradas.genero) == self._normalizar(musica.genero) and
                cadastradas.duracao == musica.duracao and cadastradas.ano == musica.ano):
                return True
        return False

    def adicionar_musica(self, musica):
        if not isinstance(musica,Musica):
            raise TypeError('É necessário informar um objeto da classe Musica')

        if self.verificar_duplicidade(musica):
            print({f'A musica {musica.nome} já existe no catálogo de músicas, cadastro não realizado'})
            return False

        
        self.musicas.append(musica)
        self.reproducoes[musica]=0 # personalizar
        # chamar um método de favorito
        print({f'A musica {musica.nome} foi adicionada ao catálogo de músicas'})

    def remover_musica(self, musica):
        if musica not in self.musicas:
            return False
        

        if self.musica_atual is musica:
            self.musica_atual = None

        # removendo de reproducoes e de lista
        self.reproducoes.pop(musica, None)  
        self.musicas.remove(musica)
        return True

    def reproduzir(self, musica):
        if musica not in self.musicas:
            print('A música não está cadastrada no catálogo.')
            return False
        
        if self.musica_atual is musica:
            print(f'A música {musica.nome} já está sendo reproduzida.')
            return False
        
        self.musica_atual = musica
        self.reproducoes[musica] += 1
        print(f'Reproduzindo a música: {musica.nome} - {musica.cantor}')
        return True

    def pausar(self):
        if self.musica_atual is None:
            print('Nenhuma música está sendo reproduzida no momento.')
            return False

        print(f'Reprodução da música {self.musica_atual.nome} pausada.')
        self.musica_atual = None
        return True
    def favoritar_musica(self, musica):
        if musica not in self.musicas or musica in self.favoritos:
            print('A música não está cadastrada no catálogo.')
            return False
        self.favoritos.append(musica)
        return True
    
    def desfavoritar_musica(self, musica):
        if musica not in self.favoritos:
            print('A música não está na lista de favoritos.')
            return False
        self.favoritos.remove(musica)
        return True
    def listar_favoritos(self):
        for musica in self.favoritos:
            print(musica)
        ##################################################################

    def listar_musicas(self):
        for musica in self.musicas:
            print(musica)

    def filtrar_por_nome(self,termo):
        termo = self._normalizar(termo)

        return [musica for musica in self.musicas 
                if termo in self._normalizar(musica.nome)]
    
    def filtrar_por_cantor(self,termo):
        termo = self._normalizar(termo)

        return [musica for musica in self.musicas 
                if termo in self._normalizar(musica.cantor)]
    
    def filtrar_por_genero(self, genero):
        genero = self._normalizar(genero)

        return [musica for musica in self.musicas 
                if genero in self._normalizar(musica.genero)]

    def filtrar_por_ano(self, ano):
        return [musica for musica in self.musicas if musica.ano == ano]

    def filtrar_por_duracao(self, min, max):
        segundos_min = min*60
        segundos_max = max*60

        return [musica for musica in self.musicas 
                if segundos_min <= musica.duracao <= segundos_max]