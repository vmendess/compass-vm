-- E16: Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. 
-- As colunas presentes no resultado devem ser estado, nmprod e quantidade_media. 
-- Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. 
-- Ordene os resultados pelo estado (1º) e nome do produto (2º).

-- Resolução:
SELECT 
    estado,
    nmpro,
    ROUND(AVG(qtd), 4) AS quantidade_media
FROM 
    tbvendas
WHERE 
    status = 'Concluído'
GROUP BY 
    estado, nmpro
ORDER BY 
    estado ASC, 
    nmpro ASC;
