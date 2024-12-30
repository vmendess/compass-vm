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