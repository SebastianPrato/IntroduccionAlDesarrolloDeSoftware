CREATE DATABASE Clase17;
USE Clase17;

CREATE TABLE IF NOT EXISTS estudiantes (
    padron INT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    PRIMARY KEY (padron)
);

DROP TABLE  estudiantes;

SELECT * FROM estudiantes;

INSERT INTO estudiantes (padron, nombre, apellido)
VALUES
    (123998, 'Juan', 'Gomez'),
    (124000, 'Juan', 'Perez'),
    (124100, 'Marta', 'Garcia');


DELETE FROM estudiantes WHERE padron < 1000;

TRUNCATE TABLE estudiantes;

ALTER TABLE estudiantes ADD (notas INT);

ALTER TABLE estudiantes DROP COLUMN  notas;