-- E07: Apresente a query para listar o nome dos autores com nenhuma publicação. 
-- Apresentá-los em ordem crescente.

-- Resolução:
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

