# Proyecto_TopicosHPC
Project about parallel programming.
#### ¿Cómo ejecutar los programas?
1. Serial
*Si se quiere ejecutar el programa en serial se debe poner la siguiente línea, <python2.7 serialProject.py ./(Carpeta donde se encuentran los documentos)/*
2. Paralelo
*Si se quiere ejecutar el programa en paralelo se debe poner la siguiente línea, <mpiexec -np (número de nucleos) python2.7 parallelProject.py ./(Carpeta donde se encuentran los documentos)/*
# 1. Realizado por:
1. Mateo Hincapié Zapata - mhinca20@eafit.edu.co
2. Marcos David Sierra Gallego - msierr37@eafit.edu.co
### Estudiantes de la Universidad EAFIT
# 2. Introducción:
*En éste repositorio se encuentran dos programas (uno en serial y otro en paralelo) que sirven para encontrar la similitud que existe entre documentos, basicamente utiliza dos algoritmos principales, Jaccard y Kmeans (que serán explicados a continuación), con los cuales agrupamos en diferentes clusters los documentos que más se parecen debido a una serie de palabras relevantes.
El dataset se obtuvo de Gutenberg por medio del siguiente link, https://goo.gl/LL4CgA, en este dataset se encuentran al rededor de 3000 documentos con los cuáles se pueden correr los programas.*
# 3. Palabras clave:
*Una de las palabras clave es la lista 'stopwords' que contiene una serie de palabras que deben ser eliminadas de cada documento leído ya que pueden ser redundantes y sin importancia por ser tan comunes en un texto.*
# 4. Análisis y Diseño de algoritmos:
*Para empezar con los programas se decidió gracias a la lectura de varios papers, escoger una cantidad 10 términos de cada documento para poder hacer la comparación entre ellos, entonces lo que se hace es que después de eliminar las 'stopwords' se buscan las 10 palabras más usadas en los documentos, estas palabras se ingresan en una lista que posteriormente será utilizada por el Jaccard para encontrar la similitud de los documentos, cuando obtenemos esta similitud también obtenemos la distancia entre archivos y esto lo ingresamos en una matriz que será procesada por el Kmeans donde finalmente agruparemos los documentos con sus respectivos centroides.
Los algoritmos que se utilizaron fueron Jaccard para obtener las distancias entre los documentos y KMeans para agrupar los documentos en sus respectivos centros*
#### Jaccard:
*El índice de Jaccard ( IJ ) o coeficiente de Jaccard ( IJ ) mide el grado de similitud entre dos conjuntos, sea cual sea el tipo de elementos.

La formulación es la siguiente:

J(A,B) = |A ∩ B| / |A ∪ B|*
*Éste algoritmo se obtuvo de la siguiente página donde se explicaba de muy buena manera su funcionamiento,
http://dataconomy.com/2015/04/implementing-the-five-most-popular-similarity-measures-in-python/*
#### KMeans:
*K-means es un método de agrupamiento, que tiene como objetivo la partición de un conjunto de n observaciones en k grupos en el que cada observación pertenece al grupo cuyo valor medio es más cercano. Es un método utilizado en minería de datos. El código para el Kmeans se obtuvo de varios links y repositorios de dónde se trató de entender su funcionamiento y gracias a los cuáles se pudo realizar el KMeans que se encuentra en los programas realizados.*
# 5. Análisis de solución:
*Al correr los dos programas, cada uno con una cantidad de 100 documentos se observaron los siguientes aspectos*
![Comando HTOP corriendo el programa en serial](/imagenes/htopSerial.jpg)
![Tiempo de ejecución del programa en serial](/imagenes/serialTime.jpg)
![Comando HTOP corriendo el programa en paralelo](/imagenes/htopParallel.jpg)
![Tiempo de ejecución del programa en paralelo](/imagenes/parallelTime.jpg)
# 6.Bibliografía:
http://dataconomy.com/2015/04/implementing-the-five-most-popular-similarity-measures-in-python/
https://es.wikipedia.org/wiki/K-means
https://es.wikipedia.org/wiki/%C3%8Dndice_Jaccard
https://goo.gl/LL4CgA
