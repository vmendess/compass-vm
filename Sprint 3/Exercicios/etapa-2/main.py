import hashlib  # Importa o módulo hashlib para trabalhar com algoritmos de hash

# Loop infinito para manter o programa em execução até o usuário decidir sair
while True:
    # Solicita ao usuário que digite uma string ou "sair" para encerrar
    entrada = input('Digite uma string (ou "sair" para encerrar): ').strip()
    
    # Verifica se o usuário digitou "sair" (ignora maiúsculas e minúsculas)
    if entrada.lower() == 'sair':
        print('Encerrando o programa.')  # Mensagem de encerramento
        break  # Sai do loop e finaliza o programa
    
    # Verifica se a entrada está vazia
    if not entrada:
        print('Entrada inválida. Por favor, digite algo.')  # Informa que a entrada foi inválida
        continue  # Volta ao início do loop para pedir uma nova entrada
    
    # Calcula o hash SHA-1 da string digitada
    hash_sha1 = hashlib.sha1(entrada.encode()).hexdigest()
    
    # Exibe o hash gerado
    print(f'Hash SHA-1: {hash_sha1}')


