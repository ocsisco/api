

#### La API consume y depagina los resultados de una consulta de los delincuentes buscados por el FBI.

Existen cuatro funcionalidades:

- **La primera funcionalidad**, con el path "/search-with-parameters/<search_parameters>" donde "<search_parameters>" son todos los parámetros que admite la API a la que se consulta, por ejemplo:
"/search/eyes=brown","/search/eyes=brown&sex=female"... (la documentación de la API no incluye cuantos parámetros ni que parámetros son consultables).
Debido a que las fichas tienen demasiados datos y la mayoría de ellos son campos irrelevantes o declarados nulos los resultados son depaginados y solo se retorna un json con el nombre y el ID de la ficha.


- **La segunda funcionalidad** con el path "search-any/<any>" donde "<any> son todas las palabras que la ficha buscada debe incluir, por ejemplo:
"/search-any/male+danger+young"...
Sirve para buscar por cualquier palabra, ya que la documentación de la API consumida no provee de que parámetros son consultables, puede que se necesite consultar algúna key o value del json que no esta contemplada como parámetro así como cualquier parte de un string, de ese modo se puede buscar aún sin conocer los parámetros consultables.
  

- **La tercera funcionalidad**  con el path "search-any-with-parameters/<search_parameters>/<any>" donde "<search_parameters>" son los parámetros consultables a ingresar y "<any>" son aquellas palabras que las fichas devueltas por una consulta de parámetros válidos contendrán en su interior, por ejemplo: "/search-any-with-parameters/sex=female&hair=blond/girls+young+blue jeans"
  
Esta funcionalidad es una combinación las dos anteriores, surge de la necesidad de que en la segunda funcionalidad, no se busca con parámetros consultables de modo que el programa busca en todas las fichas existentes y de entre los resultados se busca cuales contienen las palabras deseadas, ello consume recursos y tiempo, además, palabras como "female" no necesariamente tienen que ser atributos del delincuente, puede que sea una palabra en la descripción del delito, de modo que si se conoce algún atributo correspondiente a un parámetro consultable, es conveniente ingresarlo para que el resultado sea mas preciso y tambien sea mejor el rendimiento de la aplicación, a su vez, combina con la busqueda por palabras de la segunda funcionalidad.
  
- **La ultima funcionalidad**, con el path "view-file-by-id/<id>" donde "<id>" es la "id" obtenida de las funcionalidades anteriores si nos devuelve la ficha entera para poder consultar al detalle, esta funcionalidad admite ingresar varias id, por ejemplo: /view-file-by-id/85eb0ac4ec594555870da8246fcc01c4+8789e8f4116633bd872efd3b514ecd0b.
 

Todas las funcionalidades funcionan mediante peticiones GET de forma asincrona debido a que, por ejemplo en la segunda función, al no tener un filtrado previo mediante parámetros, la API necesita leer entre todas las fichas existentes, son 1040 fichas paginadas en 52 páginas, hacer 52 GET de forma sincrona demoraría mucho tiempo. En la primera función tambien existe la posibilidad de ingresar parámetros comunes como el sexo del individuo, que también arrojaría una gran cantidad de páginas.
