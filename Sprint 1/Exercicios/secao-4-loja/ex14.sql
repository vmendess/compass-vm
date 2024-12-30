-- E14: Apresente a query para listar o gasto médio por estado da federação. 
-- As colunas presentes no resultado devem ser estado e gastomedio. 
-- Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente. 
-- Observação: Apenas vendas com status concluído.

-- Resolução:
SELECT 
    tbvendas.estado,
    ROUND(AVG(tbvendas.qtd * tbvendas.vrunt), 2) AS gastomedio
FROM 
    tbvendas
WHERE 
    tbvendas.status = 'Concluído'
GROUP BY 
    tbvendas.estado
ORDER BY 
    gastomedio DESC;

