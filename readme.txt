This is a service sharing platform developed using python with django framework.

Currently this is just a prototype that allows users to :
    register            via     /accounts/register
    login               via     /accounts/login
    logout              via     /accounts/logout
    post a task         via     /postTask
    find a task         via     /findTask

    this service lets users apply to tasks by sending a notification with the candidate's contact
    information to the task owner via SMS (using Tritux's API)


Also this prototype allows users to list the jobs at each city by using the api:
    /api/city/city_name     e.g.        /api/city/sousse