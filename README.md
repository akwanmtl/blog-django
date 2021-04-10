# Blog-Django

## Description
The simple blog application is built using Django and Python as the backend server. It also uses Materialize as the CSS framework. It is deployed on Heroku.
This application allows you to add a new post, edit existing posts and delete posts.

Link to the Github repository: https://github.com/akwanmtl/blog-django

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Credits](#credits)
* [License](#license)

## Installation

You would need to have Python and Virtualenv already installed on your computer. To run application locally, first clone the repository.
```
$ git clone https://github.com/akwanmtl/blog-django.git
```
Create a virtual environment to install dependencies in and activate it:
```
$ python -m virtualenv env
$ source env/bin/activate
```
Then install the dependencies:
```
(env)$ pip install -r requirements.txt
```
Once pip has finished downloading the dependencies go to the app folder
```
(env)$ cd app
```

## Usage 

To run the application, use the following command:
```
(env)$ python manage.py runserver
```
You can add a new post by clicking on the Add Post. By clicking on Edit Posts, you see edit and delete button next to each post. 


[![Demo Website](Blog.gif)] 

## Credits

* [Materialize](https://materializecss.com/)
* [Django and Static Assets](https://devcenter.heroku.com/articles/django-assets)
* [How To Deploy Django App on Heroku](https://www.codementor.io/@jamesezechukwu/how-to-deploy-django-app-on-heroku-dtsee04d4)
* [License badge link](https://gist.github.com/lukas-h/2a5d00690736b4c3a7ba)


## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Copyright (c) [2020] [Annie Kwan]
