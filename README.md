# <u>**PROYECTO: Gestor de videogames**</u>

## **<u>Introducción</u>**

Este es un proyecto propio que hice en base de un ejercicio integrador que teniamos en la universidad, el cual consistia en realizar una API sobre videogames. Una vez finalizada la cursada, por mi cuenta, decidi llevar lo que habiamos aprendido hacia el front y este es mi resultado. Aún me faltan corregir muchas cosas, y algunos errores como tambien agregar una base de datos relacional. Mi objetivo con este proyecto es hacer una app al estilo myanimelist.net pero con un enfoque sobre videogames, el cual tambien incluya un foro para intercambio de ideas entre usuarios.


## <u>Tecnologías utilizadas:</u>
1. Python
2. Flask
3. Javascript
3. Html
4. Bootstrap

## <u>Instalación del proyecto</u>

Aqui los comandos a colocar en consola para inicializar el proyecto:</br>
1. `git clone https://github.com/NACXIIX/Gestor-de-videogames.git`
2. `python -m .venv venv`
3. `.venv/Scripts/activate en Windows`
`source .venv/bin/activate en Linux/Mac` 
4. `pip install Flask passlib`
5. `python app.py`

## <u>Uso</u>

1. Abra su navegador, ingrese a: http://127.0.0.1:8000
2. Se le va a redirigir a la pagina de inicion de sesión.
3. Colocar los datos predeterminados, user para el usuario y admin para la contraseña(estos estan encriptados mediante el hash de passlib).
4. Una vez dentro se podra visualizar una navbar en la parte superior, en 'all games' estaran todos los juegos que se hayan cargado.
5. En la parte de 'add game' es donde habrá un formulario para completar los campos requeridos y agregar el videogame que usted desee.
6. En la parte de 'update game' es donde se actualizará mediante un ID el juego que usted desee.
7. En la parte de 'delete game' es donde se eliminará mediante un ID el juego que usted desee.
8. En la parte superior izquierda se encuentra el boton 'salir' el cual lleva a la ruta '/logout' el cual desloguea al usuario.

## <u>ACLARACIONES</u>

En cada card que contiene la información de los videogames, hay un boton de 'Update', este botón por el momento no tiene utilidad, en un futuro cercano se agregara otro boton 'Delete' y con ellos se realizará el manejo de PUT y DELETE del backend.