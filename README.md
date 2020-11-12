# simple-api

Simplae api for creating, updating, deleting posts.


### Install virtual env
pip3 install virtualenv
virtualenv env
source env/bin/activate
cd simple_api/

# Apply and create DB
python3 manage.py makemigrations simple_api
python3 manage.py migrate

# You have to create user to be able to make posts
###python3 manage.py createsuperuser

# Install requirements
pip3 install -r requirements.txt

# Run app
python3 manage.py runserver



### DEPLOY
sudo snap install --classic heroku
heroku login
heroku ps:scale web=1

heroku git:remote -a simple-api-07

heroku buildpacks:set heroku/python

heroku local

git add .
git commit -m"static"
git push heroku HEAD:master

# Test app is runable
cd simple_api/
gunicorn simple_api.wsgi
