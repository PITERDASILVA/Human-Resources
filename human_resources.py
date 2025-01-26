class ProcessoSeletivo:
    def __init__(self, nome, idade, sexo, pretSalarial, função):
        self.nome = nome
        self.idade = int(idade)
        self.sexo = sexo
        self.pretSalarial = int(pretSalarial)   
        self.função = função
        self.aprovado = False

    def candidato_aprovado(self): 
        if not self.aprovado:
            self.aprovado = True
            return True
        return False
    
    def candidato_reprovado(self):
        if self.aprovado:
            self.aprovado = False
            return True
        return False
    
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
        status = "Admitido" if self.admitido else "Demitido"
        return f"{self.nome} - {self.funcao} - [{status}]"
    
class RecursosHumanos:
    def __init__(self):
        self.funcionarios = []
    
    def adicionar_funcionarios(self, funcionario):
        self.funcionarios.append(funcionario)

    def adicionar_candidatos(self, candidato):
        self.funcionarios.append(candidato)

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionario cadastrado")
        for i, funcionario in enumerate(self.funcionarios, 1):
            print(f'{i}. {funcionario}')
    
    def listar_candidatos(self):
        if not self.funcionarios:
            print("Nenhum candidato cadastrado")
        for i, funcionario in enumerate(self.funcionarios, 1):
            if not funcionario.admitido:
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

def funcionarios_menu():
    print("Menu de funcionarios")
    print("1. Processo seletivo") 
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
            print("Dados Pessoais do Candidto")
            print("---------------------------")
            nome = input("Nome:")
            idade = input("Idade:")
            sexo = input("Sexo:")
            pretSalarial = input("Pretensão Salarial:")
            função = input("Função:")
            candidato = ProcessoSeletivo(nome, idade, sexo, pretSalarial, função)  
            rh.adicionar_candidatos(candidato)
            
            if candidato.idade <= 18 & candidato.pretSalarial >= 1000:
                print(f"O candidato {nome} foi reprovado no processo seletivo por ser menor de idade.")
            else :
                rh.adicionar_funcionarios(candidato)
                print(f"O candidato {nome} está sob análise do RH.")
                break
                menu_candidato()

        
        if escolha == '2':
            funcionarios_menu()
            break

        funcionarios_menu()
        escolha = input("Escolha uma opção: ")


        if escolha == '1':
            nome = input("Nome:")
            idade = input("Idade:")
            sexo = input("Sexo:")
            salario = input("Salario:")
            funcao = input("Função:")
            funcionario = Funcionario(nome, idade, sexo, salario, funcao)  
            rh.adicionar_funcionarios(funcionario)
            print(f"O candidato {nome} foi aprovado  no processo seletivo com sucesso.")
          

        elif escolha == '2':    
            nome = input("Digite o nome do funcionario:") 
            rh.admitir_funcionarios(nome) 
            

        elif escolha == '3':
            nome = input("Digite o nome do funcionario: ")
            rh.demitir_funcionarios(nome)  

        elif escolha == '4':
            print("Lista de funcionarios")     
            rh.listar_funcionarios()  

        elif escolha == '5':
            break

        else:
            print("Opção inválida")
    
if __name__ == '__main__':
    main()