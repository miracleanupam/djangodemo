# Simple Django App

## Setup
There are two ways to run the application.

### 1. Cloning the repository
- Clone the repo
- Enter the corresponding credentials for `MySQL` database
- Run the following commands
    ```
    python manage.py migrate
    python manage.py init_users
    python manage.py createsuperuser
    python manage.py runserver 0.0.0.0:8000
    ```
- Enter 0.0.0.0:8000 on a browser
  
### 2. With `docker-compose`
- Clone the repo
- Run the following command
    ```
    docker-compose up
    ```
- Enter 0.0.0.0:8000 on a browser

## About the app
For the purposes, it is assumed that you have opted for the docker-compose solution for setup. Then a superuser and a 
normal user account will have been created be default.

Credentials for superuser:

username: admin
password: nimda

Credentials for normal user:

username: testuser
password: testtest

When you go to the homepage of the app, you'll see a blank screen. That's because, there are no products added by the
superuser so far.

1. Login with the superuser credentials
2. Go to the `0.0.0.0:8000/add-product` and add some products
3. Now go to homepage

A normal use can be used to test the functionality of the app.

## Demo
[Demo of this site can be found here](https://djangodemoanupam.herokuapp.com/)