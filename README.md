Before installation, please make sure that at your computer already installed:

Python ver. >= 3.6 (project was created at ver == Python 3.6.8)

PostgreSQL ver. >= 10

INSTALLATION:

Create DB, Test DB and DB Owner

run in your terminal:

sudo -u postgres psql postgres

create user blog_api_admin with password 'blog_api_admin123';

alter role vasco_db_admin set client_encoding to 'utf8';

create database blog_api_db owner vasco_db_admin;

run in your virtualenv

pip3 install -r requirements.txt

please be sure that everything is installed successfully

in folder where located manage.py run:

python3 manage.py runserver

in case 8000 port are occupied run

python3 manage.py runserver [free port]

you can test this app online it runs on Heroku https://testblogapi.herokuapp.com

you can use created by me postman collections https://app.getpostman.com/join-team?invite_code=5f51e20c6d21d51cfc21c91c226da35b
