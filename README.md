# djangorestfull_autentication_authorization
Proyecto de Django REST FULL con autoticación y autorización

```
git init
git add .
git commit -m "Primer commit"

git remote add origin <URL_del_repositorio>

git push -u origin master o main

```

## Evidencia e como utilizar el control registro de usuario

Con el siguiente comando se obtiene el token del usuario yasser creado anteriormente
```
curl -X POST http://localhost:8000/api/auth/login/ -H "Content-Type: application/json" -d '{"username": "yasser", "password": "yasser"}'
```
Para utilizar un endpoint utilizando la autenticación se pone en la cabecera de la petición, el token obtenido anteriormente de la siguiente manera de hace la solicitud a un endpoint protegido con autenticacion
```
 curl -X GET http://localhost:8000/api/articulos/ \
-H "Authorization: Token 00b12892cac091ada9c3debe68ec058961d926c5"
```