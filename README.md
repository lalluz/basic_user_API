# Description

This is a codechallenge I developed to build a basic user API using Python, Flask and Postgres.

## Installation

I developed the application in a virtualenv with Python 3.6.7 and the dependencies listed in requirements.txt.  

To run the application locally:  
    Create a Postgres database wih name 'codechallenge', user 'codechallenge' and password 'secret_passsword'. Grant all privileges to this user. [This tutorial](https://www.techrepublic.com/blog/diy-it-guy/diy-a-postgresql-database-server-setup-anyone-can-handle/) explains it really well.  
    Create a virtualenv in project root diretory:  
    `virtualenv -p python3.6 venv_name`  
    Activate it:  
    `. venv_name/bin/activate`  
    Install dependencies:  
    `pip install -r requirements.txt  `  
    Run the application at localhost:5000:  
    `python app.py`  
    Run tests:  
    `pytest` or `PYTHONPATH=. pytest`  
    To exit virtualenv:  
    `deactivate`  

## Architecture

The software is a simple Python Flask API to list, create, update and delete users.  
I chose to develop it using Flask just for familiarity with the tools. I considered Django, but Flask is lighter and I thought it would have been better for the purpose of this code challenge.  
I used Postgres as database.  
I deployed the application on AWS Lightsail using Apache2 as production server and Ubuntu 18.04 as OS.  

I handled the exceptions required and a pair of input validation just to give a sample.  

I added a pair of tests to test my date and email validation funcions. I didn't test the other funcions because it would have involved mocking, or other kinds of techniques, that at the moment it would have taken me too much time.  


### Application Url
http://35.180.23.105/users/getusers/  

Note: I chose not to go for the https scheme because I should own a domain, but I don't.  
I would have used Let's Encrypt via SSH with Certbot ACME to automatically generate and install the certificate with no downtime of my application.  

### Postman Link
https://www.getpostman.com/collections/c97cbc80f8e2223f69e7  

### GitHub Repo
https://github.com/lalluz/basic_user_API
