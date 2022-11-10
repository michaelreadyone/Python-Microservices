# [Python Microservices Web App ](<https://www.youtube.com/watch?v=0iB5IPoTDts>)

## steps not included in code:

- create a new django repo
- write Dockerfile for admin
- add requirements.txt to admin folder
- write docker-compose file for admin
- add mysql to docker-compose
- test mysql connection from dbeaver
- install products app `python manager.py startapp products`
- change admin settings 
  - add     
    'rest_framework',
    'corsheaders',
    'products'
    to INSTALLED_APPS
  - add 'corsheaders.middleware.CorsMiddleware' to MIDDLEWARE
  - config DATABSES to connect to mysql
  - add CORS_ORIGIN_ALLOW_ALL = True to last
- run server `docker-compose up`

--- 19:21 ---

- add models in products.models
- migrate db 
    ```bash 
    python manage.py makemigrations
    python manage.py migrate
    ```
- write serializer for products model
- write views for api
- write urls.py to register api, also regiester in admin/urls.py

--- 37:50 ---