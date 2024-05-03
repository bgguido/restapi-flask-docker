La rest-api maneja los sabores y las opciones de una heladeria ficticia

Las opciones se encuentran en http://localhost:5000/opciones
por lo que si quiero saber qué opciones hay tengo que hacer

curl http://localhost:5000/opciones


Para ver que sabores hay

curl http://localhost:5000/sabores

Para agregar sabores hacer lo siguiente, le asigna ID automaticamente fijandose cual está libre

curl -X POST -H "Content-Type: application/json" -d '{"sabor": "pochoclo"}' http://localhost:5000/gustos

Para eliminar un sabor con su id correspondiente, luego de eliminarlo ordena los números para que queden en orden

curl -X DELETE http://localhost:5000/gustos/2
