-- E15: Apresente a query para listar os c�digos das vendas identificadas como deletadas. 
-- Apresente o resultado em ordem crescente.

-- Resolu��o:
SELECT cdven
FROM tbvendas
WHERE deletado = 1
ORDER BY cdven;
