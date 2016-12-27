##Overview
This is a sharing platform that connects people in need of a specific skill with people who
possess that skill and are ready to offer it for a fee.
The platform is developed using python with django framework.

### Video Demo
[![Video](http://img.youtube.com/vi/nyQBVXAxopk/0.jpg)](https://www.youtube.com/watch?v=nyQBVXAxopk "sharing platform")

##Dependencies
django, django-registration, jsonpickle

to install them, run in the terminal/cmd:

>pip install django
>pip install django-registration
>pip install jsonpickle

##Running

to run the project you have to run the following commands in the terminal/cmd:
>cd path/to/project/root
>python manage.py runserver


##Details

Currently this is a prototype that allows users to :
    register            via     /accounts/register
    login               via     /accounts/login
    logout              via     /accounts/logout
    post a task         via     /postTask
    find a task         via     /findTask

    this service also lets users apply to tasks by immediately sending a notification with the candidate's contact
    information to the task owner via SMS (using Tritux's API)


Also, for data collection purposes, this prototype allows users to list some valuable information
in JSON format by using the api:

    get the list of jobs in a specific city         via         /api/city/city_name

    e.g.   GET     /api/city/sousse

    -->
    [{
        "skills": "painting",
        "description": "paint the walls of a small house",
        "region": "sahloul",
        "title": "Paint the walls"
    }, {
        "skills": "cleaning",
        "description": "clean the garden",
        "region": "khzema",
        "title": "clean the garden"
    }]


##TO DO

Integrate the UI with the backend.
The UI templates are already available as standalone html, css and js files.
