# Análisis de la importación y exportación de Venezuela en los últimos 20 años.

El proyecto se centrará en un análisis detallado y estructurado de las exportaciones e importaciones de Venezuela durante los últimas dos decadas. Su propósito principal es lograr una comprensión clara de las tendencias y patrones en el comercio, lo que facilitará una mejor toma de decisiones en la administración aduanera.

![ Presentacion de los datos ](https://github.com/TheAtticTrash/FAVFIX-proyecto/blob/master/proyecto.jpg)
[interfaz del proyecto](https://fafvix.streamlit.app)

> Proyecto.

## Tabla de contenidos

1. [Nombre](#análisis-de-la-importación-y-exportación-de-venezuela-en-los-últimos-20-años)
2. [Descripción](#descripción)
3. [Arquitectura](#arquitectura-del-proyecto)
4. [Proceso](#proceso-de-desarrollo)
5. [Funcionalidades](#funcionalidades-extra)
6. [Estado del proyecto](#estado-del-proyecto)
7. [Agradecimientos](#agradecimientos)


#### Arquitectura del proyecto.
``` el proyecto esta dividido en unas estructura sencilla, donde hay tres datasets principales, el archivo analisis.ipynb es el notebook de trabajo donde estudiamos el caso planteado en nuestro proyecto y el archivo interfaz.py es el encargado de dar vida y visualizacion a los datos en una interfaz web```

##### Proceso de desarrollo.

+ fuente donde se saco el dataset

    *  [The Observatory of Economic Complexity (OEC)](https://oec.world/es/profile/country/ven)
    * [Portal de Datos de Comercio Global de la OMC](https://globaltradedata.wto.org/official-data)

-Limpieza de datos 

![](https://github.com/TheAtticTrash/FAVFIX-proyecto/blob/master/arquitectura%20de%20la%20limpieza.jpg)

> Aquitectura de la limpieza de datos.

![](https://github.com/TheAtticTrash/FAVFIX-proyecto/blob/master/arquitectura%20basica%20de%20la%20limpieza.jpg)

![](https://github.com/TheAtticTrash/FAVFIX-proyecto/blob/master/resultado%20de%20la%20limpieza.jpg)

>Resultado de la limpieza

-Manejo excepciones/control errores

``` durante el proceso de procesamiento de los datos se determino que habian errores minimos en la fuente de informacion principal del proyecto, por lo tanto no se profundizo al respecto de estos aspectos ```

-Estadísticos (Valores, gráficos, …) ``` se utilizaron tres tipos de graficas durante el analisis visual de los datos, siendo las de barra las de mayor utilidad, y una de lineas para ver la caida y subida del valor por año, ademas de una grafica que utiliza una escala de colores para mostrar el grado de inversion en las 5 secciones con mayor inversion en cada año```

##### Funcionalidades extra.

* Desarrollo de interfaz gráfica de usuario

- Tecnología/Herramientas usadas
  - ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
  - ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
  - ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
  - ![Plotly](https://img.shields.io/badge/Plotly-3B4B8C?style=flat-square&logo=plotly&logoColor=white)
  
- Arquitectura de la interfaz
  ![](https://github.com/TheAtticTrash/FAVFIX-proyecto/blob/master/interfaz.jpg)

##### Estado Del Proyecto.

* Finalizado.

##### Agradecimientos

Queremos expresar nuestro más sincero agradecimiento a Samsung por la valiosa oportunidad de participar en el curso "Samsung Campus para Inteligencia Artificial". 
Este programa ha sido fundamental para nuestro equipo, FAVFIX, ya que nos ha proporcionado un conocimiento profundo sobre el funcionamiento de Python, el análisis de datos y el fascinante mundo de la programación.
Agradecemos especialmente a nuestros profesores, Jenny Remolina y Álvaro Arauz, por su dedicación, guía y asesoramiento a lo largo de este proceso de aprendizaje. Su apoyo ha sido crucial para nuestro desarrollo en el ámbito de la programación y el análisis de datos, y nos ha inspirado a seguir explorando y creciendo en este campo.
Este proyecto, que presenta un análisis del comercio en Venezuela desde 2002 hasta 2022, es un reflejo de los conocimientos adquiridos y de la pasión que hemos desarrollado por la inteligencia artificial y el análisis de datos.
Gracias nuevamente a todos los involucrados en este curso por su compromiso y por compartir su experiencia con nosotros.
