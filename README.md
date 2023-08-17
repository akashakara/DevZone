# DevZone - The project hub
## About
DevZone is a platform where developers from all across the world can work on project ideas submitted by the owner.
# Installation
```sh
# clone repository
git clone https://github.com/akashakara/DevZone.git
cd DevZone

# make a virtual environment
python -m venv env
source env/bin/activate

# install requirements
pip install -r requirements.txt

# migrations
python manage.py makemigrations
python manage.py migrate

# run and test
python manage.py runserver
```
    
