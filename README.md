# Proyecto Urban Grocers 
# Proyecto QA - Urban Grocers

Este proyecto contiene la automatización de las pruebas para el endpoint de creación de kits (`/api/v1/kits`) de la aplicación Urban Grocers.

## Tecnologías utilizadas
- Python 3
- Pytest
- Requests

## Cómo ejecutar las pruebas

1. Clona este repositorio en tu computadora.
2. Instala las dependencias necesarias ejecutando en la terminal:
   `pip install requests pytest`
3. Inicia el servidor de Urban Grocers en la plataforma de TripleTen.
4. Copia la nueva URL del servidor y actualízala en el archivo `configuration.py` dentro de la variable `URL_SERVICE`.
5. Ejecuta las pruebas con el siguiente comando:
   `python -m pytest create_kit_name_kit_test.py -v`

## Notas sobre los resultados
Durante la ejecución, es posible que algunas pruebas fallen con `FAILED`. Esto se debe a bugs reales encontrados en la API (por ejemplo, permitir nombres vacíos o de más de 511 caracteres). El código de automatización está diseñado para detectar estos comportamientos inesperados.

## Autor
Steven Grajales