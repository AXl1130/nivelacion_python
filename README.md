# Nivelación en Python - Actividad Final Corte #1

Este repositorio contiene la solución a la actividad final basada en los principios de la Programación Orientada a Objetos en Python.

## Descripción de la Analogía
Para el desarrollo de esta actividad, se seleccionó la analogía de la **Gestión de Vehículos**. Se simuló la construcción de un coche tecnológico (`VehiculoInteligente`), fusionando tres conceptos mediante herencia múltiple:

1. **`VehiculoBase` (Clase Abstracta):** Controla las especificaciones generales de todo vehículo como la marca y modelo, además de obligar a los modelos descendientes a definir cómo `encender()` y cómo ser representados en texto (`__str__`).
2. **`SistemaMotor` (Clase Complementaria 1):** Un módulo que administra el tipo de combustible que consume y ofrece capacidades como `repostar()`.
3. **`SistemaRastreo` (Clase Complementaria 2):** Un módulo que le añade componentes de rastreo satelital dando la opción de `encender_gps()`.

El resultado es la clase final `VehiculoInteligente` que no solo hereda todas estas capacidades, sino que hace uso de **encapsulamiento** para resguardar su `_kilometraje`. A este valor solo se le puede acceder de forma segura a través de los decoradores `@property` y ser modificado bajo validaciones estrictas en el `setter` (ej. no se puede retroceder el contador de kilometraje).

## Instrucciones para ejecutar
1. Asegurarse de tener Python 3.x instalado de forma local.
2. Descargar este repositorio abriendo una terminal o descargar los archivos directamente desde GitHub.
3. Posicionarse sobre la carpeta de los archivos desde la consola.
4. Ejecutar el script enviando la instrucción:

```bash
python main.py
```

Al ejecutarse, podrás observar por consola todas las pruebas unitarias validando la herencia múltiple, polimorfismo sobre 3 objetos distintos y la validación de los constructores y atributos encapsulados.


## Autor
- Alexander Arpushaina
- Cristian Padilla
- Programa: Ingeniería de Sistemas