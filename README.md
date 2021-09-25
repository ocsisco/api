# api

La API consume y depagina los resultados de una consulta de delincuentes buscados en la API del FBI.

Existen tres funciones, la primera "/search/<parametros>" admite todos los parámetros que admite la API a la que se consulta, por ejemplo:
"/search/eyes=brown","/search/eyes=brown&sex=female"
Los resultados son depaginados y solo se retorna un json con el nombre y el ID de la ficha.


La segunda función, sirve para buscar por cualquier palabra, ya que la documentación de la API consumida no provee de que parámetros son
válidos, puede que ingresemos uno no existente, o simplemente busquemos algúna key o valor del json que no esta contemplada como parámetro y no es consultable,
de ese modo se puede buscar aún sin conocer los parámetros admitidos, o aunque no sean parámetros y sean palabras que existan en una descripción como por ejemplo
"bomb" o "drugs" de manera que aunque no sean parámetros arroje los resultados de las fichas policiales en las que se incluyen esas palabras por ejemplo: "/search-any/guy", "/search-any/guy drugs male".


La tercera función es una combinación de ambas, surge de la necesidad de que en la segunda función, no se busca con parámetros admitidos de modo que tiene que buscar entre todas las fichas y de entre 
los resultados se busca cuales contienen las palabras deseadas, ejemplo: "/search-any-with-parameters/sex=male&hair=black/young drugs murder".

Las tres funciones emiten GET de forma asincrona debido a que, por ejemplo en la segunda función, al no tener un filtrado previo mediante parámetros, la API consumida nos
devuelve todos los sospechosos, 1040 elementos paginados en 52 páginas, hacer 52 GET de forma sincrona demoraría mucho tiempo.

La tercera función combina la velocidad de la primera función ya que solo se devuelven resultados con los parámetros indicados con la versatilidad de la segunda 
funcionalidad de buscar entre todos los resultados.
