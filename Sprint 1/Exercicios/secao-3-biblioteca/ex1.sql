-- E01: Apresente a query para listar todos os livros publicados ap�s 2014. 
-- Ordenar pela coluna cod, em ordem crescente, as linhas. 
-- Aten��o �s colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma.

-- Resposta:
SELECT *
FROM livro
WHERE publicacao > '2014-12-31'
ORDER BY cod;