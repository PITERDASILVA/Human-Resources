class ProcessoSeletivo:
    def __init__(self, nome, idade, sexo, pretSalarial, função):
        self.nome = nome
        self.idade = int(idade)
        self.sexo = sexo
        self.pretSalarial = float(pretSalarial)   
        self.funcao = função
        self.aprovado = False

    def aprovar(self): 
            self.aprovado = True
       
    
    def reprovar(self):
            self.aprovado = False
        
    
    def __str__(self):
        status_candidato = "Aprovado" if self.aprovado else "Reprovado"
        return (f"Nome: {self.nome} - Salário: {self.pretSalarial:.3f} - Função: {self.funcao}")
    
class Funcionario:
    def __init__(self, nome, idade, sexo, salario, funcao):
        self.nome = nome
        self.idade = int(idade)
        self.sexo = sexo
        self.salario = float(salario)
        self.funcao = funcao 
        self.admitido = False

    def admitir(self):
        if not self.admitido:
            self.admitido = True
            return True
        return False
    
    def demitir(self):
        if self.admitido:
            self.admitido = False
            return True
        return False
    
    def __str__(self):
        status_funcionario = "Admitido" if self.admitido else "Demitido"
        return (f"Status: {status_funcionario}\n"
                f"Nome: {self.nome}\n"
                f"Idade: {self.idade}\n"
                f"Sexo: {self.sexo}\n"
                f"Função: {self.funcao}\n"
                f"Salário: {self.salario:.3f}")
    
class RecursosHumanos:
    def __init__(self):
        self.funcionarios = []
        self.candidatos = []

    def adicionar_candidato(self, candidato):
        self.candidatos.append(candidato)
        
    def listar_candidatos(self, nome=None):
        if nome:
            encontrados = [candidato for candidato in self.candidatos if candidato.nome.lower() == nome.lower()]
            if not encontrados:
                print("Nenhum candidato cadastrado.")
            for i, candidato in enumerate(encontrados, 1):
                print(f'{i} - {candidato}\n')
        else:    
            if not self.candidatos:
                print("Nenhum candidato cadastrado")
            for i, candidato in enumerate(self.candidatos, 1):
                print(f'{i}. {candidato}')

    def aprovar_candidato(self, nome):
        for candidato in self.candidatos:
            if candidato.nome.lower() == nome.lower():
                candidato.aprovar()
                print(f"O candidato '{nome}' foi aprovado.")
                return True
        print(f"O candidato '{nome}' não foi encontrado.")
        return False
      

    def reprovar_candidato(self, nome):
        for candidato in self.candidatos:
            if candidato.nome.lower() == nome.lower():
                candidato.reprovar()
                print(f"O candidato '{nome}' foi reprovado.")
                return True
        print(f"O candidato '{nome}' não foi encontrado.")
        return False
     
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
    
    
    def listar_funcionarios(self, nome):
        encontrados = [funcionario for funcionario in self.funcionarios  if funcionario.nome.lower() == nome.lower()]
        if not encontrados:
            print("Nenhum funcionario cadastrado.")
        for i, funcionario in enumerate(encontrados, 1):
            print(f'{i} - {funcionario}\n')

    def demitir_funcionarios(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.nome.lower() == nome.lower():
                if funcionario.demitir():
                    print(f"O funcionario '{nome}' foi demitido.")
                    return True
                else:
                    print(f"O funcionario '{nome}' já está demitido.")
                    return False
        print(f"O funcionario '{nome}' não foi encontrado.")
        return False
    
    def admitir_funcionarios(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.nome.lower() == nome.lower():
                print(f"O funcionario '{nome}' já está admitido.")
                return False

        for candidato in self.candidatos:
            if candidato.nome.lower() == nome.lower():
                if candidato.aprovado:
                    self.listar_candidatos(nome)
                    modificacao = input("Deseja modificar o salário do funcionário? (s/n): ")
                    if modificacao.lower() == 's':
                        novo_salario = input("Digite o novo salário: ")
                        candidato.pretSalarial = float(novo_salario)


                    funcionario = Funcionario(candidato.nome, candidato.idade, candidato.sexo, candidato.pretSalarial, candidato.funcao)
                    funcionario.admitir() #Define a admição como true
                    self.adicionar_funcionario(funcionario)
                    self.candidatos.remove(candidato)
                    print(f"O funcionario '{nome}' foi admitido.")
                    return True
                else:   
                    print(f"O candidato '{nome}' precisar ser aprovado no processo seletivo.")
                    return False
        print(f"O candidato '{nome}' não foi encontrado.")
        return False

def menu_candidato():
    print("Menu")
    print("1. Processo seletivo")
    print("2. Funcionarios")

def menu_candidato1():
    print("Menu")
    print("1. Adicionar Candidato")
    print("2. Listar Candidatos")
    print("3. Aprovar Candidato")
    print("4. Reprovar Candidato")

def funcionarios_menu():
    print("Menu de funcionarios")
    print("1. Admitir funcionario") 
    print("2. Demitir funcionario")
    print("3. Detalhes funcionarios") 
    print("4. Sair")

def main():
    rh = RecursosHumanos()

    while True:
        menu_candidato()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            menu_candidato1()
            escolha_candidato = input("Escolha uma opção: ")

        
            if escolha_candidato == '1':
                print("Dados Pessoais do Candidato")
                print("---------------------------")
                nome = input("Nome:")
                idade = input("Idade:")
                sexo = input("Sexo:") 
                função = input("Função:")
                pretSalarial = input("Pretensão Salarial:")
                candidato = ProcessoSeletivo(nome, idade, sexo, pretSalarial, função)  
                rh.adicionar_candidato(candidato)
                print("Candidato adicionado com sucesso!")
        
                  

            elif escolha_candidato == '2':
                print("Lista de candidatos")
                rh.listar_candidatos()
                
            elif escolha_candidato == '3':      
                nome = input("Digite o nome do candidato: ")
                rh.aprovar_candidato(nome)
            
            elif escolha_candidato == '4':
                nome = input("Digite o nome do candidato: ")
                rh.reprovar_candidato(nome)
            
            else:
                print("Opção inválida")
     

            
        if escolha == '2':
            funcionarios_menu()
            escolha_funcionario = input("Escolha uma opção: ")

            if escolha_funcionario == '1':    
                nome = input("Digite o nome do funcionario:") 
                rh.admitir_funcionarios(nome)   
            
            elif escolha_funcionario == '2':
                nome = input("Digite o nome do funcionario: ")
                rh.demitir_funcionarios(nome)  

            elif escolha_funcionario == '3':
                nome = input("Nome do Funcionário: ")  
                rh.listar_funcionarios(nome)

            elif escolha_funcionario == '4':
                break

            else:
                print("Opção inválida")
    
if __name__ == '__main__':
    main()