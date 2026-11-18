        # Atributos de controle
        self.reproducoes = 0 # int, conta as reproduções iniciadas.
        self.tocando = False # bool, indica se a música está tocando.
        self.favorito = False

        def reproduzir(self):

        # Verifica se a música NÃO está tocando.
        if self.tocando == False:
            self.tocando = True # modifica o atributo.
            self.reproducoes += 1 # incrementa o contador de reproduções.
            print(f"Reproduzindo a música: {self._nome}.")

        else:
            print(f"A música {self._nome} já está sendo reproduzida.") # Se já estiver tocando, não inicia outra reprodução.
    
    
    # Método que pausa a reprodução da música.        
    def pausar(self):
         # Verifica se a música está tocando.
        if self.tocando == True:
            self.tocando = False
            print(f"A reprodução da música {self._nome} foi pausada.")

        else:
            print("Nenhuma música está sendo reproduzida.") # Não altera o estado se a música já estiver parada.


    def favoritar(self):
        if self.favorito == False:
            self.favorito = True
            print(f"A música : {self._nome} foi adicionada aos favoritos!")
        else:
            print(f"A música : {self._nome} já está nos favoritos!")

    def defavoritar(self):
            if self.favorito == True:
                self.favorito = False
                print(f"A música : {self._nome} foi removida dos favoritos!")
            else:
                print(f"A música : {self._nome} não está nos favoritos!")


def __init__(self, nome, cantor, genero, duracao, ano): 

        #=========================================================================================#
        # Validação
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome da música deve ser um texto não vazio!")
        if not isinstance(cantor, str) or not cantor.strip():
            raise ValueError("Cantor(a) da música deve ser um texto não vazio!")
        if not isinstance(genero, str) or not genero.strip():
            raise ValueError("Gênero da música deve ser um texto não vazio!")
        if type(duracao) is not int or duracao <=0:
             raise ValueError("O atributo duração deve ser um número inteiro positivo.")
        if type(ano) is not int or ano <=0:
                     raise ValueError("O atributo ano deve ser um número inteiro positivo.")

 # Atributos de controle
        self.reproducoes = 0 # int, conta as reproduções iniciadas.
        self.tocando = False # bool, indica se a música está tocando.
        self.favorito = False