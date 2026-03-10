SELECT apellido, nombre
FROM estudiantes
WHERE apellido like('%z')


SELECT *
FROM estudiantes
WHERE padron >= 124000;


SELECT *
FROM estudiantes
WHERE padron >= 124000 AND apellido like('%z');

