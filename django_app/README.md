# Django app crud operations

## Django architecture

Django follows MVT architecture
- Model - controls the connection and data manipulations with DB
- View - user request handler(the controller as of mvc)
- Template - the webview which is the html page

## Steps for setting up django app

- Create project
    - run command ``` django-admin startproject <my_proj> ```
    - can validate django is properly running with command ```python manage.py runserver```
- Create app
    - run command ``` manage.py startapp <app_name> ```
- Create a ```url.py``` in same folder as of ```views.py``` and add the route forwarding url
- Add the above url to urlpatterns in the ```url.py``` file in root folder
- Create a ```templates``` folder in app folder and add the html page
- Update ```settings.py```
- run command ```python manage.py migrate```
- Run ```python manage.py runserver``` and goto localhost:8000/<url path> , command will direct to html page
