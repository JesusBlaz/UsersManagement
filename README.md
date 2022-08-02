# UsersManagement
Prueba técnica para la administración de usuarios.
~~~~
Instalación del proyecto:

1.- Clonar el repositorio desde GitHub.
2.- Crear entorno virtual para la instalación de los requerimientos.
3.- Correr el entorno virtual
4.- Desde la terminal y con el entorno virtual activo, entrar a la carpeta 
del proyecto, UsersManagement, a la altura del README.md
5.- Hacer un pip install -r requirements/local.txt para instalar todas las
dependencias del proyecto.
6.- Posterior a ello, entramos a la carpeta UsersManagement/UsersManagement a la altura del 
archivo manage.py, desde la terminal.
7.- Una vez dentro de esta carpeta, creamos un superusuario con el comando python manage.py createsuperuser.
8.- Después de crear el super usuario hacer un python manage.py runserver para activar el servidor.
8 .- Listo, nuestro servidor esta corriendo y podemos acceder a los endpoint con el superusuario que has creado.

Dentro del proyecto, existe una documentación para ver los endpoint del proyecto.
Para acceder a ella, es con la siguiente ruta:
http://127.0.0.1:8000/docs/
o también con:
http://127.0.0.1:8000/redocs/
