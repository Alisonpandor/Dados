# Inicializa uma lista vazia para armazenar os livros
lista = []

# Loop para adicionar 3 livros à lista
for i in range(3):
    livro = input("Digite um livro: ")
    paginas = int(input('numero de páginas: '))
    # Adiciona um tupla (livro, páginas) à lista
    lista.append((livro, paginas))

# Adiciona novamente o último livro (nota: há duplicação aqui)
lista.append((livro, paginas))

# Exibe a lista completa
print(lista)
# Exibe a quantidade total de itens na lista
print(len(lista))

# Exibe o cabeçalho da seção
print("\n--- Lista de Livros ---")

# Itera sobre a lista e exibe cada livro com seu índice começando em 1
for i, (livro, paginas) in enumerate(lista, 1):
    print(f"{i}. {livro} - {paginas} páginas")
    
    # Calcula o total de páginas somando todas as páginas dos livros
    total_paginas = sum(paginas for livro, paginas in lista)
    print(f"\nTotal de páginas: {total_paginas}")
    
    # Cria um conjunto vazio para armazenar os índices dos livros lidos
    livros_lidos = set()
    
    # Loop infinito para o menu de marcação de livros como lido
    while True:
        # Solicita ao usuário que escolha um livro ou digite 'sair' para encerrar
        opcao = input("\nDigite o número do livro para marcar como lido (ou 'sair' para encerrar): ")
        
        # Se o usuário digitar 'sair', encerra o loop
        if opcao.lower() == 'sair':
            break
        
        try:
            # Converte a opção para inteiro e subtrai 1 para acessar o índice correto
            num = int(opcao) - 1
            
            # Verifica se o número está dentro do intervalo válido
            if 0 <= num < len(lista):
                # Adiciona o livro ao conjunto de lidos
                livros_lidos.add(num)
                
                # Exibe o cabeçalho da seção de livros lidos
                print("\n--- Livros Lidos ---")
                
                # Itera sobre a lista e exibe cada livro com seu status
                for i, (livro, paginas) in enumerate(lista, 1):
                    # Define o status como "✓ Lido" ou "○ Não lido"
                    status = "✓ Lido" if i-1 in livros_lidos else "○ Não lido"
                    print(f"{i}. {livro} - {paginas} páginas [{status}]")
                
                # Calcula total de páginas dos livros lidos
                total_lidos = sum(paginas for i, (livro, paginas) in enumerate(lista) if i in livros_lidos)
                # Calcula total de páginas dos livros não lidos
                total_nao_lidos = sum(paginas for i, (livro, paginas) in enumerate(lista) if i not in livros_lidos)
                
                # Exibe os totais
                print(f"Total de páginas (lidos): {total_lidos}")
                print(f"Total de páginas (não lidos): {total_nao_lidos}")
            else:
                # Mensagem de erro se o número for inválido
                print("Número inválido!")
        except ValueError:
            # Mensagem de erro se o usuário não digitar um número válido
            print("Digite um número válido!")


