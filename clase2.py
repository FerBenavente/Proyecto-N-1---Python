import pandas as pd
import numpy as np

# Genera un rango de fechas desde el 20220101 por 6 días en GMT-5
dias = pd.date_range("20220301", periods=4)

# Genera una matriz de aleatorios de 6 filas por 4 columnas
aleatorios = np.random.randn(4, 4)

# Genera un nuevo dataframe a partir de una matriz
data_frame = pd.DataFrame(aleatorios, columns=dias,
                          index=["A", "B", "C", "D"])

estudiantes = pd.read_csv('ejemplo.csv')
print(estudiantes)

# 1. De la tabla, me muestren solo los alumnos que tuvieron 15 o más de nota
print(estudiantes[estudiantes["Nota"] >= 15])
print(estudiantes[estudiantes.Nota >= 15])

# 2. Mostrar el nombre completo (Nombre y apellido) de los estudiantes en una sola columna
estudiantes["NombreCompleto"] = estudiantes.Nombre + \
    " " + estudiantes.Apellidos
print(estudiantes)

# 3. Ordenar la tabla por apellido (de la A a la Z)
estudiantes = estudiantes.sort_values(by='Apellidos', ascending=True)
print(estudiantes)
