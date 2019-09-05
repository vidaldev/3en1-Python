# :pencil: Reto 3en1

Este repositorio pertenece a un **reto** que consiste en construir la misma aplicación en 3 lenguajes diferentes. Los lenguajes elegidos fueron los siguientes

* Python [ [repositorio](https://github.com/vidaldev/3en1-Python) | [live](https://repl.it/@vidaldev/3en1-Python) ]
* NodeJS [ [repositorio](https://github.com/vidaldev/3en1-NodeJs) | [live](https://repl.it/@vidaldev/3en1-NodeJs) ]
* PHP [ [repositorio](https://github.com/vidaldev/3en1-PHP) ]

>La única regla es que el flujo de tareas y navegación que siguen los usuarios para completar las tareas sea el mismo en los 3 lenguajes. Puedes elegir los que más te gusten. Puedes seguir diferentes paradigmas, principios y buenas prácticas de programación. Pero la aplicación debe verse absolutamente igual en los 3 proyectos.

Link del reto [aqui](https://platzi.com/blog/platziretos-3-languages-challenge/)

## :trophy: Puesto clasificatorio

**3er lugar** :medal_military: ([resultados aquí](https://github.com/juandc/3-languages-challenge))

## 🚀 Comenzando

Tema principal es un **API REST CRUD** sobre alquiler de vehículos, todos los proyectos apuntan a una base de datos en **firebase**, tiene sistema a **AUTH**. En la introducción de este documento se ha explicado donde encontrar cada proyecto y donde puedes ver el proyecto funcionando perfectamente.

### 📋 Pre-requisitos

Para este proyecto se usaron las siguientes versiones con los siguientes modulos/plugins:

![python](https://img.shields.io/badge/python-3.6.8-blue?style=for-the-badge)

![pip3](https://img.shields.io/badge/pip3-9.0.1-blue?style=for-the-badge)

![ubuntu](https://img.shields.io/badge/Ubuntu_LTS-18.04.3-blue?style=for-the-badge)

El resto de los modulos que necesitaremos estan en `requirements.txt`. Espero no estar olvidando alguno, de ser así no te preocupes, al momento de la instalación te solicitará instalarlo.

Para saber la versión de tu python:

```bash
~$ python3 -V
Python 3.6.8
```

Para saber la versión de tu pip:

```bash
~$ pip3 -V
pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)
```

Para saber la version de tu linux:

```bash
~$ lsb_release -a

No LSB modules are available.
Distributor ID: Ubuntu
Description: Ubuntu 18.04.3 LTS
Release: 18.04
Codename: bionic
```

### 🔧 Instalación

Localizamos el directorio donde deseamos bajar este repositorio y ejecutamos lo siguiente:

```bash
~$ git clone git@github.com:vidaldev/3en1-Python.git
```

Puedes hacer un fork en caso de tu poseer una cuenta github (acepto mejoras de código). Luego de esto ingresa a la carpeta:

```bash
~$ cd 3en1-Python
/3en1-Python ~$ pip3 install -r requirements.txt
```

### 🛠️ Pruebas

Para correr las pruebas basta con situarse en el directorio del proyecto y ejecutar

```bash
~$ python3 main.py
```

### ⚙️ Uso / metodos / parametros

Para todos los request de manera obligatoria deben ir el correo y la contraseña

|               DESCRIPCION               |        URL       | METODO |                                             PARAMETROS                                            |
|:---------------------------------------:|:----------------:|:------:|:-------------------------------------------------------------------------------------------------:|
| Comprobar usuario                       | /login           |   GET  | email, password                                                                                   |
| Crear usuario                           | /createUser      |  POST  | email, password                                                                                   |
| Recuperar Clave                         |  /forgotPassword |  POST  | email                                                                                             |
| Abrir un alquiler                       | /alquilar        |  POST  | email, password, modelo, marca, year, color, responsable                                          |
| Cerrar un alquiler                      | /cerrarAlquiler  |  POST  | email, password, id (Del alquiler abierto), filtro (entregado)                                      |
| Corregir datos del alquiler             | /corregirDatos   |  POST  | email, password, id (Del alquiler), parametros a corregir (modelo, marca, year,color, responsable) |
| Listar todos los alquileres             | /alquileres      |  POST  | email, password, filtro (entregado, pendiente o todo)                                             |
| Listar todos los alquileres del usuario | /alquileres/user |  POST  | email, password, filtro (entregado, pendiente o todo)                                             |

### ✔️ Para recordar

No olvides configurar el archivo `config/config.py` y descargar el `config/ServiceAccountKey.json` de tu cuenta **firebase**

---
