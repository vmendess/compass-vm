# Exercícios - Sprint 3

## Descrição Geral
Este diretório contém os exercícios relacionados à Sprint 3, organizados em subdiretórios para facilitar a compreensão e execução. Cada subdiretório corresponde a uma etapa com objetivos específicos, scripts em Python e uso de Docker para execução.

## Estrutura de Diretórios
```
Exercicios/
├── etapa-1/
│   ├── carguru.py
│   └── Dockerfile
├── etapa-2/
│   ├── Dockerfile
│   ├── main.py
│
│── README.md - Descrição da pasta Exercicíos da Sprint 3
```

---

### Etapa 1: carguru.py
#### Descrição
O objetivo desta etapa é utilizar **Docker** para executar o script Python `carguru.py`. Este script sugere aleatoriamente um carro de uma lista pré-definida.

#### Arquivos
- `carguru.py`: Script Python que realiza a seleção aleatória.
- `Dockerfile`: Arquivo para construir a imagem Docker que executa o script.

#### Como Executar
1. Certifique-se de ter o Docker instalado.
2. Navegue até o diretório `etapa-1`.
3. Construa a imagem Docker:
   ```bash
   docker build -t carguru .
   ```
4. Execute o container:
   ```bash
   docker run carguru
   ```

#### Exemplo de Saída
```bash
Você deve dirigir um Chevrolet Camaro
```

---

### Etapa 2: Mascarar Dados com Docker
#### Descrição
Esta etapa consiste na criação de um container Docker que executa um script Python para mascarar dados. O script gera hashes SHA-1 de strings fornecidas pelo usuário.

#### Arquivos
- `Dockerfile`: Configuração para criar a imagem Docker.
- `main.py`: Script que recebe strings, gera hashes SHA-1 e exibe no terminal.

#### Como Executar
1. Certifique-se de ter o Docker instalado.
2. Navegue até o diretório `etapa-2`.
3. Construa a imagem Docker:
   ```bash
   docker build -t mascarar-dados .
   ```
4. Execute o container:
   ```bash
   docker run -it mascarar-dados
   ```

#### Exemplo de Execução
```bash
Digite uma string (ou "sair" para encerrar): teste
Hash SHA-1: a94a8fe5ccb19ba61c4c0873d391e987982fbbd3
Digite uma string (ou "sair" para encerrar): sair
Encerrando o programa.
```