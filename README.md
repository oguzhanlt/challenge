# Skelton for building Online-Challenges


This project can be used as a starting point to build new Online-Challenges. It uses Django as a backend server 
and Bootstrap v4 is used to build appealing UIs.

Please evaluate at the beginning of the project if a backend is needed at all. 
If the project is limited to a simple web page, without input validation on the server side, 
then better use [Jekyll](https://jekyllrb.com/docs/) to build the challenge page.

### How to modify

The [challenge_skelton](./challenge_skelton) directory is the main folder. Here, project-wide changes can be made.
For most of the Challenge, nothing needs to be changed in this folder unless you want to add new apps.

The [static](./static) folder contains only static files, e.g. images, Javascript files or CSS files.
It also contains all used Javascript libraries, which are listed at the bottom of this page.

In the [web](./web) folder you will have to make most of the changes. 
You will find a folder called "templates". There you will find all html files that will be displayed later.
The [base.html](./web/templates/base.html) file serves, as the name suggests, as a basic framework for further files. 
It includes the header and footer and all required CSS and Javascript files.
In the middle there is a content block, which is replaced by the inheriting template. 
If the [index.html](./web/templates/index.html) file now inherits from the base.html, then the content of the base file 
can be easily set there and you do not have to write everything again for each page.

New paths can be added by inserting them into the [urls.py](./web/urls.py) file inside the web folder.
Now just add the path logic to the [views.py](./web/views.py) file inside the web folder.


### How to start the project

##### testing locally / building the challenge

When building the challenge use the built-in django server by executing the following commands:
```bash
# create db - must be executed only once 
python manage.py migrate
python manage.py runserver
```

Now visit `localhost:8000` in your browser and you should see the website.


##### deployment

DO NOT USE THE BUILT-IN DJANGO SERVER!

We use gunicorn to host the django application and nginx to serve the static files. 
To simplify the whole thing we use docker. 
This way we can start the project with one command in any environment.

To host the challenge first make the following changes:

1. Set DEBUG to false in [settings.py](./challenge_skelton/settings.py)
2. Set ALLOWED_HOST variable in [settings.py](./challenge_skelton/settings.py)
3. Set <service_name> and <container_name> in [docker-compose.yml](./docker-compose.yml)

Now run the project on the server with:

```bash
docker-compose up --build -d
```

### Which port to use

We agreed on using ports in the range of *10.000 - 10.999* for workshop challenges and
ports in the range of *11.000 - 11.999* for online challenges.
Whenever possible, please stick to those ports.


### Used libraries

- [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/) as a frontend UI framework
- [jQuery](https://api.jquery.com/) bootstrap dependency
- [SweetAlert2](https://sweetalert2.github.io/) for simple modals 
