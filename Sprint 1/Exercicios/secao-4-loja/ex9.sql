-- E09: Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. 
-- As colunas presentes no resultado devem ser cdpro e nmpro.

-- Resolução:
SELECT 
    TBVENDAS.cdpro,
    TBVENDAS.nmpro
FROM 
    TBVENDAS
WHERE 
    TBVENDAS.status = 'Concluído'
    AND TBVENDAS.dtven BETWEEN '2014-02-03' AND '2018-02-02'
GROUP BY 
    TBVENDAS.cdpro, TBVENDAS.nmpro
ORDER BY 
    COUNT(TBVENDAS.cdven) DESC
LIMIT 1;
