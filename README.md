# Proyecto: Tolerante a fallas

Descripción
-----------
Pequeño proyecto con un script principal llamado `Act1.py`. Este repositorio contiene la actividad 1 relacionada con tolerancia a fallas; el README explica cómo ejecutar el script y qué esperar.

Este repositorio contiene una implementación del algoritmo de **Eliminación Gaussiana simple** en Python para resolver sistemas de ecuaciones lineales de la forma $Ax = b$.

El código está diseñado con fines educativos para demostrar los fundamentos del álgebra lineal numérica, el uso de la librería `NumPy` para operaciones vectorizadas y la gestión de excepciones en ingeniería de software.

## Características Principales

* **Eliminación Hacia Adelante:** Algoritmo que transforma la matriz aumentada en una matriz triangular superior.
* **Sustitución Hacia Atrás:** Cálculo iterativo de las incógnitas despejando desde la última ecuación hasta la primera.
* **Vectorización con NumPy:** Uso de operaciones de arrays para restar filas completas y calcular productos punto, mejorando la eficiencia y legibilidad del código.
* **Control de Errores:** Sistema dedicado para identificar matrices singulares (aquellas con determinante igual a cero o mal condicionadas numéricamente).

Requisitos
----------
- Python 3.8 o superior

Instalación
-----------
1. Clona o descarga este repositorio.
2. Asegúrate de tener Python instalado.

Uso
---
En la raíz del proyecto ejecuta:

```bash
python Act1.py
```

Si tu sistema usa `python3` en lugar de `python`:

```bash
python3 Act1.py
```

Estructura del proyecto
-----------------------
- `Act1.py`: Script principal de la actividad.
- `README.md`: Este archivo.

Contribuciones
--------------
Este es un proyecto pequeño; si quieres mejorar el README o añadir ejemplos, abre un issue o un pull request.

Licencia
--------
--
Contacto
-------
--
