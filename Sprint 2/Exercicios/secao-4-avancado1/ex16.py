'''
Crie uma classe chamada Pessoa, com um atributo privado chamado nome (declarado internamente na classe como __nome)
e um atributo público de nome id.

Adicione dois métodos à classe, sendo um para definir o valor de __nome e 
outro para retornar o valor do respectivo atributo.

Lembre-se que o acesso ao atributo privado deve ocorrer somente através dos métodos definidos, nunca diretamente.  
Você pode alcançar este comportamento através do recurso de properties do Python.

Veja um exemplo de como seu atributo privado pode ser lido e escrito:
pessoa = Pessoa(0) 
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)
'''

# Resolução:

# Usamos __init__ e self quando queremos inicializar atributos específicos para cada instância do objeto.
class Pessoa:
    def __init__(self, id_):
        """inicializa a Pessoa com um ID público e um nome privado."""
        self.id = id_
        self.__nome = None

    @property
    def nome(self):
        """retorna o nome da pessoa."""
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        """define um novo nome para a pessoa."""
        self.__nome = novo_nome

# Teste da classe
pessoa = Pessoa(0)
pessoa.nome = 'Vinicius'
print(pessoa.nome)  # Saída esperada: Vinicius

