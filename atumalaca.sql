create database atividade_sprint;
use atividade_sprint;

CREATE TABLE `tblprojetosprint` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tempo` decimal(18,2) DEFAULT NULL,
  `memoria` decimal(18,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) 
