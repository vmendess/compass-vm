-- E04: Apresente a query para listar a quantidade de livros publicada por cada autor. 
-- Ordenar as linhas pela coluna nome (autor), em ordem crescente. 
-- Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

-- Resolução:
SELECT 
    a.nome,
    a.codAutor,
    a.nascimento,
    COUNT(l.cod) as quantidade
FROM AUTOR a
LEFT JOIN LIVRO l ON l.autor = a.codAutor
GROUP BY a.codAutor, a.nome, a.nascimento
ORDER BY a.nome;