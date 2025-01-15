
# Aplicaciones de Lenguaje Natural

Escuela Superior de Cómputo | Proyecto Final | 6BM2 | Ingeniería en Inteligencia Artificial

## Authors

- Bryan Jhoan Cazares Leyva
- Ulises Gachuz Davila
- Jose Juan Gonzalez Fonseca
- Arturo Morales Martinez 


## Description project

Este proyecto es un programa desarrollado en lenguaje Python, que permite a los usuarios analizar textos en español o inglés para saber si han sido generados por modelos de IA. Este programa combina diversas tenicas del procesamiento del lenguaje natural (NLP), incluyendo Transformers, embeddings y traducciónn automática, integradas en una interfaz gráfica interactiva hecha con el framework Vue.js

## Installation

Para ejecutar el proyecto, es necesario clonar el repositorio

```bash
  git clone https://github.com/UGachuzD/proyectoFinalALN.git
```

Posteriormente, abrir la carpeta desde un editor y desde terminal dirigirse a la carpeta de `Frontend`, una vez dentro de esta carpeta ejecutar el siguiente comando que instalará todas las dependencias necesarias para ejecutar la parte del Frontend de la aplicación

```bash
  npm install
```

Despues, dirigirse a la carpeta de `Backend` la cual si no se tiene instalado las librerias de: `flask`, `flask-cors`, `langdetect`, `torch`, `transformers` y `googletrans` no se podra ejecutar el programa de Python que contiene la lógica del Backend.

Para instalar estas librerias de Python, ejecutar el siguiente comando (En caso de usar Pip)

```bash
  pip install nombreLibreria
```

Finalmente, para levantar el servidor de Frontend basta con ejecutar el siguiente comando dentro de la carpeta de Frontend

```bash
  npm run dev
```

Y para el caso del Backend dirigirse a la carpeta de Backend para ejecutar el siguiente comando

```bash
  python main.py
```

Teniendo el Frontend y el Backend levantado, podemos dirigirnos a cualquier navegador y colocar la dirección correspondiente a LocalHost para poder ver la aplicación funcionando, la cual es

```bash
  http://localhost:3000/
```


