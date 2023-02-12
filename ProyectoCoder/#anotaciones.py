# Crear un nuevo proyecto

"""
C:\coder\Clase17-Django>django-admin startproject ProyectoCoder

"""

#Crear un entorno virtual dentro de esa carpeta

"""
C:\coder\Clase17-Django\ProyectoCoder>virtualenv venv

"""

#Inicializar la app

"""
C:\coder\Clase17-Django\ProyectoCoder>python manage.py startapp AppCoder

"""

#Agregar la App a INSTALLED_APPS en settings.py 

"""
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'AppCoder.apps.AppcoderConfig',
]

"""

# Checkear que AppCoder esta bien o por lo menos su estructura

"""
(venv) C:\coder\Clase17-Django\ProyectoCoder>python manage.py check AppCoder

"""

#Agregar información a la BD

"""
(venv) C:\coder\Clase17-Django\ProyectoCoder>python manage.py shell 

#Se crea una consola interactiva

>>> from AppCoder.models import Curso

>>> curso = Curso(nombre='Python', camada=48265) 

>>> curso.save()

"""

# Dentro de la carpeta donde esta el primer ProyectoCoder crear una que sea versionGit

# Dentro de esa carpeta abrir un Git Bash

# Clonar un repo, para conectar el proyecto local con el repositorio

"""
$ git clone https://github.com/swmartinez/ProyectoCoder.git

"""

# Copiar todos los archivos de ProyectoCoder y pegarlos dentro de versionGit


###########################################################################

## Ctrl + Shift sobre una carpeta para abrir cmd ahí

###########################################################################

# Crear un entorno virtual

"""
C:\coder\versionGit\ProyectoCoder>virtualenv venv

C:\coder\versionGit\ProyectoCoder>venv\Scripts\activate

"""

#Instalar django

"""
(venv) c:\coder\Clase17-Django\ProyectoCoder>pip install django

"""