# Nivelación en Python - Actividad Final Corte #1

Este repositorio contiene la solución a la actividad final basada en los principios de la Programación Orientada a Objetos en Python.

## Descripción de la Analogía
Para el desarrollo de esta actividad, se seleccionó la analogía de la **Biología Celular**. Se simuló el comportamiento de organismos unicelulares (`Celula`), fusionando tres conceptos mediante herencia múltiple:

1. **`OrganismoBase` (Clase Abstracta):** Controla las especificaciones generales de todo organismo como el nombre científico y reino, además de obligar a los modelos descendientes a definir cómo `realizar_metabolismo()` y cómo ser representados en texto (`__str__`).
2. **`SistemaReproductor` (Clase Complementaria 1):** Un módulo que administra el tipo de reproducción celular y ofrece capacidades como `reproducirse()`.
3. **`SistemaDefensa` (Clase Complementaria 2):** Un módulo que le añade componentes de defensa inmunológica dando la opción de `activar_defensa()` y `producir_anticuerpos()`.

El resultado es la clase final `Celula` que no solo hereda todas estas capacidades, sino que hace uso de **encapsulamiento** para resguardar su `_energia`. A este valor solo se le puede acceder de forma segura a través de los decoradores `@property` y ser modificado bajo validaciones estrictas en el `setter` (ej. no se pueden asignar valores negativos, mayores a 10000, o tipos de datos no numéricos).

## Instrucciones para ejecutar
1. Asegurarse de tener Python 3.x instalado de forma local.
2. Descargar este repositorio abriendo una terminal o descargar los archivos directamente desde GitHub.
3. Posicionarse sobre la carpeta de los archivos desde la consola.
4. Ejecutar el script enviando la instrucción:

```bash
python celula.py
```

Al ejecutarse, podrás observar por consola todas las pruebas unitarias validando la herencia múltiple, polimorfismo sobre 3 objetos distintos y la validación de los constructores y atributos encapsulados.


## Autor
- Alexander Arpushaina
- Cristian Padilla
- Programa: Ingeniería de Sistemas
- Facultad de Ingeniería - Universidad de La Guajira (Uniguajira)
