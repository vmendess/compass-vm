-- E12: Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). 
-- As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas. 
-- Observação: Apenas vendas com status concluído.

-- Resolução:
SELECT 
    d.cddep,
    d.nmdep,
    d.dtnasc,
    ROUND(SUM(v.qtd * v.vrunt), 2) AS valor_total_vendas
FROM 
    tbdependente d
JOIN 
    tbvendas v ON d.cdvdd = v.cdvdd
WHERE 
    v.status = 'Concluído'
GROUP BY 
    d.cddep, d.nmdep, d.dtnasc, d.cdvdd
HAVING 
    valor_total_vendas = (
        SELECT 
            MIN(valor_total)
        FROM (
            SELECT 
                cdvdd,
                SUM(qtd * vrunt) AS valor_total
            FROM 
                tbvendas
            WHERE 
                status = 'Concluído'
            GROUP BY 
                cdvdd
            HAVING 
                valor_total > 0
        )
    );

