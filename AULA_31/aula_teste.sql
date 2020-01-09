
-- INSERIR VALOR EM UMA TABELA ----------------------------------------

INSERT INTO topskills01.Morgana (id,nome,idade,sexo)
VALUES (3,'Pedro',15,'Mas');


-- SELECIONAR VALORES DE UMA TABELA ----------------------------------------

SELECT id, nome, idade, sexo
FROM topskills01.Morgana;

-- ATUALIZAR VALORES DE UMA TABELA ----------------------------------------

UPDATE topskills01.Morgana
SET nome='', idade=NULL, sexo=''
WHERE id=0;

-- DELETAR VALORES DE UMA TABELA ----------------------------------------

DELETE FROM topskills01.Morgana
WHERE id=0;


MERGE INTO topskills01.Morgana AS tgt
USING SOURCE_TABLE AS src
ON (tgt.id=src.id)
WHEN MATCHED
THEN UPDATE SET
tgt.nome=src.nome, tgt.idade=src.idade, tgt.sexo=src.sexo
WHEN NOT MATCHED
THEN INSERT (id, nome, idade, sexo)
VALUES (src.id, src.nome, src.idade, src.sexo);


-- CRIANDO UMA TABELA ----------------------------------------

CREATE TABLE Morgana (
  id int(11) NOT NULL AUTO_INCREMENT,
  nome varchar(100) NOT NULL,
  idade int(11) DEFAULT NULL,
  sexo tinytext NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1

--------------------------------------- CÓDIGOS ALEATÓRIOS ---------------------------------------


CREATE DEFINER=`topskills01`@`%` PROCEDURE `topskills01`.`IRINEU`()
BEGIN
    DECLARE i int DEFAULT 1;
    WHILE i <= 500 DO
   		insert into Keunan (nome,sobrenome,idade) values ('IRINEU','Nao fui eu',2 ); 
        SET i = i + 1;
    END WHILE;
END


CREATE DEFINER=`topskills01`@`%` PROCEDURE `topskills01`.`IRINEUDELET`()
BEGIN
   		Delete from Morgana where nome = 'IRINEU'; 

END