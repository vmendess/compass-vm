-- A tabela tb_locacao foi dividida para seguir a normalização, organizando os dados em entidades distintas
-- Cada uma tem sua função: cliente, carro, vendedor e combustivel guardam informações específicas,
-- enquanto locacao conecta tudo e garante a integridade com as chaves estrangeiras.
CREATE TABLE cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(100),
    estadoCliente VARCHAR(2),
    paisCliente VARCHAR(50)
);

CREATE TABLE combustivel (
    idcombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(50)
);

CREATE TABLE carro (
    idCarro INT PRIMARY KEY,
    classCarro VARCHAR(50), -- Tirei o I, era 'Classi', erro de ortografia
    marcaCarro VARCHAR(50),
    modeloCarro VARCHAR(50),
    anoCarro INT,
    idcombustivel INT,
    FOREIGN KEY (idcombustivel) REFERENCES combustivel(idcombustivel)
);

CREATE TABLE vendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(100),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(2)
);

-- Criação da tabela de locação, que será a tabela principal no modelo relacional.
-- Armazena informações das locações de veículos, conectando cliente, carro e vendedor.
CREATE TABLE locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idVendedor INT,
    kmCarro INT,
    -- Formato DATETIME para armazenar data e hora completas da locação.
   	dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(10, 2),
    -- Formato DATE na devolução, pois a hora da entrega é armazenada separadamente.
    -- Escolha do formato DATE é ideal para quando só precisamos da data.
    dataEntrega DATE,
    horaEntrega TIME,
    -- Definição das chaves estrangeiras para garantir integridade referencial
    FOREIGN KEY (idCliente) REFERENCES cliente(idCliente), -- Referencia o cliente,
    FOREIGN KEY (idCarro) REFERENCES carro(idCarro),       -- Carro, vendedor
    FOREIGN KEY (idVendedor) REFERENCES vendedor(idVendedor)
);

-- Atualização da tabela tb_locacao para corrigir o formato incorreto das datas nos campos dataLocacao e dataEntrega.
-- O formato atual está errado, como no exemplo: 20.150.110, que deve ser interpretado como 2015-01-10.
-- A solução remove todos os pontos (.), converte o valor para o formato 20150110 e, em seguida, insere os hifens (-) 
-- nos locais apropriados para transformar no formato padrão ISO: YYYY-MM-DD.
UPDATE tb_locacao
   SET dataLocacao = SUBSTR(REPLACE(dataLocacao, '.', ''), 1, 4)
                     || '-'
                     || SUBSTR(REPLACE(dataLocacao, '.', ''), 5, 2)
                     || '-'
                     || SUBSTR(REPLACE(dataLocacao, '.', ''), 7, 2);

UPDATE tb_locacao
   SET dataEntrega = SUBSTR(REPLACE(dataEntrega, '.', ''), 1, 4)
                     || '-'
                     || SUBSTR(REPLACE(dataEntrega, '.', ''), 5, 2)
                     || '-'
                     || SUBSTR(REPLACE(dataEntrega, '.', ''), 7, 2);


-- Selets da tb_locacao com insercao no modelo normalizado
-- Utilizei o SELECT DISTINCT para ver apenas os valores unicos
-- Inserir clientes
INSERT INTO cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;

-- Inserindo combustivel
INSERT INTO combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT 
    idcombustivel, 
    tipoCombustivel
FROM tb_locacao;

-- Inserindo vendedores
INSERT INTO vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;

-- Inserindo locações
INSERT INTO locacao (idLocacao, idCliente, idCarro, idVendedor, kmCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)
SELECT idLocacao, idCliente, idCarro, idVendedor, kmCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM tb_locacao;

-- Inserindo carros
INSERT INTO carro (idCarro, classCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel)
SELECT DISTINCT idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro,idcombustivel 
FROM tb_locacao;

-- Modelo Dimensional baseado no relacional
-- FATO: Tabela principal com as informações mais importantes
CREATE VIEW fato_locacao AS
SELECT 
    idLocacao,
    idCliente,
    idCarro,
    idVendedor,
    qtdDiaria * vlrDiaria as valor_total_locacao,
    date(dataLocacao) as data_locacao
FROM locacao;

-- DIMENSÕES: Tabelas de características
-- Dimensão Cliente
CREATE VIEW dim_cliente AS
SELECT
    idCliente,
    nomeCliente,
    estadoCliente
FROM cliente;

-- Dimensão Carro
CREATE VIEW dim_carro AS
SELECT
    c.idCarro,
    c.marcaCarro,
    c.modeloCarro,
    c.classCarro,
    c.anoCarro,
    cb.tipoCombustivel
FROM carro c
JOIN combustivel cb ON c.idCombustivel = cb.idCombustivel;

-- Dimensão Vendedor
CREATE VIEW dim_vendedor AS
SELECT
    idVendedor,
    nomeVendedor,
    estadoVendedor
FROM vendedor;

-- Dimensões de tempo criadas para organizar as datas de locação e entrega.
-- Facilitam análises por ano, mês e dia, simplificando relatórios e consultas.
CREATE VIEW dim_tempo_locacao AS
SELECT DISTINCT
    -- Cada dia é representado por uma chave (data_pk), usada para integrar com tabelas de fatos.
	date(dataLocacao) AS data_pk,            
    strftime('%Y', dataLocacao) AS ano        -- Ano extraído da data
FROM locacao
WHERE dataLocacao IS NOT NULL
ORDER BY data_pk;


CREATE VIEW dim_tempo_entrega AS
SELECT DISTINCT
    date(dataEntrega) AS data_pk,
    -- Os códigos %Y, %m e %d no strftime extraem ano, mês e dia da data, formatando no padrão desejado. 
    strftime('%Y', dataEntrega) AS ano,
    strftime('%m', dataEntrega) AS mes,
    strftime('%d', dataEntrega) AS dia
FROM locacao
WHERE dataEntrega IS NOT NULL
ORDER BY data_pk;

-- Consulta simples:
SELECT * FROM fato_locacao;
SELECT * FROM dim_cliente;
SELECT * FROM dim_carro;
SELECT * FROM dim_vendedor;
SELECT * FROM dim_tempo_locacao;
SELECT * FROM dim_tempo_entrega;
SELECT *FROM tb_locacao;

-- Consultas de validação:
-- Modelo Relacional:
-- Valida o modelo relacional: verifica a relação entre locação, cliente, carro e vendedor.
SELECT 
    l.idLocacao,      
    c.nomeCliente,     
    car.modeloCarro,   
    v.nomeVendedor,    
    l.dataLocacao,     
    l.dataEntrega      
FROM locacao l
JOIN cliente c ON l.idCliente = c.idCliente    -- Relacionamento com cliente
JOIN carro car ON l.idCarro = car.idCarro      -- Relacionamento com carro
JOIN vendedor v ON l.idVendedor = v.idVendedor -- Relacionamento com vendedor
LIMIT 10; 

-- Validação do modelo dimensional com todas as dimensões conectadas à tabela fato.
SELECT 
    l.idLocacao, 
    d.ano, 
    c.nomeCliente, 
    car.modeloCarro, 
    v.nomeVendedor
FROM locacao l
JOIN dim_tempo_locacao d ON l.dataLocacao = d.data_pk
JOIN cliente c ON l.idCliente = c.idCliente
JOIN carro car ON l.idCarro = car.idCarro
JOIN vendedor v ON l.idVendedor = v.idVendedor
LIMIT 10;







