class Conta ():
    def __init__(self,numero,cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    def saldo (self):
        return self._saldo
    def numero (self):
        return self._numero
    def agencia(self):
        return self._agencia
    def cliente (self):
        return self._cliente
    def historico(self):
        return self._historico

    def nova_conta(self,Cliente,numero):
        return Conta(numero,Cliente)
    def sacar(self , valor):
        if valor > saldo :
            print("Saldo insuficiente")
        elif valor > 0 :
            self.saldo -= valor 
            print("Saque realizado")
            return True
        else:
            print("Valor incorreto")
        return False
    def depositar(self,valor):
        if valor > 0 :
            self._saldo += valor
            return True
        print("Valor invalido")
        return False
class ContaCorrente(Conta):
    def __init__(self,limite=500,limite_de_saques=3):
        super().__init__(numero,cliente)
        self.limite = limite
        self.limite_de_saques = limite_de_saques
        def sacar(self,valor):
            numero_saques = len([
                transacao for transacao in self._historico.transacoes if transacao["tipo"] == "Saque"])
            if valor > self.limite :
                print("Valor maior que o limite")
            elif numero_saques > self.limite_de_saques :
                print("Limite de saques alcancados")
            else:
                return super().sacar(valor)
class Cliente ():
    def __init__(self,endereco):
        self.endereco = endereco
        self.contas = []
    def realizar_transacao (self,conta,transacao):
        transacao.registrar(conta)
    def adicionar_conta(self,conta):
        self.contas.append(conta) 
class PessoaFisica(Cliente):
    def __init__(self,nome,data_nascimento,cpf,endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
class Historico :
    def __init__ (self):
        self._transacoes = []
    def transacoes(self):
        return self._transacoes
    def adicionar_transacao(self,transacao):
        self._transacoes.append(
            {
                "tipo":transacao.__class__.__name__,
                "valor":transacao.valor
                
            })
class Transacao():
    def valor (self):
        pass
    def registrar (self,conta):
        pass
class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor
    def valor (self):
        return self._valor
    def registrar (self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao :
            conta.historico.adicionar_transacao(self)
class Deposito(Transacao):
    def __init__ (self,valor):
        self._valor = valor
    
    def valor (self):
        return self._valor
    def registrar(self,conta):
        sucesso_transacao = conta.depositar(self.valor)
        if(sucesso_transacao):
            conta.historico.adicionar_transacao(self)




