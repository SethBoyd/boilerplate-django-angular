#boilerplate-django-angular
##Intro

This boilerplate is created to make it easier to start working with Django-rest-framework and AngularJS.  This project is ready to use out of the box.  By using /api in your app's urls.py, it is configured to work at port 8000 for the Django server and port 9000 for the Grunt server running the Angular app.  CORs for Django and headers for AngularJS are already configured.  Looking in settings.py and GruntFile.JS, there are comments to indicate where to edit in order to change port numbers or the default api path for REST endpoints.  Hope this makes it easier for you to start your next django-rest-framework and AngularJS project.  As always, it is recommended that you work in a new virtual environment.  This project is tested on Python 2.7, with Django 1.7.7 and AngularJS 1.3.

##QuickStart

### Install Node and update npm.

Follow the instructions from npmjs.com below:

[https://docs.npmjs.com/getting-started/installing-node](https://docs.npmjs.com/getting-started/installing-node)

### Install Bower

`sudo npm install -g bower`

### Install Grunt command line tool.

`sudo npm install -g grunt-cli`

More detailed instructions here: [http://gruntjs.com/getting-started](http://gruntjs.com/getting-started).

### Install Django packages

`cd yourpath/boilerplate_django_angular/`

`pip install -r requirements.txt`

This will install all required packages for Django.  Main ones are Django 1.7.7, django-rest-framework and django-cors.

### Install Grunt dependencies

`cd to yourpath/boilerplate_django_angular/static`

`sudo npm install`

### Install Bower Packages

Stay in directory yourpath/boilerplate_django_angular/static

`bower install`

This will install all of AngularJS's dependencies.

### Install Grunt-connect-proxy

`sudo npm install grunt-connect-proxy --save-dev`

### Patch grunt-connect-proxy

`sudo npm install eventemitter3@0.1.6`

### Create SQLite database
`cd yourpath/boilerplate_django_angular/`

`./manage.py migrate`

### Start Django server
`./manage.py runserver`

### Start Grunt server
Open a new terminal.

`cd yourpath/boilerplate_django_angular/static`

`grunt serve`

This will automatically launch your default browser and point to localhost:9000/.  If everything works, you should see the message:

> "API call works!  Let's do this!".

Otherwise you will see this instead:

> "API call did not work, did you start the server?"
