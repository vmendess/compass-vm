-- E02: Apresente a query para listar os 10 livros mais caros. 
-- Ordenar as linhas pela coluna valor, em ordem decrescente. 
-- Aten��o �s colunas esperadas no resultado final: titulo, valor.

-- Resolu��o:
SELECT quantidade,nome,estado,cidade
FROM livro
ORDER BY valor DESC
LIMIT 10;
