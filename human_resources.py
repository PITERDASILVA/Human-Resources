class Funcionario:
    def __init__(self, nome, idade, sexo, salario, funcao):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.salario = salario
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
            print(f"O funcionario {nome} foi aprovado  no processo seletivo com sucesso.")
          

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