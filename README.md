Functionality of project:-
    Create a user,
    Get all users,
    Create a client,
    Get all clients,
    Get client by ID,
    Update client by ID,
    Delete client by ID,
    Create project,
    Get all projects

APIS in the project

    POST API - To Create a new User
    http://127.0.0.1:8000/api/user/create/

    Get API - To get all Users
    http://127.0.0.1:8000/api/user/list/

    POST API - To Create a new client
    http://127.0.0.1:8000/api/client/create/

    Get API - To get all clients
    http://127.0.0.1:8000/api/client/list/

    Get Api - To get info of client by ID
    http://127.0.0.1:8000/api/client/id/

    Put/Patch API - To update Info of Client by ID
    http://127.0.0.1:8000/api/client/id/

    Delete API - To delete Client by ID
    http://127.0.0.1:8000/api/client/id/

    POST API - To Create a new project
    http://127.0.0.1:8000/api/project/create/

    Get API - To get all projects
    http://127.0.0.1:8000/api/project/list/


Instruction for how to run app locally:- 
1. Connect the database: 
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'Task',      #Database name
                    'USER': 'root',
                    'PASSWORD': '####',   #password
                    'HOST': '127.0.0.1', 
                    'PORT': '3306', 
                }
            }


2. After connecting the database run following commands:
        python manage.py makemigrations  - This command is used to create migration files.
        python manage.py migrate  -  To apply the migrations to the Database
        python manage.py runserver  - To run the Django server



