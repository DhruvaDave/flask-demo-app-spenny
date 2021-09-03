
`Spenny-app`
--------------

 Contents
----------------
 * Project Setup
 * Project Structure

## Project Setup
---------------
- Setup
` git clone https://github.com/DhruvaDave/flask-demo-app-spenny.git`
` pip3 install -r requirements.txt`
- Run project
    * Run app
        ` python3 run.py` 

    ###### Which will run project on 4500 Port


### Unit testing
- A unit test is a way of testing a unit - the smallest piece of code that can be logically isolated in a system. A unit can be almost anything you want it to be -- a line of code, a method, or a class.
- Pytest is a testing framework based on python. It is mainly used to write API test cases.
- To run tests use below command.
` pytest -vvv `
- Test coverage is defined as a technique which determines whether our test cases are actually covering the application code and how much code is exercised when we run those test cases. To run coverage run below command.
    ###### Report without missing lines:
    ` pytest --cov-report term --cov=spenny_app `
    
    ###### Report with missing lines:
    ` pytest --cov-report term-missing --cov=spenny_app `
    
    ###### HTML Report generation:
    ` pytest --cov-report html:cov_html --cov=spenny_app `

    ###### Note:
    The path for the html report file will be main-console/cov_html/index.html."cov_html" is the folder


### Env variable 
|Variable Name                         |Description                                                                  |Default value                               |Optional Value|
|--------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------|--------------|
|DB_HOST                               | Database Host name                                                          |                                            |              |
|DB_USER                               | Database User name                                                          |                                            |              |
|DB_PASSWORD                           | Database password for specific user                                         |                                            |              |
|DB_PORT                               | Database port to connect                                                    |3306                                        |              |
|DB_NAME                               | Database name (required                                                     |                                            |              |
|DB_POOLSIZE                           | database pool size                                                          |5                                           |              |
|DB_ENABLE_SSL                         | True if SSL certificate is used by Database                                 |False                                       |              |
|APP_PORT                 |4500 #Port on which main-console flask app will run                          |4500                                        |              |
|APP_DEBUG                |False #main-console Flask app debug mode                                     |False                                       |              |
|FERNET_KEY                            | An Alphanumeric Fernet string that is used to encrypt and decrypt MFA secret| k-1k6diILafCUt63-IooJplOybLy1i_hsft4gzXvt_Q|              |
|WTF_CSRF_ENABLED                      | False (To ignore CORS errors)                                                |                                            |              |
|FLASK_APP_SECRET_KEY                  | Flask app secret key to manage sessions                                     |                                            |              |
|TEMPORARY_JWT_EXP_TIME_MINS           | Lifetime of temporary JWT token that is generated during signup and login   |60                                          |              |
|JWT_EXP_TIME_MINS                     | JWT token that is stored in session                                         |120                                         |              |



##### File Description
- __init__.py: Flask wsgi application instance
- repository: Python classes allowing you to interact with your models
- services: Python classes to write application logic using repository
- models: Python classes modeling the database
- config: Related to configuration of services like mysql
- common: common modules used across project
- exceptions: custom exceptions defined for application
- utils: Utility scripts
- requirements.txt: python package dependency
- run.py: main entry point of application to start server