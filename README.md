#  Datos de la organización de The Guardians of the Globe

## Descripción General

Bienvenido a los datos de la organización de The Guardians of the Globe, un proyecto diseñado para gestionar, tanto héroes como villanos, involucrados en la continua batalla por proteger la Tierra. Este proyecto, desarrollado utilizando el marco de trabajo Django y potenciado por la base de datos SQLiteStudio, sirve para registrar y rastrear los detalles de cada héroe, villano, patrocinador y pelea dentro de la organización The Guardians of the Globe.

## Componentes del Proyecto

### Héroe

- **Detalles**: Explora información como el nombre, la edad, el origen, las habilidades y las debilidades de cada héroe.
- **Funcionalidad**: Crea, edita y elimina perfiles de héroes.
- **Consultas**: Busca fácilmente a un héroe por su nombre, habilidades, origen o debilidades.

### Villano

- **Detalles**: Adéntrate en la historia de los villanos, incluyendo su nombre, edad, origen, habilidades y debilidades.
- **Funcionalidad**: Crea, edita y elimina perfiles de villanos.
- **Consultas**: Realiza búsquedas de villanos por nombre, habilidades, origen o debilidades.

### Pelea

- **Detalles**: Accede a información sobre las batallas, incluyendo los nombres del héroe y villano participantes y el resultado de la pelea.
- **Funcionalidad**: Crea, edita y elimina registros de peleas.
- **Consultas**: Busca una pelea por el nombre del villano o el nombre del héroe.

### Patrocinador

- **Detalles**: Obtén información sobre los patrocinadores, incluyendo su nombre, el héroe que patrocinan, el monto y el origen de los fondos.
- **Funcionalidad**: Crea, edita y elimina perfiles de patrocinadores.
- **Consultas**: Recupera información sobre todos los patrocinios asociados a un patrocinador específico o descubre cuántos patrocinadores tiene un héroe.

## ¿Por Qué Este Proyecto?

The Guardians of the Globe, un equipo de individuos extraordinarios con superpoderes, incluyendo al icónico Mark Greyson, tienen la misión de proteger la Tierra de villanos, amenazas externas y peligros internos. Este proyecto simplifica la gestión de cada héroe, villano, patrocinador y pelea dentro de la organización, proporcionando una base de datos integral para un registro y análisis eficientes.

##Tecnologías Utilizadas

- **Marco de Trabajo**: Djando.
- **Base de Datos**: SQLiteStudio.

## Uso

Para ejecutar el proyecto, navega a la terminal en Visual Studio Code e ingresa el siguiente comando:

```bash
python manage.py runserver
