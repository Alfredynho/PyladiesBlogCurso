## Web Site Django

**Project Django BlogApp ** Web Site con Django INCOS
### Tecnologías
    Django
    Virtualenv 
    Python
    Linux
    Postgresql

# DJBlog
![alt text](https://res.cloudinary.com/due8e2c3a/image/upload/v1534597296/INCOSDev/DeepinScreenshot_20180818090001.png)

![alt text](https://res.cloudinary.com/due8e2c3a/image/upload/v1534597294/INCOSDev/DeepinScreenshot_select-area_20180818090040.png)

# virtualenv

  - `virtualenv -p python3 env`
  - `source env/bin/activate`
  - `pip install Django`

# Crear Base de Datos en postgres

  - `sudo su postgres`
  - `psql -c "DROP DATABASE blogapp"`
  - `psql -c "DROP USER bloguser"`
  - `psql -c "CREATE USER bloguser WITH ENCRYPTED PASSWORD '122333'"`
  - `psql -c "CREATE DATABASE blogapp WITH OWNER bloguser"`
  

# Base de Datos Sqlite3
  El proyecto se encuentra por defecto configurado para ser ejecutado con sqlite3
  
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

[@alfredynho](alfredynho.cg@gmail.com).
[@alfredynho Telegram](@alfredynho).