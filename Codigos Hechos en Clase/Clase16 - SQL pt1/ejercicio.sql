CREATE TABLE IF NOT EXISTS  alumnos(
    padron INT NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    fechaIngreso DATE NOT NULL,
    fechaEgreso DATE NOT NULL,
    PRIMARY KEY (padron)
);

CREATE TABLE IF NOT EXISTS materias(
    depto INT NOT NULL,
    codigo INT NOT NULL,
    materia VARCHAR(50),
    PRIMARY KEY (codigo)
);

CREATE TABLE IF NOT EXISTS notas(
    depto INT NOT NULL,
    codigo INT NOT NULL,
    padron INT NOT NULL,
    nota INT NOT NULL
);

CREATE TABLE IF NOT EXISTS departamento(
    codigo INT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    PRIMARY KEY (codigo)
);

SELECT materia
FROM materias
WHERE depto in (61,62)

