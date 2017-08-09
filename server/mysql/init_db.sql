DROP DATABASE cliente2;

CREATE DATABASE cliente2;
USE cliente2;
CREATE TABLE IF NOT EXISTS sensors (
  id          INT(4)      NOT NULL AUTO_INCREMENT,
  model       VARCHAR(14) NOT NULL,
  performance VARCHAR(20) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS reading (
  cont       INT(4) NOT NULL AUTO_INCREMENT,
  id         INT(4) NOT NULL,
  sensor_num INT(4) NOT NULL,
  value      FLOAT(5, 2),
  time       DATETIME,
  PRIMARY KEY (cont),
  FOREIGN KEY (id) REFERENCES sensores (id)
);

INSERT INTO sensores (model, performance) VALUES ("lm35", "temperature");


/*
INSERT INTO sensores(nombre, tipo) VALUES ("lm36", "temperatura");
INSERT INTO sensores(nombre, tipo) VALUES ("lm37", "temperatura");
INSERT INTO sensores(nombre, tipo) VALUES ("lm38", "temperatura");
*/


