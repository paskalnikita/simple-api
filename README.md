# simple-api
Simple api for creating, updating, deleting posts.https://simple-api-07.herokuapp.com/
User **admin:admin** alredy exists. You can login with this credentials for making posts.

### Install virtual env
pip3 install virtualenv

virtualenv env

source env/bin/activate


# Install requirements
pip install -r requirements.txt

# Apply and create DB
python3 manage.py makemigrations simple_api

python3 manage.py migrate


# You have to create new user to be able to make extra posts
python3 manage.py createsuperuser

# Run app
python3 manage.py runserver



### DEPLOY
sudo snap install --classic heroku

heroku login

heroku ps:scale web=1

heroku git:remote -a simple-api-07

heroku buildpacks:set heroku/python


git add .

git commit -m"message"

git push heroku HEAD:master


# Test app is runable
cd simple_api/

gunicorn simple_api.wsgi

heroku local
