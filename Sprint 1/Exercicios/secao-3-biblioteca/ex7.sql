-- E07: Apresente a query para listar o nome dos autores com nenhuma publica��o. 
-- Apresent�-los em ordem crescente.

-- Resolu��o:
SELECT 
    autor.nome
FROM 
    autor
LEFT JOIN 
    livro
ON 
    autor.codautor = livro.autor
WHERE 
    livro.cod IS NULL
ORDER BY 
    autor.nome;

