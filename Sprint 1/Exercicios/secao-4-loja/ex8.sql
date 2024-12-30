-- E08: Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída. 
-- As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

-- Resolução
SELECT 
    TBVENDEDOR.cdvdd,
    TBVENDEDOR.nmvdd
FROM 
    TBVENDEDOR
JOIN 
    TBVENDAS
ON 
    TBVENDEDOR.cdvdd = TBVENDAS.cdvdd
WHERE 
    TBVENDAS.status = 'Concluído'
GROUP BY 
    TBVENDEDOR.cdvdd, TBVENDEDOR.nmvdd
ORDER BY 
    COUNT(TBVENDAS.cdven) DESC
LIMIT 1;

