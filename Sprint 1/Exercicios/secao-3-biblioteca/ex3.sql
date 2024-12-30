-- E03: Apresente a query para listar as 5 editoras com mais livros na biblioteca. 
-- O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. 
-- Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

-- Resolução:
SELECT COUNT(*) as quantidade,
       ed.nome,
       e.estado,
       e.cidade
FROM LIVRO l, EDITORA ed, ENDERECO e
WHERE l.editora = ed.codEditora
AND ed.endereco = e.codEndereco
GROUP BY ed.codEditora
ORDER BY quantidade DESC
LIMIT 5;