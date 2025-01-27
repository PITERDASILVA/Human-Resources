class ProcessoSeletivo:
    def __init__(self, nome, idade, sexo, pretSalarial, função):
        self.nome = nome
        self.idade = int(idade)
        self.sexo = sexo
        self.pretSalarial = int(pretSalarial)   
        self.função = função
        self.aprovado = ""

    def aprovado(self): 
            self.aprovado = True
       
    
    def reprovado(self):
            self.aprovado = False
        
    
    def __str__(self):
        status = "Aprovado" if self.aprovado else "Reprovado"
        return f"{self.nome} - {self.função} - [{status}]"
    
class Funcionario:
    def __init__(self, nome, idade, sexo, salario, funcao):
        self.nome = nome
        self.idade = int(idade)
        self.sexo = sexo
        self.salario = int(salario)
        self.funcao = funcao 
        self.admitido = False

    def admitir(self):
        if not self.admitido:
            self.admitido = True
            return True
        return False
    
    def demitido(self):
        if self.admitido:
            self.admitido = False
            return True
        return False
    
    def __str__(self):
        status_candidato = "Admitido" if self.admitido else "Demitido"
        return f"{self.nome} - {self.funcao} - [{status_candidato}]"
    
class RecursosHumanos:
    def __init__(self):
        self.funcionarios = []
        self.candidatos = []

    def adicionar_candidatos(self, candidato):
        self.candidatos.append(candidato)
        
    def listar_candidatos(self):
        if not self.candidatos:
            print("Nenhum candidato cadastrado")
        for i, candidatos in enumerate(self.candidatos, 1):
           print(f'{i}. {candidatos}')

    def aprovar_candidato(self, nome):
        for candidato in self.candidatos:
            if candidato.nome.lower() == nome.lower():
                if candidato.aprovado():
                    print(f"O candidato '{nome}' foi aprovado.")
                    return True
                else:
                    print(f"O candidato '{nome}' não foi encontrado.")
                    return
        print(f"O candidato '{nome}' não foi encontrado.")

    def reprovar_candidato(self, nome):
        for candidato in self.candidatos:
            if candidato.nome.lower() == nome.lower():
                if candidato.reprovado():
                    print(f"O candidato '{nome}' foi reprovado.")
                    return False
                else:
                    print(f"O candidato '{nome}' não foi encontrado.")
                    return
        print(f"O candidato '{nome}' não foi encontrado.")

    def adicionar_funcionarios(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionario cadastrado")
        for i, funcionario in enumerate(self.funcionarios, 1):
            print(f'{i}. {funcionario}')


    def demitir_funcionarios(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.nome.lower() == nome.lower():
                if funcionario.demitido():
                    print(f"O funcionario '{nome}' foi demitido.")
                    return
                else:
                    print(f"O funcionario '{nome}' não foi encontrado.")
                    return
        print(f"O funcionario '{nome}' não foi encontrado.")
    
    def admitir_funcionarios(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.nome.lower() == nome.lower():
                if funcionario.admitir():
                    print(f"O funcionario '{nome}' foi admitido.")
                    return True
                else: 
                    print(f"O funcionario '{nome}' já está admitido.")
                    return  False
        print(f"O funcionario '{nome}' não foi encontrado.")
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
    print("1. Detalhes do funcionario") 
    print("2. Admitir funcionario") 
    print("3. Demitir funcionario")
    print("4. Listar funcionarios") 
    print("5. Sair")

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
                pretSalarial = input("Pretensão Salarial:")
                função = input("Função:")
                candidato = ProcessoSeletivo(nome, idade, sexo, pretSalarial, função)  
                rh.adicionar_candidatos(candidato)
            
                if candidato.idade < 18 or candidato.pretSalarial >= 1000:
                    print(f"O candidato {nome} foi reprovado no processo seletivo por ser menor de idade.")
                else :
                    rh.adicionar_candidatos(candidato)
                    print(f"O candidato {nome} está sob análise do RH.")
                  

            if escolha_candidato == '2':
                print("Lista de candidatos")
                rh.listar_candidatos()

            elif escolha_candidato == '3':      
                nome = input("Digite o nome do candidato: ")
                if nome not in rh.candidatos:
                    print(f"O candidato {nome} não foi encontrado.")
                else:
                    rh.aprovar_candidato(nome)
            
            elif escolha_candidato == '4':
                nome = input("Digite o nome do candidato: ")
                rh.reprovar_candidato(nome)
                

        
        if escolha == '2':
            funcionarios_menu()
            escolha_funcionario = input("Escolha uma opção: ")


            if escolha_funcionario == '1':
                nome = input("Nome:")
                idade = input("Idade:") 
                sexo = input("Sexo:")   
                salario = input("Salario:") 
                funcao = input("Função:")   
                funcionario = Funcionario(nome, idade, sexo, salario, funcao)
    
          

            elif escolha_funcionario == '2':    
                nome = input("Digite o nome do funcionario:") 
                rh.admitir_funcionarios(nome) 
            

            elif escolha_funcionario == '3':
                nome = input("Digite o nome do funcionario: ")
                rh.demitir_funcionarios(nome)  

            elif escolha_funcionario == '4':
                print("Lista de funcionarios")     
                rh.listar_funcionarios()  

            elif escolha_funcionario == '5':
                break

            else:
                print("Opção inválida")
    
if __name__ == '__main__':
    main()