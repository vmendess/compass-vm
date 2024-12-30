-- E10: A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. 
-- O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 
-- Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.

-- Resolução:
SELECT 
    v.nmvdd AS vendedor,
    ROUND(SUM(ven.qtd * ven.vrunt), 2) AS valor_total_vendas,
    ROUND(SUM(ven.qtd * ven.vrunt * v.perccomissao / 100.0), 2) AS comissao
FROM 
    tbvendas ven
INNER JOIN 
    tbvendedor v ON ven.cdvdd = v.cdvdd
WHERE 
    ven.status = 'Concluído'
GROUP BY 
    v.nmvdd
ORDER BY 
    comissao DESC;

