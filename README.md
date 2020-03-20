# trekcheck

Trekcheck is a web application that allows users to organize maintain a centralized inventory of all of their outdoor gear and create individualized gear lists for specific camping trips. This is a Django web application built using Python and the Django ORM.

## Steps to get your project started:

* Clone down your team's repo and `cd` into it

* Create your OSX virtual environment in Terminal:

  * `python -m venv CapstoneEnv`
  * `source ./CapstoneEnv/bin/activate`

* Or create your Windows virtual environment in Command Line:

  * `python -m venv CapstoneEnv`
  * `source ./CapstoneEnv/Scripts/activate`

* Install the app's dependencies:

  * `pip install -r requirements.txt`

* Build your database from the existing models:

  * `python manage.py makemigrations capstoneapp`
  * `python manage.py migrate`

* Create a superuser for your local version of the app:

  * `python manage.py createsuperuser`

  
* Fire up your dev server and get to work!

  * `python manage.py runserver`


## ERD

https://dbdiagram.io/d/5e66ee034495b02c3b8804f9

Not that the column names do not conform to the Python community standards (PEP) for naming conventions. Make sure your models use snake case.

