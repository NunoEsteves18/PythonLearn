# Começamos com uma lista de dicionários.
# Cada dicionário representa um piloto e suas informações.
pilotos_f1 = [
    {"nome": "Max Verstappen", "equipe": "Red Bull Racing", "numero": 1},
    {"nome": "Lewis Hamilton", "equipe": "Mercedes", "numero": 44},
    {"nome": "Charles Leclerc", "equipe": "Ferrari", "numero": 16},
    {"nome": "Fernando Alonso", "equipe": "Aston Martin", "numero": 14}
]

def mostrar_pilotos():
    """Mostra todos os pilotos na lista."""
    if not pilotos_f1:
        print("Nenhum piloto cadastrado ainda.")
        return

    print("\n--- Pilotos Atuais da F1 ---")
    for piloto in pilotos_f1:
        print(f"Nome: {piloto['nome']}, Equipe: {piloto['equipe']}, Número: {piloto['numero']}")
    print("----------------------------\n")

def adicionar_piloto():
    """Adiciona um novo piloto à lista."""
    print("\n--- Adicionar Novo Piloto ---")
    nome = input("Digite o nome do piloto: ")
    equipe = input(f"Digite a equipe de {nome}: ")
    # Usamos um loop para garantir que o número seja um inteiro válido
    while True:
        try:
            numero = int(input(f"Digite o número do carro de {nome}: "))
            break # Sai do loop se o número for válido
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para o número do carro.")

    novo_piloto = {"nome": nome, "equipe": equipe, "numero": numero}
    pilotos_f1.append(novo_piloto)
    print(f"Piloto '{nome}' adicionado com sucesso!\n")

def buscar_piloto():
    """Busca um piloto pelo nome."""
    print("\n--- Buscar Piloto ---")
    nome_busca = input("Digite o nome do piloto que deseja buscar: ").strip().lower() # .strip() remove espaços extras e .lower() converte para minúsculas

    encontrado = False
    for piloto in pilotos_f1:
        if piloto['nome'].lower() == nome_busca: # Compara em minúsculas para uma busca mais flexível
            print(f"\nPiloto Encontrado:")
            print(f"Nome: {piloto['nome']}, Equipe: {piloto['equipe']}, Número: {piloto['numero']}")
            encontrado = True
            break # Para a busca assim que encontrar o piloto
    
    if not encontrado:
        print(f"Piloto '{nome_busca}' não encontrado.")
    print("-----------------------\n")


def menu_principal():
    """Mostra o menu principal do programa e gerencia as opções."""
    while True:
        print("--- Menu F1 ---")
        print("1. Ver todos os pilotos")
        print("2. Adicionar novo piloto")
        print("3. Buscar piloto por nome")
        print("4. Sair")
        print("---------------")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            mostrar_pilotos()
        elif opcao == '2':
            adicionar_piloto()
        elif opcao == '3':
            buscar_piloto()
        elif opcao == '4':
            print("Saindo do programa F1. Até mais!")
            break # Sai do loop e encerra o programa
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Chamada da função principal para iniciar o programa
if __name__ == "__main__":
    menu_principal()