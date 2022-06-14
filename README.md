# Tarea1
Tarea Scrapy

Descripcion:
Scrapy a listado de links de Wikipedia que van asociados a articulos de contenido variado asociados a arquitectura, arqueología y arte, coloconadole un limite de 25 links.
estan clasificados en una unica categoria en la cual se extrae el titulo del articulo y el primer parrafo del mismo.


Contribuciones:
Jorge Cardona: Generacion de código , identificación de estructura de página
Celmy Rojas:Generacion de código , funcion de callback para llamar  a cada link
Marvin Gutierrez: Generacion de código, generación de archivo csv
Marlon Fuentes: Generacion de código,documentación y almacenamiento de la información ( YIELD)


Información Adicional:
El objetivo principal es recopilar el titulo y primer párrafo de cada artículo, se notó que la mayoria de veces estos parrafos terminan en punto (.) o espacion en blanco. Por lo que se utilizaron esos caracteres como caracteres de corte de línea y en caso los parrafos no terminaran en esas 2 condiciones se optó por cortar el scrapping a los 25 caracteres recopilados.


1. conda create -n environment_tarea1 

2. conda activate environment_tarea1

2. conda activate scrapping conda install scrapy -c conda-forge

4. scrapy startproject tripadvisor


Ejecutar este comando para generar csv con información de :
* titulo: titulo de cada link
* parrafo: primer parrafo de cada link

5. scrapy runspider article.py  -o data.csv



PARA EJECUCIÓN:

1. abrir un  pompt
2. colocarse en la ruta de la carpeta spider
3. ejecutar el siguiente comando para que corra: scrapy runspider article.py  -o data.csv
