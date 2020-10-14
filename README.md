## News- Website - [The Social Bugg](https://thesocialbugg.herokuapp.com)
---
**My Feature**

👉 You can easily post any news from portal

👉 Seo also included

👉 Easy to deploy

## Installation for windows

install virtual env
```sh
pip install virtualenv
```
copy project to a folder then enter to a folder using cd command suppose my forder name is my_project
```sh
cd my_project
```
Once inside the project folder run: 
```sh
py -m venv env
```
To activate virtualenv on Windows, and activate the script is in the Scripts folder :
```sh
env\Scripts\activate
```
Then Install Requirements.txt
```sh
pip install -r requirements.txt
```
Now to run django project in local server (first enter to location where manage.py is located suppose loacted at pathto)
```sh
cd pathto
python manage.py migrate
```
Create super user for admain page:
```sh
python manage.py createsuperuser
```
It will ask for username, email and password
Now you can run django on your local server
```sh
python manage.py runserver
```
Now open chrome and type
```sh
loaclhost:8000
```
Done👍

## Credits

[Priyanshu](https://t.me/priyanshugandhi)
