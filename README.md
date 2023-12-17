# recipe-app

Web-application built with Python using the Django framework. 

## How to get the project running

*Note: You will need to work in a virtual environment with Django installed*

### If you have not yet created a virtual environment on your machine:

- To create a virtual environment you will need to install virtualenvwrapper `pip install virtualenvwrapper`
- Once installed run `mkvirtualenc test-environment`
- Then run `workon test-environment` to load the installed environment
- Finally, run `pip install django` or `py -m pip install Django` to install Django in the environment

### Once in you virtual environment:

- Navigate to root folder in terminal
- Run the following: `python manange.py runserver`
- In browser, navigate to http://127.0.0.1:8000/

### You will be prompted to login, user the following credentials:

- Username: DemoUser
- Password: DemoPassword

## Features

- Admin panel capable of preforming CRUD operations on database (can be accessed by going to `/admin` URL and logging in with same credentials as above)

Users are able to do the following:
- View all recipes in list
- Click on any recipe to view it's details
- Create new recipes by entering custom information
- Search recipes by sorting based upon difficulty, filtered results returned in the form of different charts
