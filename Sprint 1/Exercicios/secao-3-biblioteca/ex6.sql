-- E06: Apresente a query para listar o autor com maior n�mero de livros publicados. 
-- O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

-- Resolu��o:
SELECT 
    autor.codautor,
    autor.nome,
    COUNT(livro.cod) AS quantidade_publicacoes
FROM 
    autor
LEFT JOIN 
    livro
ON 
    autor.codautor = livro.autor
GROUP BY 
    autor.codautor, autor.nome
ORDER BY 
    quantidade_publicacoes DESC
LIMIT 1;
